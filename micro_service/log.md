---
title: log
date: 2017-12-25 22:25:30
categories: [微服务]
---


<!-- TOC -->

- [1. 资料](#1-资料)
- [2. 实践](#2-实践)

<!-- /TOC -->

<a id="markdown-1-资料" name="1-资料"></a>
# 1. 资料

* https://www.cnblogs.com/sailrancho/p/4784763.html (lograte)
* https://superuser.com/questions/291368/log-rotation-of-stdout (standout 配合lograte)
* https://httpd.apache.org/docs/2.4/programs/rotatelogs.html (工具)

<a id="markdown-2-实践" name="2-实践"></a>
# 2. 实践     
```bash
yum install httpd -y

sudo mkdir /var/log/frp
sudo chown $(id -u):$(id -g) /var/log/frp
nohup ./frps -c ./frps.ini | rotatelogs /var/log/frp/frp.log-%Y%m%d 86400 &

```