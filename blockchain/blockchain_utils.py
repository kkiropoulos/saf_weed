from web3 import Web3
import json

GANACHE_URL = "http://127.0.0.1:7545"

w3 = Web3(Web3.HTTPProvider(GANACHE_URL))

with open("blockchain/contract_info.json", "r", encoding="utf-8") as file:
    contract_info = json.load(file)

contract = w3.eth.contract(
    address=contract_info["address"],
    abi=contract_info["abi"]
)

account = w3.eth.accounts[0]

def add_record(image_name, crop_count, weed_count, decision, explanation):
    tx_hash = contract.functions.addRecord(
        image_name,
        int(crop_count),
        int(weed_count),
        decision,
        explanation
    ).transact({"from": account})

    receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    return receipt.transactionHash.hex()

def get_records_count():
    return contract.functions.getRecordsCount().call()