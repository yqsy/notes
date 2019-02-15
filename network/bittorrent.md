


<!-- TOC -->

- [1. 说明](#1-说明)
- [2. torrent实践](#2-torrent实践)
- [3.3. bittorrent](#33-bittorrent)

<!-- /TOC -->

<a id="markdown-1-说明" name="1-说明"></a>
# 1. 说明

* https://zh.wikipedia.org/wiki/BitTorrent_(%E5%8D%8F%E8%AE%AE) (wiki)
* https://www.bittorrent.com/ (官网)
* https://zh.wikipedia.org/wiki/Kademlia 
* https://github.com/ipfs/go-ipfs/tree/master/exchange/bitswap (ipfs的改进)

---

* https://stackoverflow.com/questions/19749085/calculating-the-info-hash-of-a-torrent-file (如何解析infohash)
* https://github.com/transmission/transmission (命令行工具)
* https://github.com/webtorrent/parse-torrent (nodejs解析torrent文件)

---
源码:
* https://github.com/shiyanhui/dht (这个能跑,但我觉得写的很烂)
* https://github.com/fanpei91/p2pspider (也是嗅探)
* https://github.com/anacrolix/torrent (Full-featured )

2001年4余额时发布,在2001年7月2日首次正式应用


根据BitTorrent协议,文件发布者会根据要发布的文件生成通过一个.torrent文件,包含  
* Tracker信息,Tracker服务器的地址和针对Tracker服务器的设置
* 文件信息,根据对目标文件的计算生成的,结果根据`Bencode`规则进行编码,把提供下载的文件虚拟分成`大小相等的块`,块大小必须为`2k的整数次方`,并把每个块的`索引信息`和`Hash`验证码写入种子文件中.种子文件就是被下载文件的索引

下载流程:  
BT客户端首先解析种子文件得到`Tracker地址`,然后连接Tracker服务器.`Tracker服务器`回应下载者的请求,提供下载者`其他下载者的IP`.

下载者再连接其他下载者,根据种子文件,两者分别`告知`对方自己`已经有的块`,然后`交换`对方所`没有的数据`.此时不需要其他服务器参与,分散了单个线路上的数据流量,因此减少了服务器的负担

优点:  
* 一般的HTTP/FTP下载,发布文件仅在某个或某几个服务器,下载的人太多,服务器的带宽很容易不胜负荷,变得很慢.  
* 而BitTorrent协议下载的特点是，`下载的人越多`，`提供的宽带也越多`，`下载的速度就越快`．拥有完整的文件用户也越来越多，使文件的＂寿命＂不断延长．

DHT网络:  

可以在无Tracker的情况下下载

全称分布式哈希表(`Distributed Hash Table`),一种分布式存储方法.在不需要服务器的情况下,每个客户端都负责一个`小范围的路由`,并存储一小部分数据,从而实现整个DHT网络的寻址和存储.从而实现整个DHT网络的寻址和存储,使用支持该技术的BT下载软件,`用户无需连上Tracker就可以下载`,因为软件会在DHT网络中寻找下载同一个文件的其他用户并与之通讯,开始下载任务.


<a id="markdown-2-torrent实践" name="2-torrent实践"></a>
# 2. torrent实践

```bash
# 安装
npm install -g parse-torrent

# 查看种子文件
parse-torrent ./1.torrent

```

<a id="markdown-33-bittorrent" name="33-bittorrent"></a>
# 3.3. bittorrent


* torrent: 服务器接收的元数据文件(通常结尾是.torrent). 例如: 文件名,文件大小,文件的哈希值.以及Tracker的URL地址
* tracker: 负责`协调BitTorrent客户端行动`的服务器,当你打开一个torrent,你的机器连接tracker,并且请求一个可以接触的peers列表
* peer: `peer有完整的文件`,peers之间相互下载,上传
* seed: `有一个特定Torrent完整拷贝的电脑称为Seed`,文件初次发布时,需要一个seed进行初次共享
* swarm: 连接一个Torrent的所有设备群组
* chocking: 临时的`拒绝上传策略`,虽然上传停止了,但是`下载仍然继续`,对于不合作的peer,会采取临时的阻断策略
* Paretor效率: 帕累托效率(Pareto efficiency),`资源分配到了物尽其用的阶段`,对任意一个个体进一步提升效率只会导致其他个体效率下降,此时说明系统已经达到最优化了
* 针锋相对(Tit-fot-Tat): 博弈论简单的策略. 在Bittorrent中表现为,`Peers给自己贡献多少下载速度,那么也就贡献多少上传速度给它`


做种流程:  seed会生成一个扩展名为.torrent文件,包含`1.文件名,大小` `2.Tracker的URL`,一旦Seeds向Tracker注册,它就开始等待`为需要这个Torrent的Peers上传`,


分块交换:  BitTorrent把文件切割成大小为256k的小片.每一个下载者需要向他的Peers,提供它拥有的片.只有peers`检查了片段是完整的`,才会`通知其他Peers`,`自己拥有这个片段`,可以提供上传.


片段选择算法:  `如果某片段极少数Peers有备份`,这些Peers下线了,网络上就不能找到备份了,所有Peers都不能完成下载.针对这样的问题,BitTorrent提供了一系列`片段选择的策略`.
* 优先完成单一片段: 如果请求了某一片段的`子片段`,那么`本片段会被最优先请求`.这样做是为了能尽可能的先完成一个完整的片段
* 优先选择稀缺片段: `优先选择拥有者最少的片段`. 避免了风险: 拥有稀缺片段的peers停止上传,所有peers都不能得到完整的文件
* 第一个片段随机选择: 最少的片断,通常只有一个peer拥有,可能比多个peers都拥有的那些片断`下载的要慢`.因此第一个片断是随机选择的
* 结束时按照子片断的请求: ???

阻塞策略: 每个peers都有义务来共同提高共享的效率,对于合作者,`会根据对方给予同等的上传速率回报`.对于不合作者,就会`临时拒绝对它的上传`,但是下载依然继续.


* BitTorrent的阻塞算法:  每10秒重新计算一次与peers的连接
* 最优化阻塞: 始终畅通的连接,不论目前的下载情况,它每间隔30秒就会重新计算一次哪一个连接应该是最优化阻塞.30秒的周期完全够达到最大化上传和下载速度了
* 反对歧视: 某个Peer可能被全部的peers都阻塞了,为了减轻这个问题,如果过了一段时间以后,`从某个peer那里一个片段也没有得到`,那么这个peer认为自己被对方怠慢了,于是`不再为对方提供上传`
* 完成后的上传: 一旦peer完成下载任务了,就不再以它的下载速率决定为哪些peers提供上传服务....

