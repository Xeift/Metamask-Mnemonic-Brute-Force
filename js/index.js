const ethers = require('ethers')
const fs = require('fs/promises');
const path = require('path');

require('dotenv').config({
    path: path.resolve(__dirname, '.env'),
});

let WEB3_PROVIDER_ENDPOINT = process.env.WEB3_PROVIDER_ENDPOINT;

if (WEB3_PROVIDER_ENDPOINT) {
    console.log(`Using WEB3_PROVIDER_ENDPOINT in .env! (${WEB3_PROVIDER_ENDPOINT.slice(0, 10)}...${WEB3_PROVIDER_ENDPOINT.slice(-3)})`);
} else {
    WEB3_PROVIDER_ENDPOINT = 'https://eth-mainnet.g.alchemy.com/v2/JCNCAmqFfaWQ9WQrW143reOVrnRg1YfY';
    console.log(`Environment variable WEB3_PROVIDER_ENDPOINT not found! Using default hard-coded endpoint! (${WEB3_PROVIDER_ENDPOINT.slice(0, 10)}...${WEB3_PROVIDER_ENDPOINT.slice(-3)}) Consider create a .env file and add your own WEB3_PROVIDER_ENDPOINT in it.`);
    // You should NOT put your endpoint here!!! Instead, create a .env file. I created the above endpoint using a disposable email address, it's not guaranteed to work.
}
const provider = new ethers.JsonRpcProvider(WEB3_PROVIDER_ENDPOINT);

async function main() {
    while (1) {
        let wallet = ethers.Wallet.createRandom(); // create a new wallet
        let mnemonic = wallet.mnemonic.phrase; // mnemonic
        let address = wallet.address; // address
        let balance = ethers.formatEther(await provider.getBalance(wallet.address)); // balance

        if (balance === '0.0') { // no ether in wallet
            console.log(`❌ address: ${address} balance: ${balance}`)
            console.log(`mnemonic: ${mnemonic}\n`);
        }
        else { // found ether in wallet
            console.log(`✅ address: ${address} balance: ${balance}`)
            console.log(`mnemonic: ${mnemonic}\n`);
            let crackedData;
            await fs.readFile('./cracked.json') // log to json file
                .then(data => {
                    crackedData = JSON.parse(data);
                })
                .catch(err => {
                    throw err;
                });

            crackedData[address] = {
                'mnemonic': mnemonic,
                'balance': balance
            };
            await fs.writeFile(
                './cracked.json',
                JSON.stringify(crackedData, null, 4),
                'utf8'
            );
        }
    }
}

main()