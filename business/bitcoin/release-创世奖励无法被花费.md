---
title: 创世奖励无法被花费
date: 2018-02-01 13:29:12
categories: [business, bitcoin]
---

<!-- TOC -->

- [1. 说明](#1-说明)
- [2. 参考资料](#2-参考资料)

<!-- /TOC -->

<a id="markdown-1-说明" name="1-说明"></a>
# 1. 说明

中本聪如何证明自己是中本聪?一些观点认为只要有人花费创世奖励的50个比特币,那么就能证明其自己的身份是中本聪.其实这个观点是有欠缺的,因为创世奖励的50个比特币无法被花费.

解析源码中的(未压缩)公钥,得到相应的比特币地址:
```bash
parse_pubkey_uncompressed 04678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb649f6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5f

公钥: 04678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb649f6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5f
公钥hash: 62e907b15cbf27d5425399ebf6f0fb50ebb88f18
P2PKH地址: 1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa
URI: bitcoin:1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa
```

查看交易:  
https://www.blockchain.com/btc/address/1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa

这一笔创世奖励无法被花费的原因是1. 没有加入到交易缓冲池  2. 没有写到leveldb数据库.  在尝试签名交易 (signrawtransactionwithkey) 时会产生寻找不到prevout而签名失败.

通过调试源码发现其关键位置如下:

```c++
// CChainState::ConnectBlock <- CChainState::ConnectTip <- CChainState::ActivateBestChainStep <- CChainState::ActivateBestChain <- ActivateBestChain <- ThreadImport

// Special case for the genesis block, skipping connection of its transactions
// (its coinbase is unspendable)
if (block.GetHash() == chainparams.GetConsensus().hashGenesisBlock) {
    if (!fJustCheck)
        view.SetBestBlock(pindex->GetBlockHash());
    return true;
}

```
<a id="markdown-2-参考资料" name="2-参考资料"></a>
# 2. 参考资料

* https://news.bitcoin.com/people-keep-sending-satoshi-nakamoto-bitcoin/
