import json
import os
import threading

import requests
from dotenv import load_dotenv
from mnemonic import Mnemonic
from web3 import Web3

load_dotenv()

WEB3_PROVIDER_ENDPOINT = os.getenv("WEB3_PROVIDER_ENDPOINT")
if WEB3_PROVIDER_ENDPOINT:
    print(f"Using WEB3_PROVIDER_ENDPOINT in .env! ({WEB3_PROVIDER_ENDPOINT[:10]}...{WEB3_PROVIDER_ENDPOINT[-3:]})")
else:
    WEB3_PROVIDER_ENDPOINT = "https://eth-mainnet.g.alchemy.com/v2/JCNCAmqFfaWQ9WQrW143reOVrnRg1YfY"
    print(f"Environment variable WEB3_PROVIDER_ENDPOINT not found! Using default hard-coded endpoint! ({WEB3_PROVIDER_ENDPOINT[:10]}...{WEB3_PROVIDER_ENDPOINT[-3:]}) Consider create a .env file and add your own WEB3_PROVIDER_ENDPOINT in it.")
    # You should NOT put your endpoint here!!! Instead, create a .env file. I created the above endpoint using a disposable email address, it's not guaranteed to work.  

web3 = Web3(Web3.HTTPProvider(WEB3_PROVIDER_ENDPOINT))


def generateMnemonicAndAddress():
    mnemo = Mnemonic("english")
    mnemonic = mnemo.generate(128)
    web3.eth.account.enable_unaudited_hdwallet_features()
    account = web3.eth.account.from_mnemonic(
        mnemonic,
        account_path="m/44'/60'/0'/0/0"
    )
    address = account.address

    return (mnemonic, address)

def process(c):
    while True:
        try:
            print("--------------------------------------------------")
            (mnemonic, address) = generateMnemonicAndAddress()
            balance = web3.eth.get_balance(address)
            print(f"Round {c}")
            print(f"Mnemonic: {mnemonic}")
            print(f"Address: {address}")
            if balance != 0.0:
                with open("log.txt", "a", encoding="utf-8") as file:
                    file.write(f"Mnemonic: {mnemonic}\nAddress:  {address}\nEther balance: {balance}\n")
                print(f"✅Balance: {balance}")
            else:
                print(f"❌Balance: {balance}")
            print("--------------------------------------------------\n")
            
            c += 1
        except Exception as e:
            print(e)


threads = []
for i in range(512):
    t = threading.Thread(target=process, args=(i+1,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
