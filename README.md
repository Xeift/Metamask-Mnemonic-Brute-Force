# Metamask-Mnemonic-Brute-Force
A js program random generate 12 words metamask mnemonic and check the balance in the account.

Requirement
-----------------
* ethers

Quickstart
-----------------

You can run it on repl.it (A cloud IDE) or on your PC.

Try it [here](https://replit.com/@xeiftc/MetamaskMnemonicBruteForce).

If there's ether in wallet, it will record to `cracked.json`.

Tutorial
-----------------
1. Download [this script](https://github.com/Xeift/Metamask-Mnemonic-Brute-Force/archive/refs/heads/main.zip)

2. Run `npm i` in your terminal

3. Run `node index.js` in your terminal

Note
-----------------
THIS SCRIPT IS FOR EDUCATIONAL PURPOSE ONLY AND IT'S NOT EFFICIENT, IT'S MORE POSSIBLE YOU WON THE LOTTERY THAN FOUND AN ACCOUNT WITH ETH.

How long will it takes to find a non empty account?

Refer to [BIP-39 wordlist](https://github.com/bitcoin/bips/blob/master/bip-0039/english.txt), we know there's total 2048 possible words. So a 12 word mnemonic have: 
```
2048 × 2048 × …… × 2048
= 2048 ^ 12
= 5444517870735015415413993718908291383296
```
permutations.

According to [Etherscan](https://etherscan.io/chart/address), there are 
```
276766564
```
unique address(have ether in that account or have txn before) on Ethereum.

We can now caculate 'how many times we need to guess a non empty 12 words wallet':
```
5444517870735015415413993718908291383296 ÷ 276766564 = 19671877238520096001965012359326.36
```

This script can try 350000 permutations(mnemonic) in a day. You can simply calculate:
```
19671877238520096001965012359326.36 ÷ 350000 ÷ 365 = 153987297366106426629863.11 years
```

# Okay, so what does that means?

That means you need **42618535191663525756665312868166.66 years** to brute force a wallet with Ether in it.

If you want to get rich by brute force, I suggest you buy some fried chicken and beers, go home and watch Netflix the whole day and forget everything about brute force.