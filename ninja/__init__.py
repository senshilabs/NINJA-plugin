from .storage import S3ImageUpload, LoadAWSConfig, S3FileUpload

# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "S3ImageUpload": S3ImageUpload,
    "LoadAWSConfig": LoadAWSConfig,
    "S3FileUpload": S3FileUpload,
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "S3ImageUpload": "S3 Image Upload",
    "LoadAWSConfig": "Load AWS Config",
    "S3FileUpload": "S3 File Upload",
}
