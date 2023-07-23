import json
from datetime import datetime
from io import BytesIO

import boto3
import numpy as np
from PIL import Image, PngImagePlugin

from .chain.common.opensea_metadata import make_metadata, read_image_path_on_metadata
from .common import with_debug_log, load_image_http


def load_aws_config(node, config_path):
    import configparser
    config = configparser.ConfigParser()
    config.read(config_path)
    aws_access_key_id = config['AWS_S3']['aws_access_key_id']
    aws_secret_access_key = config['AWS_S3']['aws_secret_access_key']
    region = config['AWS_S3']['region']
    bucket = config['AWS_S3']['bucket']
    return with_debug_log(aws_access_key_id, aws_secret_access_key, region, bucket)


def save_metadata_s3(node, aws_access_key_id, aws_secret_access_key, region, bucket,
                     key,
                     image_path, description, external_url, name):
    metadata = make_metadata(
        image_path=image_path,
        description=description if description else None,
        external_url=external_url if external_url else None,
        name=name if name else None
    )

    # 현재 날짜와 시간을 YYYYMMDDHHMMSS 형식의 문자열로 변환
    datetime_str = datetime.now().strftime('%Y%m%d%H%M%S')

    # Key 생성
    key = key if key else f'comfyui-{datetime_str}.json'

    # BytesIO 객체를 이용해 이미지 업로드
    s3_path = f's3://{bucket}/{key}'
    public_http_path = f'https://{bucket}.s3.{region}.amazonaws.com/{key}'

    # update metadata.json
    s3 = boto3.client('s3',
                      aws_access_key_id=aws_access_key_id,
                      aws_secret_access_key=aws_secret_access_key,
                      region_name=region)
    s3.put_object(Bucket=bucket, Key=key, Body=json.dumps(metadata))

    return with_debug_log(s3_path, public_http_path)


def save_image_s3(node, image, aws_access_key_id, aws_secret_access_key, region, bucket,
                  key,
                  prompt=None, extra_pnginfo=None):
    # torch.Tensor를 NumPy 배열로 변환
    i = 255. * image.cpu().numpy()

    # 차원 축소
    i = np.squeeze(i)

    img = Image.fromarray(np.clip(i, 0, 255).astype(np.uint8))
    metadata = PngImagePlugin.PngInfo()
    if prompt is not None:
        metadata.add_text("prompt", json.dumps(prompt))
    if extra_pnginfo is not None:
        for x in extra_pnginfo:
            metadata.add_text(x, json.dumps(extra_pnginfo[x]))

    # 바이트로 이미지 변환
    byte_arr = BytesIO()
    img.save(byte_arr, format='PNG', pnginfo=metadata)
    byte_arr = byte_arr.getvalue()

    # boto3 클라이언트 초기화
    s3 = boto3.client('s3',
                      aws_access_key_id=aws_access_key_id,
                      aws_secret_access_key=aws_secret_access_key,
                      region_name=region
                      )

    # 현재 날짜와 시간을 YYYYMMDDHHMMSS 형식의 문자열로 변환
    datetime_str = datetime.now().strftime('%Y%m%d%H%M%S')

    # Key 생성
    key = key if key else f'comfyui-{datetime_str}.png'

    # BytesIO 객체를 이용해 이미지 업로드
    s3_path = f's3://{bucket}/{key}'
    public_http_path = f'https://{bucket}.s3.{region}.amazonaws.com/{key}'
    s3.put_object(Body=byte_arr, Bucket=bucket, Key=key)

    return with_debug_log(image, s3_path, public_http_path)


def load_http_image(image_url):
    return with_debug_log(load_image_http(image_url))


def load_http_image_on_metadata(metadata_url):
    return with_debug_log(load_image_http(read_image_path_on_metadata(metadata_url)))


def copy_s3(node, file_path, aws_access_key_id, aws_secret_access_key, region, bucket):
    s3 = boto3.client('s3',
                      aws_access_key_id=aws_access_key_id,
                      aws_secret_access_key=aws_secret_access_key,
                      region_name=region
                      )
    file_name = file_path.replace('\\', '/').split('/')[-1]
    s3_path = f's3://{bucket}/{file_name}'
    s3.upload_file(file_path, bucket, file_name)
    return with_debug_log(s3_path)
