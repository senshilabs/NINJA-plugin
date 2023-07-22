from .astar_node import ReadImagePathERC721 as AstarReadImagePathERC721
from .astar_node import ReadImagePathPSP43 as AstarReadImagePathPSP43
from .ether_node import ReadImagePathERC721 as EtherReadImagePathERC721
from .storage import S3ImageUpload, LoadAWSConfig, S3FileUpload, LoadImageHTTP

# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "S3ImageUpload": S3ImageUpload,
    "LoadAWSConfig": LoadAWSConfig,
    "S3FileUpload": S3FileUpload,
    "LoadImageHTTP": LoadImageHTTP,
    "EtherReadImagePathERC721": EtherReadImagePathERC721,
    "AstarReadImagePathERC721": AstarReadImagePathERC721,
    "AstarReadImagePathPSP43": AstarReadImagePathPSP43,
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "S3ImageUpload": "S3 Image Upload",
    "LoadAWSConfig": "Load AWS Config",
    "S3FileUpload": "S3 File Upload",
    "LoadImageHTTP": "Load Image HTTP",
    "EtherReadImagePathERC721": "EtherReadImagePathERC721",
    "AstarReadImagePathERC721": "AstarReadImagePathERC721",
    "AstarReadImagePathPSP43": "AstarReadImagePathPSP43",
}
