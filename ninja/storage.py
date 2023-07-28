from .service.common import COMMON, STRING, IMAGE
from .service.storage import load_aws_config, save_image_s3, copy_s3, save_metadata_s3, load_image_on_metadata, \
    load_image

CATEGORY = "NINJA/Storage"

AWS_REGIONS = [
    'us-east-1',
    'us-east-2',
    'us-west-1',
    'us-west-2',
    'af-south-1',
    'ap-east-1',
    'ap-south-1',
    'ap-northeast-2',
    'ap-southeast-1',
    'ap-southeast-2',
    'ap-northeast-1',
    'ca-central-1',
    'eu-central-1',
    'eu-west-1',
    'eu-west-2',
    'eu-south-1',
    'eu-west-3',
    'eu-north-1',
    'me-south-1',
    'sa-east-1'
]


class LoadImageViaMetadataFromURL(COMMON):
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "metadata_url": (STRING, {
                    "multiline": False,
                    "default": "http://"
                }),
            },
        }

    RETURN_TYPES = (IMAGE,)
    RETURN_NAMES = ("image",)
    CATEGORY = CATEGORY

    def execute(self, metadata_url):
        return load_image_on_metadata(metadata_url)


class LoadImageFromUrl(COMMON):
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image_url": (STRING, {
                    "multiline": False,
                    "default": "http://"
                }),
            },
        }

    RETURN_TYPES = (IMAGE,)
    RETURN_NAMES = ("image",)
    CATEGORY = CATEGORY

    def execute(self, image_url):
        return load_image(image_url)

class LoadAWSConfig(COMMON):
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "config_path": (STRING, {
                    "multiline": False,
                    "default": "Put your AWS Config path here"
                }),
            },
        }

    RETURN_TYPES = (STRING, STRING, AWS_REGIONS, STRING)
    RETURN_NAMES = ("aws_access_key_id", "aws_secret_access_key", "region", "bucket")
    CATEGORY = CATEGORY

    def execute(self, config_path):
        return load_aws_config(self, config_path)


class S3ImageUpload(COMMON):
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image": (IMAGE,),
                "aws_access_key_id": (STRING, {
                    "multiline": False,
                    "default": "Put your AWS access key here"
                }),
                "aws_secret_access_key": (STRING, {
                    "multiline": False,
                    "default": "Put your AWS secret access key here"
                }),
                "region": (AWS_REGIONS,),
                "bucket": (STRING, {
                    "multiline": False,
                    "default": "Put your bucket name here"
                }),
                "optional_key": (STRING, {
                    "multiline": False,
                    "default": ""
                }),
            },
        }

    RETURN_TYPES = (IMAGE, STRING, STRING)
    RETURN_NAMES = ("image", "s3_path", "http_public_url(only if public)")
    CATEGORY = CATEGORY

    OUTPUT_NODE = True

    def execute(self, image, aws_access_key_id, aws_secret_access_key, region, bucket,
                optional_key,
                prompt=None, extra_pnginfo=None):
        return save_image_s3(self, image, aws_access_key_id, aws_secret_access_key, region, bucket,
                             optional_key,
                             prompt, extra_pnginfo)


class S3MetadataUpload(COMMON):
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "aws_access_key_id": (STRING, {
                    "multiline": False,
                    "default": "Put your AWS access key here"
                }),
                "aws_secret_access_key": (STRING, {
                    "multiline": False,
                    "default": "Put your AWS secret access key here"
                }),
                "region": (AWS_REGIONS,),
                "bucket": (STRING, {
                    "multiline": False,
                    "default": "Put your bucket name here"
                }),
                "image_path": (STRING, {
                    "multiline": False,
                    "default": "Put your image path here"
                }),
                "description": (STRING, {
                    "multiline": True,
                    "default": "Put your description here (empty for none)"
                }),
                "external_url": (STRING, {
                    "multiline": False,
                    "default": "Put your external url here (empty for none)"
                }),
                "name": (STRING, {
                    "multiline": False,
                    "default": "Put your name here (empty for none)"
                }),
                "optional_key": (STRING, {
                    "multiline": False,
                    "default": ""
                }),
            },
        }

    RETURN_TYPES = (STRING, STRING)
    RETURN_NAMES = ("s3_path", "http_public_url(only if public)")
    CATEGORY = CATEGORY

    OUTPUT_NODE = True

    def execute(self, aws_access_key_id, aws_secret_access_key, region, bucket,
                optional_key,
                image_path, description, external_url, name, prompt=None, extra_pnginfo=None):
        return save_metadata_s3(self, aws_access_key_id, aws_secret_access_key, region, bucket,
                                optional_key,
                                image_path, description, external_url, name)


class S3FileUpload(COMMON):
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "local_file_path": (STRING, {
                    "multiline": False,
                    "default": "Local File Path"
                }),
                "aws_access_key_id": (STRING, {
                    "multiline": False,
                    "default": "Put your AWS access key here"
                }),
                "aws_secret_access_key": (STRING, {
                    "multiline": False,
                    "default": "Put your AWS secret access key here"
                }),
                "region": (AWS_REGIONS,),
                "bucket": (STRING, {
                    "multiline": False,
                    "default": "Put your bucket name here"
                }),

            },
        }

    RETURN_TYPES = (STRING,)
    RETURN_NAMES = ("s3_path",)
    CATEGORY = CATEGORY

    OUTPUT_NODE = True

    # 이미지는 텐서
    def execute(self, local_file_path, aws_access_key_id, aws_secret_access_key, region, bucket):
        return copy_s3(self, local_file_path, aws_access_key_id, aws_secret_access_key, region, bucket)
