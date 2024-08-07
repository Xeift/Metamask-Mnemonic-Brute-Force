import json
import requests
from web3 import Web3
from mnemonic import Mnemonic
import threading

web3 = Web3(Web3.HTTPProvider("https://eth-mainnet.g.alchemy.com/v2/JCNCAmqFfaWQ9WQrW143reOVrnRg1YfY"))


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
