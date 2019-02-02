---
title: shadowsocks
date: 2018-5-9 21:08:24
categories: [项目分析]
---

<!-- TOC -->

- [1. 分析](#1-分析)
- [2. 检测文献](#2-检测文献)
- [3. 流量混淆](#3-流量混淆)

<!-- /TOC -->

<a id="markdown-1-分析" name="1-分析"></a>
# 1. 分析

```
browser -> locale -> server -> remote
browser <- locale <- server <- remote
```

local提供socks5的接口,local和server的通讯是自制协议


缺点:
* 没有账户/密码/流量统计 相关机制
* 没有监控/管理web页面
* session key不是预共享密钥,加密套件和密钥都是事先商议好的. 无法前向保密.
* 协议没有hash key,(MAC) 被篡改后无法被发现
* <加密后的协议可以被试探,IV固定 (其实没法防御,最多混淆)>
* 非阻塞代码切成多段,看起来很烦
* 包头解析的时候把流当包解析了
* 作为双端proxy不能正确处理半关闭
* 吞吐量? 本机 100MB /s.(aes-256-cfb) 我的有700MB/s


<a id="markdown-2-检测文献" name="2-检测文献"></a>
# 2. 检测文献

* https://docs.google.com/viewer?url=patentimages.storage.googleapis.com/pdfs/c4655bdfd3bcee64d0a3/CN105281973A.pdf 


<a id="markdown-3-流量混淆" name="3-流量混淆"></a>
# 3. 流量混淆

* https://github.com/shadowsocks/simple-obfs
