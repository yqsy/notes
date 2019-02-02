---
title: relay
date: 2018-1-24 22:43:23
categories: [网络相关]
---


<!-- TOC -->

- [1. 资料](#1-资料)
- [2. 实践](#2-实践)
- [3. socks5研究](#3-socks5研究)

<!-- /TOC -->

<a id="markdown-1-资料" name="1-资料"></a>
# 1. 资料

* https://unix.stackexchange.com/questions/115897/whats-ssh-port-forwarding-and-whats-the-difference-between-ssh-local-and-remot (tcp relay)
* http://blog.csdn.net/chenjh213/article/details/49795521 (中文介绍)
* switchysharp (chrome代理插件)

<a id="markdown-2-实践" name="2-实践"></a>
# 2. 实践

```bash
# 暴露了一个端口
http://127.0.0.1:4040

# 在本机上使用ssh tunnel,即可访问
ssh -NL  9001:localhost:4040 root@pi1

-N (Do not execute remote command)
-f (Go to background)
-L (Locally forwarded ports)
-R (Remotely forwarded ports)

# 将远程的 x.x.x.x:22 映射到本地的:9001
ssh -NL 9001:x.x.x.x:22 pi@pi1

# 将本地的x.x.x.x:22 映射到远程的:9001
ssh -NR 9001:x.x.x.x:22 pi@pi1

# socks4 socks5
ssh -ND 1080 root@gg
```


<a id="markdown-3-socks5研究" name="3-socks5研究"></a>
# 3. socks5研究

sshd  
raw ==== local ===ssh tun=== remote socks5 ====other  

而shadowsocks是这样的!  
raw ==== local socks5 === 加密 === remote shadowsocks自定义协议 ==== other  

怎么得知这个结论?

```bash
# 树莓派
chmod 700 ~/.ssh/id_rsa
eval `ssh-agent -s`
ssh-add

ssh -ND 1080 yq@vm1

# 抓包
sudo tcpdump -i lo port 1080 -w /home/pi/env/tcpdump/1080stop.pcap

# 在另一台服务器上中止socks5 server
kill -STOP 62365

# 这个是恢复
kill -CONT 62365

# centos nc
nc --proxy-type socks4 --proxy 127.0.0.1:1080 localhost 5003

# debian nc
nc -X 4 -x 127.0.0.1:1080 localhost 5003

```

抓包结果

```bash
4	0.000657	127.0.0.1	Socks	1080	75	Version: 4, Remote Port: 5003
6	12.166724(回复后才有应答)	127.0.0.1	Socks	52678	74	Version: 4, Remote Port: 5003 (应答)

# 注意恢复后才有应答
```

