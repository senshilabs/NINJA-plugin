from .astar_node import ReadImagePathERC721 as AstarReadImagePathERC721
from .astar_node import ReadImagePathPSP34 as AstarReadImagePathPSP34
from .astar_node import ReadAttributePSP43 as AstarReadAttributePSP43
from .ether_node import ReadImagePathERC721 as EtherReadImagePathERC721
from .storage import S3ImageUpload, LoadAWSConfig, S3FileUpload, LoadImageHTTP, S3MetadataUpload
from .http import HttpCall

# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "S3ImageUpload": S3ImageUpload,
    "S3MetadataUpload": S3MetadataUpload,
    "LoadAWSConfig": LoadAWSConfig,
    "S3FileUpload": S3FileUpload,
    "LoadImageHTTP": LoadImageHTTP,
    "EtherReadImagePathERC721": EtherReadImagePathERC721,
    "AstarReadImagePathERC721": AstarReadImagePathERC721,
    "AstarReadImagePathPSP34": AstarReadImagePathPSP34,
    "AstarReadAttributePSP43": AstarReadAttributePSP43,
    "HttpCall": HttpCall,
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "S3ImageUpload": "S3 Image Upload",
    "S3MetadataUpload": "S3 Metadata Upload",
    "LoadAWSConfig": "Load AWS Config",
    "S3FileUpload": "S3 File Upload",
    "LoadImageHTTP": "Load Image HTTP",
    "EtherReadImagePathERC721": "Ether Read Image Path ERC721",
    "AstarReadImagePathERC721": "Astar Read Image Path ERC721",
    "AstarReadImagePathPSP34": "Astar Read Image Path PSP34",
    "AstarReadAttributePSP43": "Astar Read Attribute PSP43",
    "HttpCall": "HttpCall",
}
