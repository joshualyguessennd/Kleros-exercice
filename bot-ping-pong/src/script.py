import os
import json
from web3 import Web3


with open("./src/abi/abi.json", "r") as abi_file:
    pingpong_abi = json.load(abi_file)

INFURA_KEY=os.getenv("INFURA_KEY")
w3 = Web3(Web3.HTTPProvider("https://kovan.infura.io/v3/$INFURA_KEY"))
private_key = os.getenv("ETHEREUM_PRIVATE_KEY")
account = "0x27a1876A09581E02E583E002E42EC1322abE9655"

pingPongContract = w3.eth.contract(address="0x382b332863a541d764391deF0063b1dF360afc50", abi=pingpong_abi)
tx = pingPongContract.functions.pong("0xa1ea72846f0f95a25c58d83dcbdfb1b0fc411c9a51b60a50c115098c0ddb3cfc").buildTransaction({'nonce': w3.eth.getTransactionCount(account)})
signed_tx = w3.eth.account.signTransaction(tx, private_key)
w3.eth.sendRawTransaction(signed_tx.rawTransaction)