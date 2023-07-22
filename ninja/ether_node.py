from .service.chain.ether.read import read_image_path
from .service.common import COMMON, STRING, INT

CATEGORY = "NINJA/Chain/Ether"


class ReadImagePathERC721(COMMON):
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "provider_url": (STRING, {
                    "multiline": False,
                    "default": "provider_url (infura.io or alchemyapi.io)",
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
        return read_image_path(provider_url, contract_address, token_id)
