---
title: 交易费用
date: 2018-02-01 13:29:12
categories: [business, bitcoin]
---

<!-- TOC -->

- [1. 说明](#1-说明)
- [2. pay to public key (P2PK)](#2-pay-to-public-key-p2pk)
- [3. pay to public key hash(P2PKH)](#3-pay-to-public-key-hashp2pkh)
- [4. pay to script hash (P2SH)](#4-pay-to-script-hash-p2sh)
- [5. OP_RETURN](#5-op_return)
- [6. 交易数据](#6-交易数据)
- [7. 参考资料](#7-参考资料)

<!-- /TOC -->

<a id="markdown-1-说明" name="1-说明"></a>
# 1. 说明

上一文<密钥和地址>我们讲到比特币的转账借助了`unspent transaction output (UTXO)`(未花费输出),`Secp256k1 with ECDSA`(椭圆曲线数字签名)等技术,完成了货币的支付职能.这一文我们了解其具体实现的方式-脚本语言.

比特币的脚本语言使用了基于堆栈的执行方式,也即是计算机最底层的汇编语言的执行方式.而比特币的交易验证引擎依赖于两类脚本来验证比特币的交易:

* `锁定交易` - 表示所属权身份(公钥/公钥hash),只有使用私钥进行签名才可以解锁
* `解锁交易` - 使用私钥进行签名解锁,随即可以生成新的锁定交易,将货币的所属权交给新的身份(公钥/公钥hash)

**请注意,以下示例每一次启动前都会删除所有的历史数据!**

<a id="markdown-2-pay-to-public-key-p2pk" name="2-pay-to-public-key-p2pk"></a>
# 2. pay to public key (P2PK)

参考中本聪在2009年所创造的创世区块时的`锁定交易`
```bash
CreateGenesisBlock

CScript() << ParseHex("04678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb649f6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5f") << OP_CHECKSIG;
```

rpc指令generate出块奖励的`锁定脚本`:
```bash
generate -> CWallet::GetScriptForMining

script->reserveScr
ipt = CScript() << ToByteVector(pubkey) << OP_CHECKSIG;
```

解锁交易时的`签名`:

```bash
signrawtransactionwithkey -> SignTransaction -> ProduceSignature -> SignStep -> CreateSig -> MutableTransactionSignatureCreator::CreateSig -> CKey::Sign
```

加锁与解锁的堆栈:

```bash
# scriptPubKey (prev out)
OP_CHECKSIG
<pubKey>

# scriptSig (in)
<sig>
```

注意:  

挖矿产生的奖励只在100个区块后才可以被使用
```c++
/** Coinbase transaction outputs can only be spent after this number of new blocks (network rule) */
static const int COINBASE_MATURITY = 100;
```

通过挖矿奖励获得P2PK的`锁定交易`:

```bash
bg 101

# 查锁定交易
bbasetx 1

# 查询余额
bitcoin-cli getbalance
```

对该比挖矿奖励进行`解锁交易`,引用到该笔交易的地址,并使用私钥进行签名:

```bash
PRE_TXID=`_bbasehash 1`
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
'''
`

# 从钱包中获得第一个区块奖励的私钥
PRE_ADDRESS=`bbasetx 1 | python -c 'import json,sys;obj=json.load(sys.stdin);print(obj["vout"][0]["scriptPubKey"]["addresses"][0])' `
PRE_PRIKEYWIF=`bitcoin-cli dumpprivkey $PRE_ADDRESS`

# 2) 签名交易
SIGNED_RAWTX_JSON=`bitcoin-cli signrawtransactionwithkey $RAWTX '''
[
    "'$PRE_PRIKEYWIF'"
]
'''`

SIGNED_RAWTX=`echo $SIGNED_RAWTX_JSON | python -c 'import json,sys;obj=json.load(sys.stdin);print(obj["hex"])'`

# 3) 发送交易
bitcoin-cli sendrawtransaction $SIGNED_RAWTX

# 4) 生成区块打包区块
bg 1

# 查询新地址信息
echo $NEWADDRESS_INFO

# 导入新地址到钱包
bitcoin-cli importaddress $NEWP2PkHADDR

# 查询新地址接受到的金额
bitcoin-cli getreceivedbyaddress $NEWP2PkHADDR 0

# 查询这一笔交易
bhtx 102 1
```

<a id="markdown-3-pay-to-public-key-hashp2pkh" name="3-pay-to-public-key-hashp2pkh"></a>
# 3. pay to public key hash(P2PKH)

加锁与解锁的堆栈:

```bash
# scriptPubKey (prev out)
OP_CHECKSIG
OP_EQUALVERIFY
<pubkeyHash>
OP_HASH160
OP_DUP

# scriptSig (in)
<pubKey>
<sig>
```

通过挖矿奖励获得P2PKH的`锁定交易`:

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

对该比挖矿奖励进行`解锁交易`,引用到该笔交易的地址,并使用私钥进行签名:

```bash
PRE_TXID=`_bbasehash 1`
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
    "'$COINBASEPRIKEYWIF'"
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
bhtx 102 1
```


<a id="markdown-4-pay-to-script-hash-p2sh" name="4-pay-to-script-hash-p2sh"></a>
# 4. pay to script hash (P2SH)

加锁与解锁的堆栈:

```bash
# scriptPubKey (prev out)
OP_EQUAL
[20-byte-hash of {2 [pubkey1] [pubkey2] [pubkey3] 3 OP_CHECKMULTISIG} ]
OP_HASH160

# scriptSig (in)
{2 [pubkey1] [pubkey2] [pubkey3] 3 OP_CHECKMULTISIG}
[signature2]
[signature1]
0
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

获得P2SH的`锁定交易`, 2-of-3:

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
]'''`

# 脚本地址
MUTISIG_ADDRESS=`echo $MULTISIG_JSON | python -c 'import json,sys;obj=json.load(sys.stdin);print(obj["address"])'`

# 赎回脚本
MUTISIG_REDEEMSCRIPT=`echo $MULTISIG_JSON | python -c 'import json,sys;obj=json.load(sys.stdin);print(obj["redeemScript"])'`

# 2. 向多重签名地址转账
UTXOID=`bitcoin-cli sendtoaddress $MUTISIG_ADDRESS 50.00 "" "" true`

# 查询该比P2SH锁定交易的脚本
RAWTRANSACTION_JSON=`bitcoin-cli getrawtransaction $UTXOID 1`
echo $RAWTRANSACTION_JSON
```

对该比P2SH输出进行`解锁交易`, 用任意的两个私钥进行签名:

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
        "amount": "49.99996220"
    }
]
''' `

# 注意上面可以省略amount, 因为传统的交易不把amount算在签名对象之内 (隔离见证会算在内)

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

<a id="markdown-5-op_return" name="5-op_return"></a>
# 5. OP_RETURN

加锁与解锁的堆栈:

```bash
# scriptPubKey (prev out)
<data2>
<data1>
OP_RETURN

# scriptSig (in)
# 空
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

`解锁资金源`,引用到该比交易的地址,并使用私钥进行签名
```bash

PRE_TXID=`_bbasehash 1`
PRE_VOUT=0

HEX=`bx base16-encode "Get busy living, Or get busy dying"`

# 1) 创建交易
RAWTX=`bitcoin-cli createrawtransaction '''
[
    {
        "txid": "'$PRE_TXID'",
        "vout": '$PRE_VOUT'
    }
]
''' '''
[
    {
        "'$COINBASECP2PKHADDR'": 49.9999
    },
    {
        "data": "'$HEX'"
    }
]
'''
`

# 2) 签名交易
SIGNED_RAWTX_JSON=`bitcoin-cli signrawtransactionwithkey $RAWTX '''
[
    "'$COINBASEPRIKEYWIF'"
]
'''`

SIGNED_RAWTX=`echo $SIGNED_RAWTX_JSON | python -c 'import json,sys;obj=json.load(sys.stdin);print(obj["hex"])'`

# 3)发送交易
bitcoin-cli sendrawtransaction $SIGNED_RAWTX

# 4) 生成区块打包区块
bg 1

# 查询这一笔交易
bhtx 102 1
```

<a id="markdown-6-交易数据" name="6-交易数据"></a>
# 6. 交易数据

* https://raw.githubusercontent.com/yqsy/yqsy.notes/master/source/_posts/business/bitcoin/script/P2PK  (P2Pk)
* https://raw.githubusercontent.com/yqsy/yqsy.notes/master/source/_posts/business/bitcoin/script/P2PKH (P2PKH)
* https://raw.githubusercontent.com/yqsy/yqsy.notes/master/source/_posts/business/bitcoin/script/P2SH (P2SH)
* https://raw.githubusercontent.com/yqsy/yqsy.notes/master/source/_posts/business/bitcoin/script/RETURN (RETURN)


<a id="markdown-7-参考资料" name="7-参考资料"></a>
# 7. 参考资料

* https://en.bitcoin.it/wiki/Transaction (常见交易为P2PKH,P2SH)
* https://bitcoin.org/en/developer-examples (examples)
* https://en.bitcoin.it/wiki/Script (opcode)
* https://siminchen.github.io/bitcoinIDE/build/editor.html (堆栈脚本可视化)
* https://bitcoin-script-debugger.visvirial.com (常见交易种类的调试)
* https://github.com/bitcoin/bitcoin/blob/v0.17.0/doc/descriptors.md (源代码中的交易种类)
* https://bitcoincore.org/en/doc/0.17.0/ (rpc接口说明)
