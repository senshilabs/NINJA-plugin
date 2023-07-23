from .service.chain.astar.read import read_attribute as read_attribute_substrate
from .service.chain.astar.read import read_image_path as read_image_path_substrate
from .service.chain.ether.read import read_image_path as read_image_path_evm
from .service.common import COMMON, STRING, INT

CATEGORY = "NINJA/Chain/Astar"


class ReadImagePathERC721(COMMON):
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "provider_url": (STRING, {
                    "multiline": False,
                    "default": "https://evm.astar.network",
                }),
                "contract_address": (STRING, {
                    "multiline": False,
                    "default": "contract_address",
                }),
                "token_id": (INT, {
                    "multiline": False,
                    "default": 0,
                }),
            },
        }

    RETURN_TYPES = (STRING,)
    RETURN_NAMES = ("image_url",)
    CATEGORY = CATEGORY

    def execute(self, provider_url, contract_address, token_id):
        return read_image_path_evm(provider_url, contract_address, token_id)


class ReadImagePathPayableMint(COMMON):
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "rpc_url": (STRING, {
                    "multiline": False,
                    "default": "wss://rpc.astar.network",
                }),
                "contract_address": (STRING, {
                    "multiline": False,
                    "default": "contract_address",
                }),
                "id": (INT, {
                    "multiline": False,
                    "default": 0,
                }),
            },
        }

    RETURN_TYPES = (STRING,)
    RETURN_NAMES = ("image_url",)
    CATEGORY = CATEGORY

    def execute(self, rpc_url, contract_address, id):
        return read_image_path_substrate(rpc_url, contract_address, id)


class ReadAttributePSP43(COMMON):
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "rpc_url": (STRING, {
                    "multiline": False,
                    "default": "wss://rpc.astar.network",
                }),
                "contract_address": (STRING, {
                    "multiline": False,
                    "default": "contract_address",
                }),
                "id": (INT, {
                    "multiline": False,
                    "default": 0,
                }),
                "attribute_key": (STRING, {
                    "multiline": False,
                    "default": "baseUri",
                }),
            },
        }

    RETURN_TYPES = (STRING,)
    RETURN_NAMES = ("image_url",)
    CATEGORY = CATEGORY

    def execute(self, rpc_url, contract_address, id, attribute_key):
        return read_attribute_substrate(rpc_url, contract_address, id, attribute_key)
