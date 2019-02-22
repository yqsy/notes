<!-- TOC -->

- [1. 说明](#1-说明)
- [2. 交易数据](#2-交易数据)

<!-- /TOC -->


<a id="markdown-1-说明" name="1-说明"></a>
# 1. 说明

ethereum的交易的原理和比特币略有不同,相同之处都是使用secp256k1


不过比特币运用`unspent transaction output (UTXO)`表示的`余额状态`的方式,在ethereum中变成了 Receipt Tree (收据树), State Tree (状态树). 我们做几笔交易来分析一下:

参照之前的<私有链>在本地搭建一个挖矿环境,我们做一笔交易:

```bash
# 挖矿账号如下
私钥: 6c2f62fe367e43a29546ccbea84740be00d42efcde81fe9e96cc80a2039e4e89
公钥: e1af61498eccd7706ac307ab4645037f465360f28633831c35b14020cc4481b7648bb054dcf50977c895015078f6b2f45688b20ff379df5f79cd5b9ec65983ac
地址: 5351b0ead94e9d5cb69798e1cbc2af99e6764eb7

# 新建一个账号做测试：
私钥: 5f33b36aadc0f0308a278795767a2df8bd6fed81515e3a232663d0fdef651518
公钥: 3cc5e3de38726b2b85b653e417168f83abfe5110b4f7e18cbc0ee61ab908288d50570f86c7ebfce9eeb233975df43b25c96754d033ccc60798baf057ebe05f6d
地址: 9b344df1bf52da04b988361d1f52e75111aa8b11

# 连接窗口
geth attach ipc:/mnt/disk1/linux/env/ethereum/data1/geth.ipc

# 导入账号
personal.importRawKey('5f33b36aadc0f0308a278795767a2df8bd6fed81515e3a232663d0fdef651518', '123456')

# 打印账号 (2个)
eth.accounts

# 发送交易
var sender = eth.accounts[0];
var receiver = eth.accounts[1];
var amount = web3.toWei(0.01, "ether");
# 返回交易hash
var txid=personal.sendTransaction({from:sender, to:receiver, value: amount}, '123456');

# 查询交易
eth.getTransaction(txid);

# 查询区块
var blockid=eth.getTransaction(txid).blockHash;
eth.getBlock(blockid);
```

<a id="markdown-2-交易数据" name="2-交易数据"></a>
# 2. 交易数据
