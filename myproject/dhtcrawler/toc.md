<!-- TOC -->

- [1. 说明](#1-说明)
- [2. anacrolix/torrent项目观察](#2-anacrolixtorrent项目观察)
- [3. 参考资料](#3-参考资料)

<!-- /TOC -->

<a id="markdown-1-说明" name="1-说明"></a>
# 1. 说明

制作一个DHT爬虫工具,需要用到bittorrent,kademlia,数据库,前端nodejs+后端go jsonrpc接口等等. 底层全部从零实现.

- [ ] bittorrent
    - [ ] bencode
    - [ ] metainfo
- [ ] DHT
    - [ ] DHT表
    - [ ] krpc
    - [ ] 节点
- [ ] 数据采集
    - [ ] 存储
    - [ ] 检阅 json rpc
- [ ] web
    - [ ] nodejs调用层
    - [ ] 前端

<a id="markdown-2-anacrolixtorrent项目观察" name="2-anacrolixtorrent项目观察"></a>
# 2. anacrolix/torrent项目观察

```bash
go get github.com/anacrolix/torrent
```

* dht 3309 - krpc, dht表, 节点 
* go-libutp 3000 - 基于udp的可靠协议
* log 230 - 自己写的
* torrent 15200 - bencode, metainfo, p2p协议, 存储, tracker ...

<a id="markdown-3-参考资料" name="3-参考资料"></a>
# 3. 参考资料

* https://github.com/libp2p/go-libp2p (libp2p)
* https://github.com/anacrolix/torrent (torrent)
