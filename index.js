const ethers = require("ethers");
const Web3   = require("web3");
const bip39  = require("bip39");
const api = process.env['api']// web3 provider api
const provider = new Web3(new Web3.providers.HttpProvider(api));

async function main() {
  while(1){
    var mnemonic = bip39.generateMnemonic();
    var wallet   = ethers.Wallet.fromMnemonic(mnemonic);
    var address  = wallet.address;    
    var balance = await provider.eth.getBalance(address);
    
    if (balance !== '0')// eth in this account
    {
      // write mnemonic and address to cracked.txt
      const fs = require('fs')
      const content = mnemonic+'\n'+address+'\n'
      
      fs.appendFile('cracked.txt', content, err => {
        if (err) {
          console.error(err)
          return;
        }
      })
    }  
    else// no eth in this account
    {
      // write mnemonic and address to zerobalance.txt
      const fs = require('fs')
      const content = mnemonic+'\n'+address+'\n'
      
      fs.appendFile('zerobalance.txt', content, err => {
        if (err) {
          console.error(err)
          return;
        }
      })      
    }
    //    
    console.log(address);
    console.log("balance: ", balance);
  }
}

main()
    .then(() => {
        process.exit(0)
    })
    .catch((error) => {
        console.error(error);
        process.exit(1);
    });