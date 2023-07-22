from web3 import Web3
import requests
from ninja.service.chain.common.erc721 import ABI
from ninja.service.common import with_debug_log


def read_image_path(provider_url, contract_address, token_id):
    w3 = Web3(Web3.HTTPProvider(provider_url))
    checksum_address = Web3.to_checksum_address(contract_address)
    abi = ABI
    contract = w3.eth.contract(address=checksum_address, abi=abi)
    token_uri = contract.functions.tokenURI(token_id).call()
    metadata = requests.get(token_uri).json()
    image_url = metadata["image"]
    return with_debug_log(image_url)
