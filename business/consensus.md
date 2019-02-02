---
title: 共识算法
date: 2018-07-09 17:57:25
categories: [business]
---


<!-- TOC -->

- [1. 说明](#1-说明)
    - [1.1. 私有链共识](#11-私有链共识)
    - [1.2. 联盟链共识](#12-联盟链共识)
    - [1.3. 公有链](#13-公有链)
- [2. 继续总结](#2-继续总结)

<!-- /TOC -->


<a id="markdown-1-说明" name="1-说明"></a>
# 1. 说明

* https://blog.csdn.net/lsttoy/article/details/61624287 (csdn的资料)
* https://en.wikipedia.org/wiki/Cryptocurrency (所有机制)
* https://zhuanlan.zhihu.com/p/35847127 (美图的共识算法维度整理)
* https://zhuanlan.zhihu.com/p/38627527 (美图dpos实现)

<a id="markdown-11-私有链共识" name="11-私有链共识"></a>
## 1.1. 私有链共识
paxos:
* https://lamport.azurewebsites.net/pubs/lamport-paxos.pdf (论文)

raft:
* http://thesecretlivesofdata.com/raft/ (动画)
* https://en.wikipedia.org/wiki/Raft_(computer_science)
* https://github.com/coreos/etcd (在etcd中有实现) 
* https://zhuanlan.zhihu.com/p/26506491 (简易实现raft算法)
* https://raft.github.io/raft.pdf (论文)

允许正常节点(N为总数): n >= (N/2) + 1

* 5台机器,错误机器<=2
* 100台机器,错误机器<=49

zab:
* https://github.com/lshmouse/reading-papers/blob/master/distributed-system/Zab:%20High-performance%20broadcast%20for%0Aprimary-backup%20systems.pdf (论文)

<a id="markdown-12-联盟链共识" name="12-联盟链共识"></a>
## 1.2. 联盟链共识

pbft:  
* https://en.wikipedia.org/wiki/Byzantine_fault_tolerance
* http://pmg.csail.mit.edu/papers/osdi99.pdf (论文)

有t个错误节点时,总节点N必须满足: N >= 3t + 1

* 5台机器,错误机器<=1
* 100台机器,错误机器<=33

<a id="markdown-13-公有链" name="13-公有链"></a>
## 1.3. 公有链

pow pos dpos:
* https://bitfury.com/content/downloads/pos-vs-pow-1.0.2.pdf (论文 包括dpos)
* https://www.jianshu.com/p/9a1b165129dd (论文翻译)

<a id="markdown-2-继续总结" name="2-继续总结"></a>
# 2. 继续总结

![](http://on-img.com/chart_image/5b66f7c3e4b025cf4936d7e2.png)


* 私有链: 共识算法为传统`分布式系统强一致性算法`,适用环境是`不考虑`集群中存在`作恶`节点,只考虑`系统/网络故障节点`
* 联盟链: 既考虑`作恶`节点,又要考虑`故障`节点.每个`新`加入的`节点`都是需要`严格验证`和`审核`
* 公有链: 既考虑`作恶`节点,又要考虑`故障`节点.每个`新`加入的`节点`不需要严格验证和审核


主要解决什么问题?:
* double-spend (双花)
* block-chain fork (分叉)

各种解决方法解决一些问题又带来一些问题

pow: 
* spent on eletricity (耗能源)
* slow (速度慢)

pos:
* Nothing at Stake Problem (`账本分叉`): PoS矿工往往会往`两个方向挖` -> dpos
* Initial Distribution Problem(`冷启动`): `早期`获得代币的`持有者`,`没有动力`花费或转移代币给第三方 -> pow 先挖一会

攻击方式|Pow|PoS|DPoS
-|-|-|-
bribe(贿赂攻击)|-|+|-
Long range atack(长距离攻击)|-|+|+
Coin age accumulation attack(币龄加攻击)|-|maybe|-
Precomputing attack(预计算攻击)|-|+|-
Denial of Service(Dos)|+|+|+
Sybil attack(女巫攻击)|+|+|+
Selfish mining(自私挖矿))|maybe|-|-


攻击手段解释:
* Bribe Attack (`贿赂攻击`): 贿赂攻击的成本小于货物或者服务费用，此次攻击就是成功的 -> PoW
* Long-Range Attack (`长距离攻击`): block产生速度快,缺乏算力约束,可以修改历史 -> 限制最大能接受的分叉节点数量
*  Coin Age Accumulation Attack(`币龄加和攻击`): 在最早的 Peercoin 版本中，挖矿难度不仅与当前账户余额有关，也与每个币的持币时间挂钩。这就导致，部分节点在等待足够长时间后，就有能力利用 Age 的增加来控制整个网络，产生非常显著的影响 -> 限制 CoinAge 的最大值
* Precomputing Attack (`预计算攻击`): 当 PoS 中的某一节点占有了一定量的算力后，PoS 中占有特定算力的节点,有能力控制 -> ?
 
