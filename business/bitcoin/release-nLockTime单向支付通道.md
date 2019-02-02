---
title: nLockTime单向支付通道
date: 2018-02-01 13:29:12
categories: [business, bitcoin]
---

<!-- TOC -->

- [1. 说明](#1-说明)
- [2. 实践](#2-实践)
    - [2.1. 场景一:用户在时间到后花费](#21-场景一用户在时间到后花费)
    - [2.2. 场景二:用户和商家同时签名花费](#22-场景二用户和商家同时签名花费)
    - [2.3. 场景三:链下交易,链上结算](#23-场景三链下交易链上结算)
- [3. 缺陷](#3-缺陷)
- [4. 交易数据](#4-交易数据)
- [5. 参考资料](#5-参考资料)

<!-- /TOC -->

<a id="markdown-1-说明" name="1-说明"></a>
# 1. 说明

设想一种支付方式: 用户把钱抵押给商家时,1. 商家可以看到钱但是不可以私自挪动钱,商家想要花费任意一点钱都需要征得用户的同意.  2. 用户在指定时间后可以退款.  

让我们来思考一下使用比特币的脚本如何实现这个逻辑(可以参考`<nLockTime时间锁交易>`的场景二双因素钱包 (GreenAddress)):

```bash
IF
    <service pubkey> CHECKSIGVERIFY
ELSE
    <expiry time> CHECKLOCKTIMEVERIFY DROP
ENDIF
<user pubkey> CHECKSIG
```

<a id="markdown-2-实践" name="2-实践"></a>
# 2. 实践

* https://github.com/yqsy/bitcointest/blob/master/cltv_singlepayment.py

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
# 用户的私钥信息:
# [压缩]
# 私钥: 9e93d1702f131626916f693592fd1cfddfe15b1e88c363c756dfceedecd850c3
# 私钥WIF: L2XxuM4B7GiVFwWhtriLugfWxMAB8AAn63dpygovyczESzBK6p4o
# 公钥: 030c080a2e82c342172d5e8845877e8a576cfd5ce2117e78bb15574a39dd00e58e
# 公钥hash: 600682ebd83c160b24d908752dbe52d1b2413b5c
# P2PKH地址: 19kjfqWzcujpK4SgyuSv6Lk9SfVwrV4hDt
# URI: bitcoin:19kjfqWzcujpK4SgyuSv6Lk9SfVwrV4hDt
# P2SH-P2WPKH: 3Km2LMyYzekRzH9DFComM7M8bqyfwg2bzh
# P2WPKH: bc1qvqrg967c8stqkfxepp6jm0jj6xeyzw6u7kkxc3

# 商家的私钥信息:
# [压缩]
# 私钥: 28f97e1aabce0cd8c7d166f25c18fa522dfa758ace160592bd93ef9dd38b90b7
# 私钥WIF: KxbMqfhaN8NFXPCmHE4ZupJfBYRDj46iT1YxNqHrJcrpmaKMiL6C
# 公钥: 03aa9f9253b5e8ce3f23bef805e035c9268a1157ba3d52ca0468ca3ebae3a5aea3
# 公钥hash: 4b482b072b3937ae2e987b9ad2194f22d6d9fcdb
# P2PKH地址: 17s48iNQ6ys4CWRvFn6wYT6rExfoJXyxzA
# URI: bitcoin:17s48iNQ6ys4CWRvFn6wYT6rExfoJXyxzA
# P2SH-P2WPKH: 3K9GUYjRznoXBugGj6DxaFcGPdUek1nNMP
# P2WPKH: bc1qfdyzkpet8ym6ut5c0wddyx20yttdnlxmf7sj2w

# 脚本:
# if [03aa9f9253b5e8ce3f23bef805e035c9268a1157ba3d52ca0468ca3ebae3a5aea3] checksigverify else [2c01] checklocktimeverify drop endif [030c080a2e82c342172d5e8845877e8a576cfd5ce2117e78bb15574a39dd00e58e] checksig

# 地址
SCRIPT_ADDR=39QGYRrmYXM3pLD6xAEoQiyiA1Gd4uZ2j1

UTXOID=`bitcoin-cli sendtoaddress $SCRIPT_ADDR 50.0 "" "" true`

# 打包交易至区块
bg 1

# 打印交易哈希 (动态会变)
echo $UTXOID

# 查看交易
bhtx 102 1
```

<a id="markdown-21-场景一用户在时间到后花费" name="21-场景一用户在时间到后花费"></a>
## 2.1. 场景一:用户在时间到后花费

请注意,这是其中一个场景,执行完后删除数据,再去执行其他场景
```bash
# scriptPubKey (prev out)
OP_EQUAL
<20-byte-hash of script>
OP_HASH160

# redeemScript

OP_CHECKSIG
<userPubkey>           <- 
OP_ENDIF
OP_DROP
OP_CHECKLOCKTIMEVERIFY <- 
<expiry time>
OP_ELSE
OP_CHECKSIGVERIFY
<servicePubkey>
OP_IF

# scriptSig (in)

0 # false, 走时间的判断
<sig>
```

使用python脚本，把P2SH的币转到其他的地址. (把上面的UTXOID粘贴到,python脚本中(因为会动态变化),来生成新的交易)
```bash
bg 198

# 用户成功在时间到之后将P2SH的资金退款到自己的账户
bitcoin-cli sendrawtransaction $python脚本打印的交易数据

bg 1

bhtx 301 1
```

<a id="markdown-22-场景二用户和商家同时签名花费" name="22-场景二用户和商家同时签名花费"></a>
## 2.2. 场景二:用户和商家同时签名花费

请注意,这是其中一个场景,执行完后删除数据,再去执行其他场景

```bash
# scriptPubKey (prev out)
OP_EQUAL
<20-byte-hash of script>
OP_HASH160

# redeemScript

OP_CHECKSIG
<userPubkey>            <-  
OP_ENDIF
OP_DROP
OP_CHECKLOCKTIMEVERIFY 
<expiry time>
OP_ELSE
OP_CHECKSIGVERIFY  
<servicePubkey>         <- 
OP_IF

# scriptSig (in)
1  # true, 走商家公钥的判断
<service's sig>
<user's sig>
```

使用python脚本，把P2SH的币转到其他的地址. (把上面的UTXOID粘贴到,python脚本中(因为会动态变化),来生成新的交易)

```bash
# 用户和商家同时签名解锁交易,资金打到商家的账户里
bitcoin-cli sendrawtransaction $python脚本打印的交易数据

bg 1

bhtx 103 1
```

<a id="markdown-23-场景三链下交易链上结算" name="23-场景三链下交易链上结算"></a>
## 2.3. 场景三:链下交易,链上结算

我们按照<精通比特币>书中的简单支付通道示例的案例,来做一个关于`共享单车`的实践,用户将`存款`打到用户与商家多重签名的p2sh脚本内. 

链下交易:

* 用户使用车: 用户签名了给商家指定时间租凭费用的交易,并连同交易和签名发送给商家. 商家认证签名符合用户公钥,给车的使用权. 

链上结算:

* 用户取回退款: 在没有发生任何交易的情况下,用户凭借时间条件以及签名可从p2sh拿走退还资金 
* 商家取得自己的利益: 商家拿用户最近的交易,并签名,然后同步到链上

作恶手段:

* 作恶只存在于用户方,用户可以拿旧的交易在商家同步之前,同步到链上. (发生一笔交易p2sh内的资金会全部转移走,商家只能拿着最终交易状态眼睁睁的看着用户白骑车)

作恶手段的解决方法:

* 越早的交易设置时间锁越晚(越晚能同步到链上),商家在用户可作恶时间点之前将最终交易状态同步到链上

其实这个作恶手段可以规避:

* 因为交易是由用户发起的,用户签名了之后把交易和签名给商家,商家可以不把商家签名了的交易给用户的.基于这个前提之下,用户是无法作恶的.

```bash
# p2sh 脚本上已有50个币的抵押资金. 假设用户要骑10次,每次骑1个币的费用. 也就是链下交易10次,最终商家链上同步 

# 因为我们的p2sh锁定时间为300区块,所以我们可以将第一次交易的结算时间设置为300,第二次为299...(结算时间点超过300没有意义,因为用户可以通过时间和自己的签名取回p2sh锁定的钱),最后的交易可以获得最先上链的资格,商家应实时关注锁定时间的到来,将最有利的状态最终结算到链上


bg 189

# 商家结算最后一笔交易
# 资金打到商家的账户里,找零打到用户的账户里
bitcoin-cli sendrawtransaction $python脚本打印的交易数据

bg 1

bhtx 292 1
```

<a id="markdown-3-缺陷" name="3-缺陷"></a>
# 3. 缺陷

* 在通道首次打开时建立最大时间锁,限制了通道使用的寿命. 如果商家退出(不签名),那么用户只能等到到锁定时间后才能得到退款.
* 因为通道寿命的有限,双方承诺交易数量也是有限的.商家必须时刻保持警惕,发送正确承诺的交易,防止用户有作恶的可能. (可以规避)

<a id="markdown-4-交易数据" name="4-交易数据"></a>
# 4. 交易数据

* https://raw.githubusercontent.com/yqsy/yqsy.notes/master/source/_posts/business/bitcoin/script/cltv_singlepayment1 (场景一 - 用户在时间到后花费)
* https://raw.githubusercontent.com/yqsy/yqsy.notes/master/source/_posts/business/bitcoin/script/cltv_singlepayment2 (场景二 - 用户和商家同时签名花费)
* https://raw.githubusercontent.com/yqsy/yqsy.notes/master/source/_posts/business/bitcoin/script/cltv_singlepayment3 (场景三 - 链下交易,链上结算)

<a id="markdown-5-参考资料" name="5-参考资料"></a>
# 5. 参考资料

* https://github.com/petertodd/checklocktimeverify-demos (BIP65 demo - python 单向支付通道)
* https://github.com/mruddy/bip65-demos (BIP65 demo - nodejs)
* https://github.com/bitcoinbook/bitcoinbook/blob/develop/ch12.asciidoc (精通比特币,应用章节-简单支付通道示例)
