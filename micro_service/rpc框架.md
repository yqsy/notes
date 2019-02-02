---
title: rpc框架
date: 2017-12-17 22:53:56
categories: [微服务]
---

<!-- TOC -->

- [1. 资料](#1-资料)
- [2. 维度](#2-维度)

<!-- /TOC -->

<a id="markdown-1-资料" name="1-资料"></a>
# 1. 资料

* https://github.com/brpc/brpc/blob/master/README_cn.md
* https://www.zhihu.com/question/49617328/answer/116923669 (为什么需要rpc)
* https://www.zhihu.com/question/41609070 (既然有了http请求为什么还需要rpc框架?)
* http://p.primeton.com/articles/59030eeda6f2a40690f03629 (选择)

<a id="markdown-2-维度" name="2-维度"></a>
# 2. 维度

连接方式
* 短链接: 每次请求前创建一个新连接,完成后关闭
* 连接池: 每次请求前从pool中获取一个新连接,结束后归还
* 单连接: 所有发往同一地址的请求/返回,公用同一个连接

负载均衡方式
* random
* Round-Robin
* 一致性hash

服务发现
* Zookeeper (zab)
* etcd (raft)
* consul (raft)

追踪

健康检查

认证

