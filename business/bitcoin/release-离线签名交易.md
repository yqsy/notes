---
title: 离线签名交易
date: 2018-02-01 13:29:12
categories: [business, bitcoin]
---

<!-- TOC -->

- [1. 说明](#1-说明)
- [2. 实践](#2-实践)
- [3. 参考资料](#3-参考资料)

<!-- /TOC -->

<a id="markdown-1-说明" name="1-说明"></a>
# 1. 说明

离线签名的含义是: 花费不在链上的币. 通过前面的文章<数据签名>,我们可以分析出其大概的原理:

![](./pic/p2pkh_sign.png)

交易的签名行为是为了证明用户所公布的交易其所花费的钱是属于用户自己的(比如P2PKH,见证脚本中输入用户的签名和公钥 1. `公钥`和引用输出的公钥哈系对应 2. 公钥解密`签名`得到的hash值与广播的交易hash值相同) 

我们观察上面的两个要素 1. 公钥是用户提供的 2. `签名需要引用输出的hash & n & 锁定脚本...` (P2SH,P2WSH需要赎回脚本---这是由于把锁定脚本延迟到见证时刻展示,只要hash对上即可) / (隔离见证需要amount输出金额)

而当币不在链上时,通过createrawtransaction输入的`txid & vout`信息无法得知到`锁定脚本`. 所以需要在签名signrawtransactionwithkey输入额外的锁定信息. 并且当同步交易至链上时需要先输入前面的交易,才能使得后面的交易能够被正常处理.

据上面的推理,我们看到rpc接口的说明,正是符合我们的猜想:
```bash
# signrawtransactionwithkey
* txid
* vout
* scriptPubKey (必须用到,生成交易hash并签名时用)
* redeemScript (P2SH,P2WSH)才需要用到,放到见证脚本内
* amount  (隔离见证用)
```

<a id="markdown-2-实践" name="2-实践"></a>
# 2. 实践

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

将区块1的奖励输出到新的P2PKH地址:

```bash
PRE_TXID=`_bbasehash 1`
PRE_VOUT=0

# 获得新的地址
NEWEC=`bx seed | bx ec-new`
NEWADDRESS_INFO=`parse_privkey $NEWEC`

# 提取私钥备用
NEWADDRESS_PRIKEYWIF=`echo $NEWADDRESS_INFO | sed -n 10p | awk '{print $2}'`

# 提取P2PKH地址
NEWP2PkHADDR=`echo $NEWADDRESS_INFO | sed -n 13p | awk '{print $2}'`

# 1) 创建交易
PRE_RAWTX=`bitcoin-cli createrawtransaction '''
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
PRE_SIGNED_RAWTX_JSON=`bitcoin-cli signrawtransactionwithkey $PRE_RAWTX '''
[
    "'$COINBASEPRIKEYWIF'"
]
'''`

PRE_SIGNED_RAWTX=`echo $PRE_SIGNED_RAWTX_JSON | python -c 'import json,sys;obj=json.load(sys.stdin);print(obj["hex"])'`
```

当这一笔交易没有上链时,我们尝试引用该比交易:

```bash

# 创建新的输出地址
NEWOUTADDR_EC=`bx seed | bx ec-new`
NEWOUTADDR_INFO=`parse_privkey $NEWOUTADDR_EC`
NEWOUTADDR_ADDRESS=`echo $NEWOUTADDR_INFO | sed -n 13p | awk '{print $2}'`

UTXOID=`bitcoin-cli decoderawtransaction $PRE_SIGNED_RAWTX | python -c 'import json,sys;obj=json.load(sys.stdin);print(obj["txid"])'`
UTXO_VOUT=0
UTXO_OUTPUT_SCRIPT=`bitcoin-cli decoderawtransaction $PRE_SIGNED_RAWTX | python -c 'import json,sys;obj=json.load(sys.stdin);print(obj["vout"][0]["scriptPubKey"]["hex"])'`

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
    "'$NEWOUTADDR_ADDRESS'": 49.9998
}
'''`

# 2. 签名交易
SIGNED_RAWTX_JSON=`bitcoin-cli signrawtransactionwithkey $RAWTX '''
[
    "'$NEWADDRESS_PRIKEYWIF'"
]''' '''
[
    {
        "txid": "'$UTXOID'",
        "vout": '$UTXO_VOUT',
        "scriptPubKey": "'$UTXO_OUTPUT_SCRIPT'"
    }
]
''' `

SIGNED_RAWTX=`echo $SIGNED_RAWTX_JSON | python -c 'import json,sys;obj=json.load(sys.stdin);print(obj["hex"])'`

#  发送交易会失败
# 提示: Missing inputs
# bitcoin-cli sendrawtransaction $SIGNED_RAWTX

# 发送前置交易
bitcoin-cli sendrawtransaction $PRE_SIGNED_RAWTX

# 发送当前交易
bitcoin-cli sendrawtransaction $SIGNED_RAWTX

# 查看内存池的两笔交易
bitcoin-cli getrawmempool

# 生成打包区块
bg 1

# 查看这两比交易
bhtx 102 1
bhtx 102 2
```

<a id="markdown-3-参考资料" name="3-参考资料"></a>
# 3. 参考资料

* https://bitcoin.org/en/developer-examples#offline-signing
