from .service.common import COMMON, STRING, IMAGE
from .service.storage import loadAWSConfig, saveS3
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

    RETURN_TYPES = (STRING,STRING,AWS_REGIONS,STRING)
    RETURN_NAMES = ("aws_access_key_id","aws_secret_access_key","region","bucket")
    CATEGORY = CATEGORY

    def execute(self, config_path):
        return loadAWSConfig(self, config_path)

class S3(COMMON):
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image": (IMAGE,),
                "aws_access_key_id": (STRING, {
                    "multiline": False, #True if you want the field to look like the one on the ClipTextEncode node
                    "default": "Put your AWS access key here"
                }),
                "aws_secret_access_key": (STRING, {
                    "multiline": False, #True if you want the field to look like the one on the ClipTextEncode node
                    "default": "Put your AWS secret access key here"
                }),
                "region": (AWS_REGIONS, ),
                "bucket": (STRING, {
                    "multiline": False, #True if you want the field to look like the one on the ClipTextEncode node
                    "default": "Put your bucket name here"
                }),
                
            },
        }

    RETURN_TYPES = (IMAGE,STRING)
    RETURN_NAMES = ("image","s3_path")
    CATEGORY = CATEGORY
    
    OUTPUT_NODE = True

    # 이미지는 텐서
    def execute(self, image, aws_access_key_id, aws_secret_access_key, region, bucket, prompt=None, extra_pnginfo=None):
        return saveS3(self, image, aws_access_key_id, aws_secret_access_key, region, bucket, prompt, extra_pnginfo)