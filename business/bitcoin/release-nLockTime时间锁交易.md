---
title: nLockTime时间锁交易
date: 2018-02-01 13:29:12
categories: [business, bitcoin]
---

<!-- TOC -->

- [1. 说明](#1-说明)
- [2. nLockTime](#2-nlocktime)
- [3. CheckLockTimeVerify常用场景](#3-checklocktimeverify常用场景)
- [4. 场景四 冻结资金实践 (失败的尝试)](#4-场景四-冻结资金实践-失败的尝试)
- [5. 场景四 冻结资金实践 (使用python脚本做签名)](#5-场景四-冻结资金实践-使用python脚本做签名)
- [6. 交易数据](#6-交易数据)
- [7. 参考资料](#7-参考资料)

<!-- /TOC -->


<a id="markdown-1-说明" name="1-说明"></a>
# 1. 说明

```c++
class CTransaction    
int32_t nVersion;
std::vector<CTxIn> vin;
std::vector<CTxOut> vout;
uint32_t nLockTime;
```

设想一种功能: 锁定某一笔钱直到若干年后才能被消费. 这样的功能在传统中心化软件中无法真正做到,因为中心化系统的规则并不是真正的规则.在区块链软件中,规则一旦制定,随着时间的推移其修改的成本会变的越来越高.这里做一下时间锁相关的交易,并跟踪到相关代码来分析.

<a id="markdown-2-nlocktime" name="2-nlocktime"></a>
# 2. nLockTime 

代码:
```bash
# nLockTime在500000000 以内表示高度. 超过表示时间.

# 1. nLockTime 为零时 可上链
# 2. nLockTime 已成为过去式 可上链
# 3. nLockTime 是未来式, 且所有的见证数据的nSequence 为0xffffffff  可上链 (所有的in的nSequence为0xffffffff(表示禁用nLockTime))

IsFinalTx <- ContextualCheckBlock

class CTransaction
const uint32_t nLockTime;
```

通过挖矿奖励得资金源:

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

创建带有nLockTime的`锁定交易`:

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
''' 2000`

# 2) 签名交易
SIGNED_RAWTX_JSON=`bitcoin-cli signrawtransactionwithkey $RAWTX '''
[
    "'$COINBASEPRIKEYWIF'"
]
'''`

SIGNED_RAWTX=`echo $SIGNED_RAWTX_JSON | python -c 'import json,sys;obj=json.load(sys.stdin);print(obj["hex"])'`

# 3)发送交易 (无法被打包, 无法被放入到交易池中)
bitcoin-cli sendrawtransaction $SIGNED_RAWTX

bg 1899

# 2000个区块后,交易可被节点接受
bitcoin-cli sendrawtransaction $SIGNED_RAWTX

bg 1

# 查询交易
bhtx 2001 1
```

<a id="markdown-3-checklocktimeverify常用场景" name="3-checklocktimeverify常用场景"></a>
# 3. CheckLockTimeVerify常用场景

(BIP65, CLTV)

场景一: 第三方托管(Escrow), Alice 和 Bob联合经营业务`(钱在两个人意见一致时才能使用)`,将所有资金锁定在2-of-2的多重交易输出中(必须得到2个人中的2个签名才可以解锁).为了避免其中一个人发生意外问题无法签名,所以任命Lenny作为第三方. Lenny 和任意Alice或Bob其中一人都可解锁交易,`为了避免Alice和Bob在经营业务时间中合谋,`所以用上了时间锁技术,在指定时间(3个月后)律师才可以和其中一人完成签名解锁交易.
```bash
IF
    <now + 3 months> CHECKLOCKTIMEVERIFY DROP
    <Lenny's pubkey> CHECKSIGVERIFY
    1
ELSE
    2
ENDIF
<Alice's pubkey> <Bob's pubkey> 2 CHECKMULTISIG
```

场景二: 双因素钱包 (GreenAddress). 一个密钥用户控制,一个密钥服务控制.在任何情况下,服务商和用户联合签名可以解密,用时间锁技术超过一定时间后用户可自行取钱.`(服务商使用钱必须征得用户的签名同意并且用户在指定时间后可退款)`

```bash
IF
    <service pubkey> CHECKSIGVERIFY
ELSE
    <expiry time> CHECKLOCKTIMEVERIFY DROP
ENDIF
<user pubkey> CHECKSIG
```

场景三: 数据的无信任付款(Trustless Payments for Publishing Data) 数据的买方购买数据`(比如一个珍贵的资料,买家只知道hash,不知道具体的数据)`,可以向指定脚本打币,当发布者出示了数据后可提走钱. 假设发布者迟迟不出示数据,使用时间锁技术使买方可以在指定时间后得到退款.

```bash
IF
    HASH160 <Hash160(encryption key)> EQUALVERIFY
    <publisher pubkey> CHECKSIG
ELSE
    <expiry time> CHECKLOCKTIMEVERIFY DROP
    <buyer pubkey> CHECKSIG
ENDIF
```

场景四: 冻结资金. `没有人能在提供的时间到来之前花费锁定的输出`

```bash
<expiry time> CHECKLOCKTIMEVERIFY DROP DUP HASH160 <pubKeyHash> EQUALVERIFY CHECKSIG

# 或(在锁定脚本中放入公钥,见证脚本中放入签名即可)
<expiry time> CHECKLOCKTIMEVERIFY DROP <pubKey> CHECKSIG
```


代码:
```bash
# EvalScript 

case OP_CHECKLOCKTIMEVERIFY:
# 省略

bool GenericTransactionSignatureChecker<T>::CheckLockTime

# 1. nLockTime 和 脚本锁定时间 必须符合范围规则
# 交易nLockTime < 50 亿 && 脚本锁定时间 < 50亿 (高度)
# 交易nLockTime >= 50亿 && 脚本锁定时间 > 50亿 (时间)

# 2. 必须符合规则: 脚本锁定时间 <= 交易nLockTime (脚本锁定时间是链上已确定,无法修改的,)

# 3. 必须符合规则: 所有见证脚本的nSequence不为0xFFFFFFFF(不能禁用nLockTime)

```

我们来举个例子思考:

```bash

# 如下图, tx1为将币锁定到时间锁脚本上, tx2花费时间锁脚本的币. 

[in out(p2sh) 锁定300块后可被花费]   [in 证明自己已经过了300个区块  out]
          tx1                           tx2

# 问题的核心关键是,如何在tx2中证明自己过了300个区块? 可以使用交易nLockTime! 因为其含义是: nLockTime时间/区块后,交易才可以上链. 如果nLockTime 为300, 并且交易可以通过上链检测. 那么说明此时的区块已经过去了300个.

```

<a id="markdown-4-场景四-冻结资金实践-失败的尝试" name="4-场景四-冻结资金实践-失败的尝试"></a>
# 4. 场景四 冻结资金实践 (失败的尝试)

通过挖矿奖励得资金源:

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


```bash
# 锁定脚本:
<expiry time> CHECKLOCKTIMEVERIFY DROP DUP HASH160 <pubKeyHash> EQUALVERIFY CHECKSIG

# 获得新的地址
NEWEC=`bx seed | bx ec-new`
NEWADDRESS_INFO=`parse_privkey $NEWEC`

# 提取公钥
NEWPUBKEY=`echo $NEWADDRESS_INFO | sed -n 11p | awk '{print $2}'`


# 提取私钥做备用
NEWPRVKEYWIF=`echo $NEWADDRESS_INFO | sed -n 10p | awk '{print $2}'`


# 脚本加锁 至300 区块 (请注意4字节数字需要以小端法输入,但是公钥不需要 参考:ScriptToAsmStr)


REDEEM_SCRIPT=`bx script-encode "[2C010000] checklocktimeverify drop [$NEWPUBKEY] checksig"`

SCRIPT_ADDR=`echo $REDEEM_SCRIPT | bx sha256 | bx ripemd160 | bx base58check-encode --version 5`

# 1. 向脚本转账
UTXOID=`bitcoin-cli sendtoaddress $SCRIPT_ADDR 50.0 "" "" true`

# 2. 生成区块打包交易
bg 1

# 查看锁定交易
bhtx 102 1

UTXO_OUTPUT_SCRIPT=`bhtx 102 1 | python -c 'import json,sys;obj=json.load(sys.stdin);print(obj["vout"][0]["scriptPubKey"]["hex"])'`

```

对该比脚本输出进行`解锁交易`,引用到该笔交易的地址,并使用私钥进行签名

```bash
# 创建新的输出地址
NEWOUTADDR_EC=`bx seed | bx ec-new`
NEWOUTADDR_INFO=`parse_privkey $NEWOUTADDR_EC`
NEWOUTADDR_ADDRESS=`echo $NEWOUTADDR_INFO | sed -n 13p | awk '{print $2}'`

UTXO_VOUT=0

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
    "'$NEWPRVKEYWIF'"
]''' '''
[
    {
        "txid": "'$UTXOID'",
        "vout": '$UTXO_VOUT',
        "scriptPubKey": "'$UTXO_OUTPUT_SCRIPT'",
        "redeemScript": "'$REDEEM_SCRIPT'"
    }
]
''' `

# 这时候我们发现签名会失败,是因为:

# 自定制的交易(P2SH-XXX)的赎回脚本无法使用signrawtransactionwithkey等接口. 因为在signrawtransactionwithkey中只会签名指定的交易格式.函数调用堆栈如下:

# Solver <- SignStep <- ProduceSignature <- SignTransaction <- signrawtransactionwithkey

# 其根本的原因是自定制的脚本对于比特币来说无法识别出应该push到见证脚本内什么数据(比如多个签名+公钥)
```

<a id="markdown-5-场景四-冻结资金实践-使用python脚本做签名" name="5-场景四-冻结资金实践-使用python脚本做签名"></a>
# 5. 场景四 冻结资金实践 (使用python脚本做签名)

加锁与解锁的堆栈:
```bash
# scriptPubKey (prev out)
OP_EQUAL
<20-byte-hash of script>
OP_HASH160

# redeemScript
OP_CHECKSIG
<pubKey>
OP_DROP
OP_CHECKLOCKTIMEVERIFY
<expiry time>

# scriptSig (in)
<sig>
```

得到一笔资金:  
```bash
# [压缩]
# 私钥: f1a80f81857decd896b1c51ede9460e445013ec8386bf8d778c523b60802b12e
# 私钥WIF: L5KTc49MiBTpueR8Ed5etFXRE9ZiZhqrYxudYWru6KetGkVAgzZW
# 公钥: 023908ead084840b8a67307025837548d44e65a59fb528263c263d1fa5e1782a4d
# 公钥hash: fa4d6873e5203075dcf32f8594f67125bf57e9b6
# P2PKH地址: 1PpUfMwTE4sSEsCWko3eUDPjHb98htX9HK
# URI: bitcoin:1PpUfMwTE4sSEsCWko3eUDPjHb98htX9HK
# P2SH-P2WPKH: 32TuMaeEVhdwPhohBrZRcDzmrRmYEs4Px9
# P2WPKH: bc1qlfxksul9yqc8th8n97zefan3ykl406dk52fw62

COINBASECP2PKHADDR=1PpUfMwTE4sSEsCWko3eUDPjHb98htX9HK

bitcoin-cli generatetoaddress 101 $COINBASECP2PKHADDR

# 查询锁定脚本
bbasetx 1

# 提取私钥并导入到钱包
COINBASEPRIKEYWIF=L5KTc49MiBTpueR8Ed5etFXRE9ZiZhqrYxudYWru6KetGkVAgzZW
bitcoin-cli importprivkey $COINBASEPRIKEYWIF

# 查询余额
bitcoin-cli getbalance
```


使用python脚本(可以直接使用命令行)，生成新的锁定交易，到新的地址： 
```bash
# [压缩]
# 私钥: 9e93d1702f131626916f693592fd1cfddfe15b1e88c363c756dfceedecd850c3
# 私钥WIF: L2XxuM4B7GiVFwWhtriLugfWxMAB8AAn63dpygovyczESzBK6p4o
# 公钥: 030c080a2e82c342172d5e8845877e8a576cfd5ce2117e78bb15574a39dd00e58e
# 公钥hash: 600682ebd83c160b24d908752dbe52d1b2413b5c
# P2PKH地址: 19kjfqWzcujpK4SgyuSv6Lk9SfVwrV4hDt
# URI: bitcoin:19kjfqWzcujpK4SgyuSv6Lk9SfVwrV4hDt
# P2SH-P2WPKH: 3Km2LMyYzekRzH9DFComM7M8bqyfwg2bzh
# P2WPKH: bc1qvqrg967c8stqkfxepp6jm0jj6xeyzw6u7kkxc3

# 脚本: 
# [time/block] checklocktimeverify drop [publickey] checksig
# 022c01b17521030c080a2e82c342172d5e8845877e8a576cfd5ce2117e78bb15574a39dd00e58eac

# 地址
SCRIPT_ADDR=33zz8hWy52y2V2dJhVpt2EPWUpqM9ynQUx

UTXOID=`bitcoin-cli sendtoaddress $SCRIPT_ADDR 50.0 "" "" true`

# 打包交易至区块
bg 1

# 打印交易哈希 (动态会变)
echo $UTXOID
```

使用python脚本，把P2SH的币转到其他的地址. (把上面的UTXOID粘贴到,python脚本中(因为会动态变化),来生成新的交易)
```bash
# [压缩]
# 私钥: 28f97e1aabce0cd8c7d166f25c18fa522dfa758ace160592bd93ef9dd38b90b7
# 私钥WIF: KxbMqfhaN8NFXPCmHE4ZupJfBYRDj46iT1YxNqHrJcrpmaKMiL6C
# 公钥: 03aa9f9253b5e8ce3f23bef805e035c9268a1157ba3d52ca0468ca3ebae3a5aea3
# 公钥hash: 4b482b072b3937ae2e987b9ad2194f22d6d9fcdb
# P2PKH地址: 17s48iNQ6ys4CWRvFn6wYT6rExfoJXyxzA
# URI: bitcoin:17s48iNQ6ys4CWRvFn6wYT6rExfoJXyxzA
# P2SH-P2WPKH: 3K9GUYjRznoXBugGj6DxaFcGPdUek1nNMP
# P2WPKH: bc1qfdyzkpet8ym6ut5c0wddyx20yttdnlxmf7sj2w

bg 197

# 无法打包交易,因为nLockTime时间点未到
# bitcoin-cli sendrawtransaction $python脚本打印的交易数据

bg 1

# 成功见证了时间锁锁定
bitcoin-cli sendrawtransaction $python脚本打印的交易数据

bg 1

bhtx 301 1
```

python脚本:

* https://github.com/yqsy/bitcointest/blob/master/cltv_freezefund.py

<a id="markdown-6-交易数据" name="6-交易数据"></a>
# 6. 交易数据

* https://raw.githubusercontent.com/yqsy/yqsy.notes/master/source/_posts/business/bitcoin/script/nLockTime (nLockTime)
* https://raw.githubusercontent.com/yqsy/yqsy.notes/master/source/_posts/business/bitcoin/script/cltv_freezefund  (场景四 冻结资金实践)

<a id="markdown-7-参考资料" name="7-参考资料"></a>
# 7. 参考资料

* https://en.bitcoin.it/wiki/Timelock (百科)
* https://coinb.in/#newTimeLocked (在线生成锁定脚本)
* https://github.com/bitcoin/bips/blob/master/bip-0065.mediawiki (BIP65)

