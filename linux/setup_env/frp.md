---
title: frp
date: 2018-02-01 13:29:12
categories: [linux, 搭建环境]
---


<!-- TOC -->

- [1. 说明](#1-说明)

<!-- /TOC -->


<a id="markdown-1-说明" name="1-说明"></a>
# 1. 说明

* https://github.com/fatedier/frp


```bash
# 服务器
wget https://github.com/fatedier/frp/releases/download/v0.21.0/frp_0.21.0_linux_amd64.tar.gz

tar -xzf frp_0.21.0_linux_amd64.tar.gz

cd frp_0.21.0_linux_amd64
./frps -c ./frps.ini

```

```bash
# 客户端
wget https://github.com/fatedier/frp/releases/download/v0.21.0/frp_0.21.0_linux_amd64.tar.gz

tar -xzf frp_0.21.0_linux_amd64.tar.gz
cd frp_0.21.0_linux_amd64

vim frpc.ini
./frpc -c ./frpc.ini

```
