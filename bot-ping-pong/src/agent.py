import json
import os
from web3 import Web3
from forta_agent import Finding, FindingType, FindingSeverity
from src.const import PINGPONG_ADDRESS

# ping pong abi
with open("./src/abi/abi.json", "r") as abi_file:
    pingpong_abi = json.load(abi_file)

# connect to web3 provider
INFURA_KEY=os.getenv("INFURA_KEY")
w3 = Web3(Web3.HTTPProvider("https://kovan.infura.io/v3/$INFURA_KEY"))
private_key = os.getenv("ETHEREUM_PRIVATE_KEY")
account = "0x27a1876A09581E02E583E002E42EC1322abE9655"
# enumerate Event 
ping_abi = next((x for x in pingpong_abi if x.get('name', "") == "Ping"), None)
pong_abi = next((x for x in pingpong_abi if x.get('name', "") == "Pong"), None)


startedBlock = w3.eth.get_block('latest')
f = open('./src/block.txt', 'a')
f.write(f"{startedBlock.number}")
f.close()


targeted_events = {
    'ping': ping_abi,
    'pong': pong_abi
}


# start script 
def handle_transaction(transaction_event):
    findings = []
    
    # filter event
    events = transaction_event.filter_log([json.dumps(x) for x in list(targeted_events.values())], PINGPONG_ADDRESS)
    for event in events:
        event_name = event.get("event")
        hash = transaction_event.hash
        if event_name == 'Ping':
            findings.append(
                Finding({
                    'name': 'Ping event listener',
                    'description': f'this bot listen ping event and run pong function',
                    'alert_id': 'PINGPONG-1',
                    'protocol': "ethereum-kovan",
                    'type': FindingType.Info,
                    'severity': FindingSeverity.Info,
                    'metadata': {
                        'txHash': hash,
                        'starting': startedBlock.number
                    }
                })
            )
            pingPongContract = w3.eth.contract(address=PINGPONG_ADDRESS, abi=pingpong_abi)
            tx = pingPongContract.functions.pong(hash).buildTransaction({'nonce': w3.eth.getTransactionCount(account)})
            signed_tx = w3.eth.account.signTransaction(tx, private_key)
            w3.eth.sendRawTransaction(signed_tx.rawTransaction)
    return findings

