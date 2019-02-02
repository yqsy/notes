---
title: 隔离见证交易
date: 2018-02-01 13:29:12
categories: [business, bitcoin]
---

<!-- TOC -->

- [1. 说明](#1-说明)
- [2. P2WPKH](#2-p2wpkh)
- [3. P2WSH](#3-p2wsh)
- [4. P2SH-P2WPKH](#4-p2sh-p2wpkh)
- [5. P2SH-P2WSH](#5-p2sh-p2wsh)
- [6. 交易数据](#6-交易数据)
- [7. 参考资料](#7-参考资料)

<!-- /TOC -->

<a id="markdown-1-说明" name="1-说明"></a>
# 1. 说明

隔离见证是比特币的扩容方案,将见证数据移到交易的末尾并把见证脚本置为空,通过这样的方式升级可实现前向兼容,也即是旧的版本的节点可以接受隔离见证区块.这里做一下隔离见证的几个交易,然后再分析隔离见证的优缺点.

<a id="markdown-2-p2wpkh" name="2-p2wpkh"></a>
# 2. P2WPKH

加锁与解锁的堆栈:

```bash
# scriptPubKey (prev out)
scriptPubKey: 0 <20-byte-key-hash>

# scriptSig (in)
witness:      <signature> <pubkey>
scriptSig:    (empty)
```

获得一笔输出作为资金源:

```bash
# 获得coinbase的地址
COINBASEEC=`bx seed | bx ec-new`
COINBASEECADDRESS_INFO=`parse_privkey $COINBASEEC`

# 提取P2PKH地址
COINBASECP2PKHADDR=`echo $COINBASEECADDRESS_INFO | sed -n 13p | awk '{print $2}'`

bitcoin-cli generatetoaddress 101 $COINBASECP2PKHADDR

# 查询锁定脚本
bbasetx 1

# 提取私钥并导入到钱包
COINBASEPRIKEYWIF=`echo $COINBASEECADDRESS_INFO | sed -n 10p | awk '{print $2}'`
bitcoin-cli importprivkey $COINBASEPRIKEYWIF

# 查询余额
bitcoin-cli getbalance
```

获得P2WPKH的`锁定交易`:

```bash
# 获得新的地址
NEWEC=`bx seed | bx ec-new`
NEWP2WPKHADDRESS_INFO=`parse_privkey $NEWEC`

# 提取P2WPKH地址
NEWP2WPkHADDR=`echo $NEWP2WPKHADDRESS_INFO | sed -n 16p | awk '{print $2}'`

# 提取私钥,方便一会使用
NEWP2WPKHPRIKEYWIF=`echo $NEWP2WPKHADDRESS_INFO | sed -n 10p | awk '{print $2}'`

# 1) 创建交易 & 签名交易 & 发送交易
bitcoin-cli sendtoaddress $NEWP2WPkHADDR 50.0 "" "" true

# 2) 生成区块打包区块
bg 1 

# 查询这一笔交易
bhtx 102 1
```

对该比输出进行`解锁交易`,引用到该笔交易的地址,并使用私钥进行签名:
```bash
PRE_TXID=`_bhtxhash 102 1`
PRE_VOUT=0

# 获得新的地址
NEWEC=`bx seed | bx ec-new`
NEWADDRESS_INFO=`parse_privkey $NEWEC`

# 提取P2PKH地址
NEWP2PkHADDR=`echo $NEWADDRESS_INFO | sed -n 13p | awk '{print $2}'`

# 1) 创建交易
RAWTX=`bitcoin-cli createrawtransaction '''
[
    {
        "txid": "'$PRE_TXID'",
        "vout": '$PRE_VOUT'
    }
]
''' '''
{
    "'$NEWP2PkHADDR'": 49.9999
}
'''`

# 2) 签名交易
SIGNED_RAWTX_JSON=`bitcoin-cli signrawtransactionwithkey $RAWTX '''
[
    "'$NEWP2WPKHPRIKEYWIF'"
]
'''`

SIGNED_RAWTX=`echo $SIGNED_RAWTX_JSON | python -c 'import json,sys;obj=json.load(sys.stdin);print(obj["hex"])'`

# 3)发送交易
bitcoin-cli sendrawtransaction $SIGNED_RAWTX

# 4) 生成打包区块
bg 1

# 查询这一笔交易
bhtx 103 1
```


<a id="markdown-3-p2wsh" name="3-p2wsh"></a>
# 3. P2WSH

加锁与解锁的堆栈:

```bash
# scriptPubKey (prev out)
scriptPubKey: 0 <32-byte-hash>

# scriptSig (in)
witness:      0 <signature1> <1 <pubkey1> <pubkey2> 2 CHECKMULTISIG>
scriptSig:    (empty)
```


获得一笔输出作为资金源:
```bash
# 获得coinbase的地址
COINBASEEC=`bx seed | bx ec-new`
COINBASEECADDRESS_INFO=`parse_privkey $COINBASEEC`

# 提取P2PKH地址
COINBASECP2PKHADDR=`echo $COINBASEECADDRESS_INFO | sed -n 13p | awk '{print $2}'`

bitcoin-cli generatetoaddress 101 $COINBASECP2PKHADDR

# 查询锁定脚本
bbasetx 1

# 提取私钥并导入到钱包
COINBASEPRIKEYWIF=`echo $COINBASEECADDRESS_INFO | sed -n 10p | awk '{print $2}'`
bitcoin-cli importprivkey $COINBASEPRIKEYWIF

# 查询余额
bitcoin-cli getbalance
```

获得P2WSH的`锁定交易`, 2-of-3:


```bash
MULTIADDR1_EC=`bx seed | bx ec-new`
MULTIADDR1_INFO=`parse_privkey $MULTIADDR1_EC`
MULTIADDR1_ADDRESS=`echo $MULTIADDR1_INFO | sed -n 13p | awk '{print $2}'`
MULTIADDR1_PUBKEY=`echo $MULTIADDR1_INFO | sed -n 11p | awk '{print $2}'`
MULTIADDR1_PRVKEY_WIF=`echo $MULTIADDR1_INFO | sed -n 10p | awk '{print $2}'`

MULTIADDR2_EC=`bx seed | bx ec-new`
MULTIADDR2_INFO=`parse_privkey $MULTIADDR2_EC`
MULTIADDR2_ADDRESS=`echo $MULTIADDR2_INFO | sed -n 13p | awk '{print $2}'`
MULTIADDR2_PUBKEY=`echo $MULTIADDR2_INFO | sed -n 11p | awk '{print $2}'`
MULTIADDR2_PRVKEY_WIF=`echo $MULTIADDR2_INFO | sed -n 10p | awk '{print $2}'`

MULTIADDR3_EC=`bx seed | bx ec-new`
MULTIADDR3_INFO=`parse_privkey $MULTIADDR3_EC`
MULTIADDR3_ADDRESS=`echo $MULTIADDR3_INFO | sed -n 13p | awk '{print $2}'`
MULTIADDR3_PUBKEY=`echo $MULTIADDR3_INFO | sed -n 11p | awk '{print $2}'`
MULTIADDR3_PRVKEY_WIF=`echo $MULTIADDR3_INFO | sed -n 10p | awk '{print $2}'`


# 1. 创建P2SH多重签名地址 (不能丢失)
MULTISIG_JSON=`bitcoin-cli createmultisig 2 '''
[
    "'$MULTIADDR1_PUBKEY'",
    "'$MULTIADDR2_PUBKEY'",
    "'$MULTIADDR3_PUBKEY'"
]''' "bech32"`

# 脚本地址
MUTISIG_ADDRESS=`echo $MULTISIG_JSON | python -c 'import json,sys;obj=json.load(sys.stdin);print(obj["address"])'`

# 赎回脚本
MUTISIG_REDEEMSCRIPT=`echo $MULTISIG_JSON | python -c 'import json,sys;obj=json.load(sys.stdin);print(obj["redeemScript"])'`

# 2. 向多重签名地址转账
UTXOID=`bitcoin-cli sendtoaddress $MUTISIG_ADDRESS 50.00 "" "" true`

# 查询该比P2SH锁定交易的脚本 (未打包上链)
RAWTRANSACTION_JSON=`bitcoin-cli getrawtransaction $UTXOID 1`
echo $RAWTRANSACTION_JSON
```

对该比P2WSH输出进行`解锁交易`, 用任意的两个私钥进行签名:

```bash
UTXO_VOUT=0
UTXO_OUTPUT_SCRIPT=` echo $RAWTRANSACTION_JSON | 
python -c 'import json,sys;obj=json.load(sys.stdin);print(obj["vout"][0]["scriptPubKey"]["hex"])' `

# 创建新的输出地址
NEWOUTADDR_EC=`bx seed | bx ec-new`
NEWOUTADDR_INFO=`parse_privkey $NEWOUTADDR_EC`
NEWOUTADDR_ADDRESS=`echo $NEWOUTADDR_INFO | sed -n 13p | awk '{print $2}'`

# 1. 创建交易

RAWTX=`bitcoin-cli createrawtransaction '''
[
    {
        "txid": "'$UTXOID'",
        "vout": '$UTXO_VOUT'
    }
]
''' '''
{
    "'$NEWOUTADDR_ADDRESS'": 49.9999
}
'''`

# 2. 签名交易 (需要使用 1. P2SH地址 2. 赎回脚本(这个很关键))
SIGNED_RAWTX_JSON=`bitcoin-cli signrawtransactionwithkey $RAWTX '''
[
    "'$MULTIADDR1_PRVKEY_WIF'",
    "'$MULTIADDR2_PRVKEY_WIF'"
]''' '''
[
    {
        "txid": "'$UTXOID'",
        "vout": '$UTXO_VOUT',
        "scriptPubKey": "'$UTXO_OUTPUT_SCRIPT'",
        "redeemScript": "'$MUTISIG_REDEEMSCRIPT'",
        "amount": "49.99996"
    }
]
''' `

SIGNED_RAWTX=`echo $SIGNED_RAWTX_JSON | python -c 'import json,sys;obj=json.load(sys.stdin);print(obj["hex"])'`

# 3. 发送交易
bitcoin-cli sendrawtransaction $SIGNED_RAWTX

# 4. 生成打包区块
bg 1 

# 查询新地址信息
echo $NEWOUTADDR_INFO

# 导入新地址到钱包
bitcoin-cli importaddress $NEWOUTADDR_ADDRESS

# 查询新地址接受到的金额
bitcoin-cli getreceivedbyaddress $NEWOUTADDR_ADDRESS 0

# 查询这一笔交易
bhtx 102 2
```

<a id="markdown-4-p2sh-p2wpkh" name="4-p2sh-p2wpkh"></a>
# 4. P2SH-P2WPKH

加锁与解锁的堆栈:

```bash
# scriptPubKey (prev out)
scriptPubKey: HASH160 <20-byte-script-hash> EQUAL

# scriptSig (in)
witness:      <signature> <pubkey>
scriptSig:    <0 <20-byte-key-hash>>
```


获得一笔输出作为资金源:

```bash
# 获得coinbase的地址
COINBASEEC=`bx seed | bx ec-new`
COINBASEECADDRESS_INFO=`parse_privkey $COINBASEEC`

# 提取P2PKH地址
COINBASECP2PKHADDR=`echo $COINBASEECADDRESS_INFO | sed -n 13p | awk '{print $2}'`

bitcoin-cli generatetoaddress 101 $COINBASECP2PKHADDR

# 查询锁定脚本
bbasetx 1

# 提取私钥并导入到钱包
COINBASEPRIKEYWIF=`echo $COINBASEECADDRESS_INFO | sed -n 10p | awk '{print $2}'`
bitcoin-cli importprivkey $COINBASEPRIKEYWIF

# 查询余额
bitcoin-cli getbalance
```

产生一笔输出到P2SH-P2WPKH地址:
```bash

# 获得新的地址
NEWEC=`bx seed | bx ec-new`
NEWADDRESS_INFO=`parse_privkey $NEWEC`
NEWADDRESS_P2SH_P2PKH=`echo $NEWADDRESS_INFO | sed -n 15p | awk '{print $2}'`
NEWADDRESS_PRIKEY=`echo $NEWADDRESS_INFO | sed -n 10p | awk '{print $2}'`

# 1) 创建交易 & 签名交易 & 发送交易
bitcoin-cli sendtoaddress $NEWADDRESS_P2SH_P2PKH 50.00  "" "" true

# 2) 生成区块打包区块
bg 1 

# 查询这一笔交易
bhtx 102 1

```

对该比输出进行`解锁交易`,引用到该笔交易的地址,并使用私钥进行签名:

```bash

PRE_TXID=`_bhtxhash 102 1`
PRE_VOUT=0

# 获得新的地址
NEWEC=`bx seed | bx ec-new`
NEWADDRESS_INFO=`parse_privkey $NEWEC`

# 提取P2PKH地址
NEWP2PkHADDR=`echo $NEWADDRESS_INFO | sed -n 13p | awk '{print $2}'`

# 1) 创建交易
RAWTX=`bitcoin-cli createrawtransaction '''
[
    {
        "txid": "'$PRE_TXID'",
        "vout": '$PRE_VOUT'
    }
]
''' '''
{
    "'$NEWP2PkHADDR'": 49.9999
}
'''`

# 2) 签名交易
SIGNED_RAWTX_JSON=`bitcoin-cli signrawtransactionwithkey $RAWTX '''
[
    "'$NEWADDRESS_PRIKEY'"
]
'''`

SIGNED_RAWTX=`echo $SIGNED_RAWTX_JSON | python -c 'import json,sys;obj=json.load(sys.stdin);print(obj["hex"])'`

# 3)发送交易
bitcoin-cli sendrawtransaction $SIGNED_RAWTX

# 4) 生成打包区块
bg 1

# 查询新地址信息
echo $NEWADDRESS_INFO

# 导入新地址到钱包
bitcoin-cli importaddress $NEWP2PkHADDR

# 查询新地址接受到的金额
bitcoin-cli getreceivedbyaddress $NEWP2PkHADDR 0

# 查询这一笔交易
bhtx 103 1
```


<a id="markdown-5-p2sh-p2wsh" name="5-p2sh-p2wsh"></a>
# 5. P2SH-P2WSH


加锁与解锁的堆栈:

```bash
# scriptPubKey (prev out)
scriptPubKey: HASH160 <20-byte-hash> EQUAL

# scriptSig (in)
witness:      0 <signature1> <1 <pubkey1> <pubkey2> 2 CHECKMULTISIG>
scriptSig:    <0 <32-byte-hash>>
```


获得一笔输出作为资金源:
```bash
# 获得coinbase的地址
COINBASEEC=`bx seed | bx ec-new`
COINBASEECADDRESS_INFO=`parse_privkey $COINBASEEC`

# 提取P2PKH地址
COINBASECP2PKHADDR=`echo $COINBASEECADDRESS_INFO | sed -n 13p | awk '{print $2}'`

bitcoin-cli generatetoaddress 101 $COINBASECP2PKHADDR

# 查询锁定脚本
bbasetx 1

# 提取私钥并导入到钱包
COINBASEPRIKEYWIF=`echo $COINBASEECADDRESS_INFO | sed -n 10p | awk '{print $2}'`
bitcoin-cli importprivkey $COINBASEPRIKEYWIF

# 查询余额
bitcoin-cli getbalance
```

获得P2SH-P2WSH的`锁定交易`, 2-of-3:

```bash
MULTIADDR1_EC=`bx seed | bx ec-new`
MULTIADDR1_INFO=`parse_privkey $MULTIADDR1_EC`
MULTIADDR1_ADDRESS=`echo $MULTIADDR1_INFO | sed -n 13p | awk '{print $2}'`
MULTIADDR1_PUBKEY=`echo $MULTIADDR1_INFO | sed -n 11p | awk '{print $2}'`
MULTIADDR1_PRVKEY_WIF=`echo $MULTIADDR1_INFO | sed -n 10p | awk '{print $2}'`

MULTIADDR2_EC=`bx seed | bx ec-new`
MULTIADDR2_INFO=`parse_privkey $MULTIADDR2_EC`
MULTIADDR2_ADDRESS=`echo $MULTIADDR2_INFO | sed -n 13p | awk '{print $2}'`
MULTIADDR2_PUBKEY=`echo $MULTIADDR2_INFO | sed -n 11p | awk '{print $2}'`
MULTIADDR2_PRVKEY_WIF=`echo $MULTIADDR2_INFO | sed -n 10p | awk '{print $2}'`

MULTIADDR3_EC=`bx seed | bx ec-new`
MULTIADDR3_INFO=`parse_privkey $MULTIADDR3_EC`
MULTIADDR3_ADDRESS=`echo $MULTIADDR3_INFO | sed -n 13p | awk '{print $2}'`
MULTIADDR3_PUBKEY=`echo $MULTIADDR3_INFO | sed -n 11p | awk '{print $2}'`
MULTIADDR3_PRVKEY_WIF=`echo $MULTIADDR3_INFO | sed -n 10p | awk '{print $2}'`


# 1. 创建P2SH多重签名地址 (不能丢失)
MULTISIG_JSON=`bitcoin-cli createmultisig 2 '''
[
    "'$MULTIADDR1_PUBKEY'",
    "'$MULTIADDR2_PUBKEY'",
    "'$MULTIADDR3_PUBKEY'"
]''' "p2sh-segwit"`

# 脚本地址
MUTISIG_ADDRESS=`echo $MULTISIG_JSON | python -c 'import json,sys;obj=json.load(sys.stdin);print(obj["address"])'`

# 赎回脚本
MUTISIG_REDEEMSCRIPT=`echo $MULTISIG_JSON | python -c 'import json,sys;obj=json.load(sys.stdin);print(obj["redeemScript"])'`

# 2. 向多重签名地址转账
UTXOID=`bitcoin-cli sendtoaddress $MUTISIG_ADDRESS 50.00 "" "" true`

# 查询该比P2SH锁定交易的脚本 (未打包上链)
RAWTRANSACTION_JSON=`bitcoin-cli getrawtransaction $UTXOID 1`
echo $RAWTRANSACTION_JSON
```

对该比P2WSH输出进行`解锁交易`, 用任意的两个私钥进行签名:

```bash
UTXO_VOUT=0
UTXO_OUTPUT_SCRIPT=` echo $RAWTRANSACTION_JSON | 
python -c 'import json,sys;obj=json.load(sys.stdin);print(obj["vout"][0]["scriptPubKey"]["hex"])' `

# 创建新的输出地址
NEWOUTADDR_EC=`bx seed | bx ec-new`
NEWOUTADDR_INFO=`parse_privkey $NEWOUTADDR_EC`
NEWOUTADDR_ADDRESS=`echo $NEWOUTADDR_INFO | sed -n 13p | awk '{print $2}'`

# 1. 创建交易

RAWTX=`bitcoin-cli createrawtransaction '''
[
    {
        "txid": "'$UTXOID'",
        "vout": '$UTXO_VOUT'
    }
]
''' '''
{
    "'$NEWOUTADDR_ADDRESS'": 49.9999
}
'''`

# 2. 签名交易 (需要使用 1. P2SH地址 2. 赎回脚本(这个很关键))
SIGNED_RAWTX_JSON=`bitcoin-cli signrawtransactionwithkey $RAWTX '''
[
    "'$MULTIADDR1_PRVKEY_WIF'",
    "'$MULTIADDR2_PRVKEY_WIF'"
]''' '''
[
    {
        "txid": "'$UTXOID'",
        "vout": '$UTXO_VOUT',
        "scriptPubKey": "'$UTXO_OUTPUT_SCRIPT'",
        "redeemScript": "'$MUTISIG_REDEEMSCRIPT'",
        "amount": "49.9999622"
    }
]
''' `

SIGNED_RAWTX=`echo $SIGNED_RAWTX_JSON | python -c 'import json,sys;obj=json.load(sys.stdin);print(obj["hex"])'`

# 3. 发送交易
bitcoin-cli sendrawtransaction $SIGNED_RAWTX

# 4. 生成打包区块
bg 1 

# 查询新地址信息
echo $NEWOUTADDR_INFO

# 导入新地址到钱包
bitcoin-cli importaddress $NEWOUTADDR_ADDRESS

# 查询新地址接受到的金额
bitcoin-cli getreceivedbyaddress $NEWOUTADDR_ADDRESS 0

# 查询这一笔交易
bhtx 102 2
```

<a id="markdown-6-交易数据" name="6-交易数据"></a>
# 6. 交易数据

* https://raw.githubusercontent.com/yqsy/yqsy.notes/master/source/_posts/business/bitcoin/script/P2WPKH (P2WPKH)
* https://raw.githubusercontent.com/yqsy/yqsy.notes/master/source/_posts/business/bitcoin/script/P2WSH  (P2WSH)
* https://raw.githubusercontent.com/yqsy/yqsy.notes/master/source/_posts/business/bitcoin/script/P2SH (P2SH-P2WPKH)
* https://raw.githubusercontent.com/yqsy/yqsy.notes/master/source/_posts/business/bitcoin/script/RETURN (P2SH-P2WSH)

<a id="markdown-7-参考资料" name="7-参考资料"></a>
# 7. 参考资料

* https://github.com/bitcoin/bips/blob/master/bip-0141.mediawiki (BIP141)
