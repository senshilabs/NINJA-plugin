from PIL import Image, PngImagePlugin
from io import BytesIO
import numpy as np
import boto3
from datetime import datetime

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

class S3Upload:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image": ("IMAGE",),
                "aws_access_key_id": ("STRING", {
                    "multiline": False, #True if you want the field to look like the one on the ClipTextEncode node
                    "default": "Put your AWS access key here"
                }),
                "aws_secret_access_key": ("STRING", {
                    "multiline": False, #True if you want the field to look like the one on the ClipTextEncode node
                    "default": "Put your AWS secret access key here"
                }),
                "region_name": (AWS_REGIONS, ),
                "my_bucket": ("STRING", {
                    "multiline": False, #True if you want the field to look like the one on the ClipTextEncode node
                    "default": "Put your bucket name here"
                }),
                
            },
        }

    RETURN_TYPES = ("IMAGE",)

    FUNCTION = "upload"

    CATEGORY = "SenshiLabs"

    # 이미지는 텐서
    def upload(self, image, aws_access_key_id, aws_secret_access_key, region_name, my_bucket, prompt=None, extra_pnginfo=None):
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
            region_name=region_name
        )

        # 현재 날짜와 시간을 YYYYMMDDHHMMSS 형식의 문자열로 변환
        datetime_str = datetime.now().strftime('%Y%m%d%H%M%S')

        # Key 생성
        key = f'comfyui-{datetime_str}.png'

        # BytesIO 객체를 이용해 이미지 업로드
        s3.put_object(Body=byte_arr, Bucket=my_bucket, Key=key)

        return (image,)

        filename_prefix += self.prefix_append
        full_output_folder, filename, counter, subfolder, filename_prefix = folder_paths.get_save_image_path(filename_prefix, self.output_dir, images[0].shape[1], images[0].shape[0])
        results = list()
        for image in images:
            i = 255. * image.cpu().numpy()
            img = Image.fromarray(np.clip(i, 0, 255).astype(np.uint8))
            metadata = PngInfo()
            if prompt is not None:
                metadata.add_text("prompt", json.dumps(prompt))
            if extra_pnginfo is not None:
                for x in extra_pnginfo:
                    metadata.add_text(x, json.dumps(extra_pnginfo[x]))

            file = f"{filename}_{counter:05}_.png"
            img.save(os.path.join(full_output_folder, file), pnginfo=metadata, compress_level=4)
            results.append({
                "filename": file,
                "subfolder": subfolder,
                "type": self.type
            })
            counter += 1

        return { "ui": { "images": results } }

# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "S3Upload": S3Upload
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "S3Upload": "S3 Upload"
}
