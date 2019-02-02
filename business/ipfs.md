---
title: ipfs
date: 2018-07-13 13:11:45
categories: [business]
---


<!-- TOC -->

- [1. 说明](#1-说明)
- [2. 自己的梳理](#2-自己的梳理)
- [3. filecoin](#3-filecoin)
- [4. 实践](#4-实践)
- [5. 常用指令](#5-常用指令)

<!-- /TOC -->

<a id="markdown-1-说明" name="1-说明"></a>
# 1. 说明

* http://www.btcjiucai.com/jiucai/1839.html (要给去中心化存储打上问号)


--- 

* http://ipfser.org/2018/06/27/r45/ (书)
* https://github.com/ipfs/ipfs (官方文档)
* https://ipfs.io/docs/examples/ (常用场景,看完了)
* https://github.com/ipfs/specs (协议)
* https://github.com/ipfs/reading-list (阅读列表)
* https://github.com/filecoin-project (file-coin源码)
* https://explore.ipld.io (这个超帅的!!!)
* https://www.youtube.com/watch?v=h73bd9b5pPA (indeep-turtoial)

---

ipld:
* https://ipld.io/
* https://github.com/ipld/ipld 

---

私人网络:

* https://blog.csdn.net/oscube/article/details/80598790
* https://github.com/ipfs/go-ipfs/blob/master/docs/experimental-features.md#private-networks

---
论文:
* https://ipfs.io/ipfs/QmR7GSQM93Cx5eAg6a6yRzNde1FQv7uL6X1o4k7zrJa3LX/ipfs.draft3.pdf
* http://www.docin.com/p-2121715857.html (论文的翻译)
* https://filecoin.io/filecoin.pdf

---
应用:  
* https://d.tube


![](http://ouxarji35.bkt.clouddn.com/QQ%E5%9B%BE%E7%89%8720180725093735.png)

![](http://ouxarji35.bkt.clouddn.com/QQ%E6%88%AA%E5%9B%BE20180725094636.png)


<a id="markdown-2-自己的梳理" name="2-自己的梳理"></a>
# 2. 自己的梳理

* Identities 身份层, `S/Kademlia DHT网络,` 由Kademlia发展而来,做出两点提升 1. 防止Sybill attacks 2. 容错15%
* Network 网络层, 使用WebRTC,uTP,`ICE NAT`,checksum,HMAC等技术保证可传输,可靠性,连通性,完整性,真实性
* Routing 路由层, 基于1. S/Kademlia 2. Coral DSHT 的 `DSHT` (distributed sloppy hash table)
* Block Exchange 块交换层, 升级于BitTorrent的`BitSwap`协议, 独特的信用体系,防止吸血鬼攻击
* Objects 对象层,  使用`Merkle DAG `数据结构 1. 按内容hash寻址 2.防止篡改 3. 去重复
* Files 文件层, 参照`GIT`的设计, 将底层存储分为 1. block 2. list 3. tree 4. commit . 实现版本的快照/管理
* Naming 命名层, 使用hash来定位一切文件,文件永远存在

---

* Incentive 激励层, 基于 `proof-of-storage` 和 `proof-of-replication`的`去中心化存储算法市场`

1. 客户端支付费用存储和检索数据
2. 矿工提供存储/检索服务

<a id="markdown-3-filecoin" name="3-filecoin"></a>
# 3. filecoin


* 女巫攻击 (Sybil Attacks): 利用n个身份，承诺存储n份数据D，`而实际上存储小于n份`（比如1份），但是`却提供了n份存储证明`，攻击成功
* 外部数据源攻击 (Outsourcing Attacks): 攻击者矿工收到检验者要求提供数据D的证明的时候，`攻击者矿工从别的矿工那里生成证明`，证明自己一直存储了数据D，而实际上没有存储，攻击成功
* 生成攻击 (Generation Attacks):  `攻击者A可以使用某种方式生成数据D`，当检验者验证的时候，攻击者A就可以重新生成数据D来完成存储证明，攻击成功

其他共识?

* 数据持有性证明(Provable Data Possession,PDP): 用户发送数据给矿工进行存储,矿工`证明数据已经被自己存储`,用户重复检查矿工是否还在存储自己的数据
* 可检索证明(Proof-of-Retrievablity,PoRet): 和PDP过程比较类似,证明矿工存储的数据是可以用来查询的

---
* 存储证明(Proof-of-Storage,PoS): 利用存储空间进行的证明,工作量证明的一种,FileCoin上一篇论文一直使用这个名字,`新的论文则升级为PoRep`
* 复制证明(Proof-of-Replication,`PoRep`): 新的PoS(Proof-of-storage),`PoRep可以保证每份数据都是独立的`.可以防止女巫攻击,外源攻击和生成攻击
* 时空证明(Proof-of-Spacetime,`PoSt`): 证明自己花费了spacetime的资源,`一定时间内的存储使用`,`PoSt是基于PoRep实现的`

---
* 工作量证明(Proof-of-Work,`PoW`): 证明者向校验者证明自己花费了一定的资源.
* 空间证明(Proof-of-Space,PoSpace): `PoSpace是PoW的一种`,不同的是PoW是用的是`计算的资源`,而PoSpace使用的是`存储的资源`




<a id="markdown-4-实践" name="4-实践"></a>
# 4. 实践

安装ipfs

```bash
go get -u -d github.com/ipfs/go-ipfs
cd $GOPATH/src/github.com/ipfs/go-ipfs

# 这个通过ipfs网络下载不到? 被墙了(因为官网被墙了)?
make install

cd /mnt/disk1/linux/installpack
wget https://dist.ipfs.io/go-ipfs/v0.4.16/go-ipfs_v0.4.16_linux-amd64.tar.gz
tar -xvzf go-ipfs_v0.4.16_linux-amd64.tar.gz
cd go-ipfs
sudo cp ipfs /usr/bin

# 创建默认的配置文件
ipfs init   

# 查看readme
ipfs cat /ipfs/QmS4ustL54uo8FzR9455qaxZwuMiUhyvMcX9Ba8nUH4uVv/readme

```



基础实践
```bash
# 初始化全局配置
ipfs init 

# 上传当前整个目录
ipfs add -r .

# 使用ipfs cat打印
ipfs cat /ipfs/QmeV1kwh3333bsnT6YRfdCRrSgUPngKmAhhTa4RrqYPbKT

# 连接到互联网
ipfs daemon

# 查看peers
ipfs swarm peers

# 本地inspector:
http://127.0.0.1:5001/webui

# 本地直接的浏览
http://127.0.0.1:8080/ipfs/QmeV1kwh3333bsnT6YRfdCRrSgUPngKmAhhTa4RrqYPbKT

#　如果开启了daemon 那么会传输到星际网络
https://gateway.ipfs.io/ipfs/QmeV1kwh3333bsnT6YRfdCRrSgUPngKmAhhTa4RrqYPbKT

# 这个也可以吗?
https://ipfs.io/ipfs/QmeV1kwh3333bsnT6YRfdCRrSgUPngKmAhhTa4RrqYPbKT

# 查看文件分片
ipfs ls QmQn14QTMctBUp8GVhSamP1cz1NbnsqfcGm9nJWzqQV47u

# 直接创建分片
echo "This is some data" | ipfs block put

# 获取分片
ipfs block get QmfQ5QAjvg4GtA3wg3adpnDJug8ktA1BxurVqBD8rtgVjM

# 主动连接 swarm
ipfs swarm connect /ip4/104.236.176.52/tcp/4001/ipfs/QmSoLnSGccFuZQJzRadHn95W2CrSFmZuTdDWP8HXaHca9z

# 寻找peer
ipfs dht findpeer QmSoLnSGccFuZQJzRadHn95W2CrSFmZuTdDWP8HXaHca9z

# 防止gc
ipfs pin


# 本地映射
sudo mkdir /ipfs /ipns
sudo chown `whoami` /ipfs /ipns

ipfs mount

```

ipns 名字空间!!!!
```bash
echo 'Let us have some mutable fun!' | ipfs add

# 发布
ipfs name publish QmYuWGLtu2fwTBMyt9LWJw212PBdMm2uDchub4rHqkHPg3

# 解析自己的(hash是自己的node id)
ipfs name resolve QmRxvVhBA9p1CTamqzyfPbqS4QsdnihYaMnm6sLY2utW6D

# 为何不是目录树,而直接是文本呢?
https://ipfs.io/ipns/QmRxvVhBA9p1CTamqzyfPbqS4QsdnihYaMnm6sLY2utW6D

echo 'Look! Things have changed!' | ipfs add

# 绑定节点名(绑定到自己的!)
# 主要解决问题是每次修改文件后add都会返回不同的hash,对于网站来说没法访问
ipfs name publish QmSb8DSVmu4Qip56jcqPVz1Cx9RJ3vTf3d1Gf9ixaG2tWg

```

bootstrap(初始化引导列表把)
```
ipfs bootstrap list
```

ipfs 配置
```
"Addresses": {
    "Swarm": [  
      "/ip4/0.0.0.0/tcp/4001" # 公网地址给别人dial的
    ],
    "API": "/ip4/127.0.0.1/tcp/5001", # 提供http API,操控daemon,本机用
    "Gateway": "/ip4/127.0.0.1/tcp/8080" # 网关地址,本机用
  }
```

Graphing Objects 画图哦
```
yq@yq-PC:~/resource/test% tree shit
shit
├── cat.jpg
└── test
    ├── bar
    ├── baz
    │   ├── b
    │   └── f
    └── foo

graphmd Qma2m3f9w345iMWX32ormPsNwq8PWa5Pmm94N9WiErMqHY | dot -Tpng > graph.png

```

git more distributed

```bash
git clone --bare https://github.com/yqsy/testipfs

# 往ipfs上扔的时候
git update-server-info

# 可选
cp objects/pack/*.pack .
git unpack-objects < ./*.pack
rm ./*.pack

ipfs add -r .


git clone http://127.0.0.1:8080/ipfs/QmaUufWKhav51hZHT9BMHSVGwTg4ksiSwKXd8cPH9D8sXP myrepo

# 直接可以这样用
import (
    mylib "gateway.ipfs.io/ipfs/QmX679gmfyaRkKMvPA4WGNWXj9PtpvKWGPgtXaF18etC95"
)

```

websites

```bash
mkdir testhtml
cd testhtml
echo "<h> hello world</h>" > index.html
ipfs add -r .

# 访问
http://127.0.0.1:8080/ipfs/QmZfycqAQViYGJ4eH2e63cgAD7J57VRcPeD3NkHfkxdbT8/
```


<a id="markdown-5-常用指令" name="5-常用指令"></a>
# 5. 常用指令

```bash
# 连接的peer
ipfs swarm peers

# 展示所有的bootstrap
ipfs bootstrap list

# 恢复
ipfs bootstrap rm --all
ipfs bootstrap add --default

# 增加
ipfs bootstrap add /ip4/192.168.0.248/tcp/4001/ipfs/QmcAQMcAdw1jzkRyScLqWQK9fXiSjkVh9uYHHki76vvahm

```
