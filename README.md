# Metamask-Mnemonic-Brute-Force
A js program random generate 12 words metamask mnemonic and check the balance in the account.

Requirement
-----------------
* ethers

* web3

* bip39

Quickstart
-----------------

You can run it on repl.it or on your PC.

Just change web3 provider api in line 4. You can use Infura, Alchemy or other web3 provider.

If there's no eth in the account, then mnemonic and address will be record to `zerobalance.txt`.

Otherwise will record to `cracked.txt`

if you want to run it on replit, line 4 should look like this:

`const api = process.env['api'] // web3 provider api`

put your web3 provider url in environment variable, key = api, value = 'https://infura......'

if you want to run it on your pc, line 4 should look like this:

`const api = 'https://infura......' // web3 provider api`

# IF YOU KNOW NOTHING ABOUT JAVASCRIPT, **DO NOT DM ME**. CONSIDER LEARN JS FIRST, I DON'T HAVE TIME ANSWERING YOUR STUPID QUESTIONS.
