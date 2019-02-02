---
title: pow
date: 2018-01-02 14:15:28
categories: [math]
---

<!-- TOC -->

- [1. 基础](#1-基础)
- [2. cuckoo cycle](#2-cuckoo-cycle)
- [3. sha256](#3-sha256)

<!-- /TOC -->

<a id="markdown-1-基础" name="1-基础"></a>
# 1. 基础

* https://www.zhihu.com/question/26762707/answer/40119521

> 将任意长度的数据映射到有限的长度的域上.

注重的能力:
* 抗碰撞能力:对于任意两个不同的数据块,其hash值相同的可能性极小; 对于一个给定的数据块，找到和它hash值相同的数据块极为困难.
* 抗篡改能力:对于一个数据块，哪怕只是改动其中一个比特位，其hash值的改动也会非常大.

作用:
* 哈希桶数据结构
* 消息摘要,签名 (完整性校验)


<a id="markdown-2-cuckoo-cycle" name="2-cuckoo-cycle"></a>
# 2. cuckoo cycle
* https://github.com/tromp/cuckoo (源码)
* https://bc-2.jp/cuckoo-profile.pdf (评测)
* https://en.wikipedia.org/wiki/Cuckoo_hashing (维基百科)
* http://grin-tech.org/ (grin rust)
* http://www.aeternity.com/ (ae erlang)
* https://github.com/bitcoin/bips/blob/master/bip-0154.mediawiki (bitcoin的提案)


<a id="markdown-3-sha256" name="3-sha256"></a>
# 3. sha256 

* https://zh.wikipedia.org/wiki/SHA-2
* https://github.com/okdshin/PicoSHA2/blob/master/picosha2.h (源码)
* https://www.cnblogs.com/foxclever/p/8370712.html (虽然写的不是很好,但是入门学习下也好)

