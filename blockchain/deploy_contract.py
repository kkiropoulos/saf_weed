from web3 import Web3
from solcx import compile_source, install_solc
import json

GANACHE_URL = "http://127.0.0.1:7545"

w3 = Web3(Web3.HTTPProvider(GANACHE_URL))

if not w3.is_connected():
    raise Exception("Δεν υπάρχει σύνδεση με Ganache")

install_solc("0.8.0")

with open("blockchain/WeedLog.sol", "r", encoding="utf-8") as file:
    contract_source = file.read()

compiled_sol = compile_source(
    contract_source,
    output_values=["abi", "bin"],
    solc_version="0.8.0"
)

contract_id, contract_interface = compiled_sol.popitem()

abi = contract_interface["abi"]
bytecode = contract_interface["bin"]

account = w3.eth.accounts[0]

WeedLog = w3.eth.contract(abi=abi, bytecode=bytecode)

tx_hash = WeedLog.constructor().transact({"from": account})
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

contract_address = tx_receipt.contractAddress

print("Smart contract deployed!")
print("Contract address:", contract_address)

with open("blockchain/contract_info.json", "w", encoding="utf-8") as file:
    json.dump(
        {
            "address": contract_address,
            "abi": abi
        },
        file,
        indent=4
    )

print("Saved contract info to blockchain/contract_info.json")