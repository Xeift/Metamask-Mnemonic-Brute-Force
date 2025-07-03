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

# 🚨 Scam Alert
If you are reading this, then you must have some interest in brute forcing. There have been some reports that recently someone was selling fake brute force scripts. None of the existing scripts are able to crack an account with ETH in a short time. To my knowledge, there's no way to reverse, crack, or speed up SHA-256 efficiently, even with quantum algorithms. If you see someone claiming that their script can find an address with ETH in it without any additional knowledge (e.g., the mnemonic words that derive that address but in the wrong order, the first 8 mnemonic words of that address, etc.), then that's 100% a scam.

How does the scam work?
> 1. They sell the script.
> 2. They write some logic to display a mnemonic that derives an account owned by them when you run the script for a while.
> 3. There is USDT in that account, but it lacks ETH to pay for gas.
> 4. You want to get the USDT out of that account, so you transfer ETH to that account, and your ETH will be immediately transferred to the scammer once the account receives it.

So steps `1` and `4` are how they make money. Sometimes they even implement ransomware or keyloggers.

Since this script is under the MIT license, you are free to modify, sell, or do whatever you want with it. I don't really care. But please remember, **do not run the code if you don't know how it works**. You can ask ChatGPT if there's anything malicious before running any code. Stay safe.
