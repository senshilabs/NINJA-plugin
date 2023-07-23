import json

from substrateinterface import SubstrateInterface, Keypair
from substrateinterface.contracts import ContractInstance, ContractMetadata

from ..common.psp34 import ABI as ABI_PSP34
from ..common.payable_mint import ABI as ABI_PAYABLE_MINT
from ...common import with_debug_log


def read_attribute(rpc_url, contract_address, id, key):
    substrate = SubstrateInterface(url=rpc_url)

    contract = ContractInstance(
        contract_address=contract_address,
        metadata=ContractMetadata(json.loads(ABI_PSP34), substrate),
        substrate=substrate
    )

    dummy_keypair = Keypair.create_from_uri('//Alice')

    resp = contract.read(dummy_keypair, "PSP34Metadata::get_attribute", {
        "id": {
            "U8": id
        },
        "key": key
    }).value
    return with_debug_log(resp['result']['Ok']['data']['Ok'])


def read_image_path(rpc_url, contract_address, id):
    substrate = SubstrateInterface(url=rpc_url)

    contract = ContractInstance(
        contract_address=contract_address,
        metadata=ContractMetadata(json.loads(ABI_PAYABLE_MINT), substrate),
        substrate=substrate
    )

    dummy_keypair = Keypair.create_from_uri('//Alice')

    resp = contract.read(dummy_keypair, "PayableMint::token_uri", {
        "id": {
            "U8": id
        },
    }).value
    print(resp)
    return with_debug_log(resp['result']['Ok']['data']['Ok'])
