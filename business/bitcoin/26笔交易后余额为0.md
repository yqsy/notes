---
title: 26笔交易后余额为0
date: 2018-02-01 13:29:12
categories: [business, bitcoin]
---


<!-- TOC -->

- [1. 说明](#1-说明)
- [2. 连续转账26比余额变零](#2-连续转账26比余额变零)
- [3. 转账25笔打包,再转25笔没有问题](#3-转账25笔打包再转25笔没有问题)
- [4. 通过阅读代码发现](#4-通过阅读代码发现)

<!-- /TOC -->


<a id="markdown-1-说明" name="1-说明"></a>
# 1. 说明

做了一下bitcoin的压力测试,思路是直接sendtoaddress自己地址发自己,把交易池给打满.但是在测试过程中发现,给自己发送超过25笔交易后,交易不但没有被放到交易池,并且余额显示为0.

<a id="markdown-2-连续转账26比余额变零" name="2-连续转账26比余额变零"></a>
# 2. 连续转账26比余额变零

```bash
# 因为没有区块所以没法智能算出手续费用,开启fallbackfee
bitcoind -fallbackfee=0.0002
```

测试: 

```bash
# 准备地址作为挖矿奖励地址,防止余额干扰
COINBASESEED=`bx seed | bx ec-new`
COINBASEINFO=`parse_privkey $COINBASESEED`
COINBASEADDR=`echo $COINBASEINFO | sed -n 13p | awk '{print $2}'`
echo $COINBASEADDR

# 测试花费的地址
TESTSPENDSEED=`bx seed | bx ec-new`
TESTSPENDINFO=`parse_privkey $TESTSPENDSEED`
TESTSPENDPRIVKEYWIF=`echo $TESTSPENDINFO | sed -n 10p | awk '{print $2}'`
TESTSPENDADDR=`echo $TESTSPENDINFO | sed -n 13p | awk '{print $2}'`
echo $TESTSPENDADDR

# 转账到的地址
TMPSEED=`bx seed | bx ec-new`
TMPINFO=`parse_privkey $TMPSEED`
TMPADDR=`echo $TMPINFO | sed -n 13p | awk '{print $2}'`
echo $TMPADDR

# 奖励50个币
bitcoin-cli generatetoaddress 1 $TESTSPENDADDR

# 生成100个区块使得coinbase生效
bitcoin-cli generatetoaddress 100 $COINBASEADDR

# 将测试花费地址导入到地址池中
bitcoin-cli importprivkey $TESTSPENDPRIVKEYWIF

# 查询余额50个币
bitcoin-cli getbalance

# 转25个币
for i in `seq 1 25`; do
bitcoin-cli sendtoaddress $TMPADDR 1.00 "" "" true
done

# 查询余额25个币
bitcoin-cli getbalance

# 再转一笔
TXID=`bitcoin-cli sendtoaddress $TMPADDR 1.00 "" "" true`

# 余额变成0!!!!
bitcoin-cli getbalance

# 查询交易 没有被放到到交易池!
_btxhashdecode $TXID

# 生成一个区块确认 25笔 (第26比没有被放到交易池)
bitcoin-cli generatetoaddress 1 $COINBASEADDR

# 查询第25笔交易, 正常 (25个币的找零)
bhtx 102 25

# 查询第24笔交易
bhtx 102 24


# why???
```

<a id="markdown-3-转账25笔打包再转25笔没有问题" name="3-转账25笔打包再转25笔没有问题"></a>
# 3. 转账25笔打包,再转25笔没有问题

```bash
# 准备地址作为挖矿奖励地址,防止余额干扰
COINBASESEED=`bx seed | bx ec-new`
COINBASEINFO=`parse_privkey $COINBASESEED`
COINBASEADDR=`echo $COINBASEINFO | sed -n 13p | awk '{print $2}'`
echo $COINBASEADDR

# 测试花费的地址
TESTSPENDSEED=`bx seed | bx ec-new`
TESTSPENDINFO=`parse_privkey $TESTSPENDSEED`
TESTSPENDPRIVKEYWIF=`echo $TESTSPENDINFO | sed -n 10p | awk '{print $2}'`
TESTSPENDADDR=`echo $TESTSPENDINFO | sed -n 13p | awk '{print $2}'`
echo $TESTSPENDADDR

# 转账到的地址
TMPSEED=`bx seed | bx ec-new`
TMPINFO=`parse_privkey $TMPSEED`
TMPADDR=`echo $TMPINFO | sed -n 13p | awk '{print $2}'`
echo $TMPADDR


# 奖励50个币
bitcoin-cli generatetoaddress 1 $TESTSPENDADDR

# 生成100个区块使得coinbase生效
bitcoin-cli generatetoaddress 100 $COINBASEADDR

# 将测试花费地址导入到地址池中
bitcoin-cli importprivkey $TESTSPENDPRIVKEYWIF

# 查询余额50个币
bitcoin-cli getbalance

# 转25个币
for i in `seq 1 25`; do
bitcoin-cli sendtoaddress $TMPADDR 1.00 "" "" true
done

# 查询余额25个币
bitcoin-cli getbalance

# 打包25笔交易
bitcoin-cli generatetoaddress 1 $COINBASEADDR

# 查询交易池 没有交易
bitcoin-cli getrawmempool

# 查询余额25个币
bitcoin-cli getbalance

for i in `seq 1 25`; do
bitcoin-cli sendtoaddress $TMPADDR 1.00 "" "" true
done

# 查询交易池
bitcoin-cli getrawmempool

```

<a id="markdown-4-通过阅读代码发现" name="4-通过阅读代码发现"></a>
# 4. 通过阅读代码发现


```bash
# 在同一个区块中,一笔交易被引用为prev out超过25次,则不能继续引用

CTxMemPool::CalculateMemPoolAncestors
AcceptToMemoryPoolWorker
AcceptToMemoryPoolWithTime
AcceptToMemoryPool
CWalletTx::AcceptToMemoryPool
CWallet::CommitTransaction
SendMoney
sendtoaddress
```
