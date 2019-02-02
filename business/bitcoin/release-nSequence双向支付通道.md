---
title: nSequence双向支付通道
date: 2018-02-01 13:29:12
categories: [business, bitcoin]
---

<!-- TOC -->

- [1. 说明](#1-说明)
    - [1.1. 再提一下单向支付通道](#11-再提一下单向支付通道)
    - [1.2. 双向支付通道](#12-双向支付通道)
- [2. 实践](#2-实践)
- [3. 参考资料](#3-参考资料)

<!-- /TOC -->


<a id="markdown-1-说明" name="1-说明"></a>
# 1. 说明

<a id="markdown-11-再提一下单向支付通道" name="11-再提一下单向支付通道"></a>
## 1.1. 再提一下单向支付通道

在讲述nSequence双向支付通道之前. 让我们再来思考一下基于nLockTime的单向支付通道.

一般分为两种:

(1). <精通比特币书的案例,不需要用到OP_CHECKLOCKTIMEVERIFY

用户将钱打到P2SH 2-2的多重签名脚本,可以称之为押金 如下图:

```bash
[in out]  [in out]

  用户         用户 & 商家多重签名

# scriptPubKey (prev out)
OP_EQUAL
[20-byte-hash of {2 [pubkey1] [pubkey2] 2 OP_CHECKMULTISIG} ]
OP_HASH160

# scriptSig (in)
{2 [pubkey1] [pubkey2] 2 OP_CHECKMULTISIG}
[signature2]
[signature1]
0
```

用户使用nLockTime生成退款的交易,让商家来签名(因为是多重签名锁定),并把签名好的交易留在自己的手中,这是在超时赎回资金的方法.

有了退款交易之后,用户可以放心的将这笔押金交易打到链上.然后用户分阶段签名小额交易,往商家方向输出.比如抵押了300个币,阶段一:商家1,用户299,阶段二:商家2,用户298... 这个过程中,用户是无法作恶的,因为交易是用户自己发起的,只有单独签名的用户无法广播交易. 而商家也是没有作恶的动机的,因为状态是单向演变的,会逐渐对商家有利,商家只需要将最终的状态,也就是对商家最有利的状态同步到链上即可.

(2). 利用OP_CHECKLOCKTIMEVERIFY

利用OP_CHECKLOCKTIMEVERIFY可以简化退款逻辑,用户直接将币打到可退款的多重签名脚本中

```bash
IF
    <service pubkey> CHECKSIGVERIFY
ELSE
    <expiry time> CHECKLOCKTIMEVERIFY DROP
ENDIF
<user pubkey> CHECKSIG
```

这两种绝对时间锁实现单一支付通道的缺点即是支付通道打开后,如果商家跑路,不履行商家的义务,那么用户必须等待了超时时间结束才能够领取币.

<a id="markdown-12-双向支付通道" name="12-双向支付通道"></a>
## 1.2. 双向支付通道

什么是双向支付?交易的状态不是单方向逐渐变得越来越有利. 上述的例子中,商家会从所有的交易中寻找到一个最有利的交易广播到链上做结算,而这最有利的交易也正是用户最后发起的交易.但是双向支付的特点是,用户A 和 用户B之间架起双向支付通道后,用户A可以向用户B输出,用户B可以向用户A输出.状态的结果可以是对用户A有利,也可以是对用户B有利. 那么如何防止对方作恶,用已经撤销但是对对方有利的交易同步到链上?

利用相对时间锁+非对称可撤销密钥可以解决这个问题.

我们拿`Revocable Sequence Maturity Contracts`的案例做一下分析:

向Bob支付的交易:
```bash
 OP_IF 
    144 OP_CECKSEQUENCEVERIFY
    OP_HASH160 <Bob's key>  OP_EQUALVERIFY OP_CHECKSIG 
 OP_ELSE 
    2 <Alice's secret revocation key><Bob's secret revocation key> 2 OP_CHECKMULTISIGVERIFY 
 OP_ENDIF
```

向Alice支付的交易:
```bash
 OP_IF 
    144 OP_CECKSEQUENCEVERIFY
    OP_HASH160 <Alice's key>  OP_EQUALVERIFY OP_CHECKSIG 
 OP_ELSE 
    2 <Alice's secret revocation key><Bob's secret revocation key> 2 OP_CHECKMULTISIGVERIFY 
 OP_ENDIF
```

通道打开:  
Alice 和 Bob各自打5个币,一共10个币到2-2多重签名脚本中:

链下交易一,Alice打2个币给对方:  
Alice生成交易: Alice:3,Bob:7.  Alice有单独签名的交易,Bob有完整签名的交易,Bob是受益方

链下交易二,Bob打5个币给对方:  
Bob生成交易: Alice:8,Bob:2.  Bob有单独签名的交易,Alice有完整签名的交易,Alice是受益方

我们思考一下,在生成链下交易二时对于Alice有什么风险? 链下交易一还是有效的! 对于Bob来说Bob可以将这笔交易同步到链上,使的Alice受到损失. 那么在进行链下交易二之前,Bob必须将赎回密钥给到Alice,使得Alice可以在Bob作恶时,有24个小时的时间可以使用赎回密钥解锁资金.

通道关闭:  
Alice将链下交易二同步到链上.将p2sh 2-2的脚本的钱变成新的状态.

<a id="markdown-2-实践" name="2-实践"></a>
# 2. 实践

TODO

<a id="markdown-3-参考资料" name="3-参考资料"></a>
# 3. 参考资料

* https://github.com/bitcoinbook/bitcoinbook/blob/develop/ch12.asciidoc 
* https://en.wikiversity.org/wiki/Revocable_Sequence_Maturity_Contracts (RSMC)
