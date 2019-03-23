
<!-- TOC -->

- [1. networkid](#1-networkid)
- [2. interface](#2-interface)

<!-- /TOC -->

<a id="markdown-1-networkid" name="1-networkid"></a>
# 1. networkid

* https://ethereum.stackexchange.com/questions/17051/how-to-select-a-network-id-or-is-there-a-list-of-network-ids


```
0: Olympic, Ethereum public pre-release testnet
1: Frontier, Homestead, Metropolis, the Ethereum public main network
1: Classic, the (un)forked public Ethereum Classic main network, chain ID 61
1: Expanse, an alternative Ethereum implementation, chain ID 2
2: Morden, the public Ethereum testnet, now Ethereum Classic testnet
3: Ropsten, the public cross-client Ethereum testnet
4: Rinkeby, the public Geth PoA testnet
8: Ubiq, the public Gubiq main network with flux difficulty chain ID 8
42: Kovan, the public Parity PoA testnet
77: Sokol, the public POA Network testnet
99: Core, the public POA Network main network
100: xDai, the public MakerDAO/POA Network main network
401697: Tobalaba, the public Energy Web Foundation testnet
7762959: Musicoin, the music blockchain
61717561: Aquachain, ASIC resistant chain
[Other]: Could indicate that your connected to a local development test network.
```

<a id="markdown-2-interface" name="2-interface"></a>
# 2. interface

* http 
* ipc

http:  
url: /mnt/disk1/linux/env/ethereum/data1/geth.ipc  
权限: eth:1.0 net:1.0 rpc:1.0 web3:1.0

ipc:
url: ipc:/mnt/disk1/linux/env/ethereum/data1/geth.ipc  
权限: admin:1.0 debug:1.0 eth:1.0 ethash:1.0 miner:1.0 net:1.0 personal:1.0 rpc:1.0 txpool:1.0 web3:1.0

也就是ipc多了:  

* admin:1.0 
* debug:1.0
* ethash:1.0
* miner:1.0 
* personal:1.0
* txpool:1.0

