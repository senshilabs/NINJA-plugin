from .storage import S3ImageUpload, LoadAWSConfig

# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "S3_Image_Upload": S3ImageUpload,
    "LoadAWSConfig": LoadAWSConfig,
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "S3_Image_Upload": "S3_Image_Upload",
    "LoadAWSConfig": "LoadAWSConfig",
}
