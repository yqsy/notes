---
title: Monitor
date: 2018-01-02 14:08:11
categories: [微服务]
---


<!-- TOC -->

- [1. 资料](#1-资料)
    - [1.1. 开源方案](#11-开源方案)
    - [1.2. 前端展示](#12-前端展示)
- [2. 核心问题](#2-核心问题)
- [3. 时序数据库实践](#3-时序数据库实践)
- [4. glances调试环境搭建](#4-glances调试环境搭建)
- [5. 使用flask模拟glances小计](#5-使用flask模拟glances小计)
- [tick stack方案搭建小计](#tick-stack方案搭建小计)
- [6. 分析小计](#6-分析小计)

<!-- /TOC -->


<a id="markdown-1-资料" name="1-资料"></a>
# 1. 资料

* https://www.zhihu.com/question/19636141/answer/13154248 (常用的运维,管理工具)
* https://blog.serverdensity.com/80-linux-monitoring-tools-know/ (80个监控工具)
* http://www.linuxscrew.com/2012/03/22/linux-monitoring-tools/ (排名前5监控系统)
* http://my-netdata.io/ (my-netdata.io 太复杂啦)
* https://hub.docker.com/r/titpetric/netdata/  (这也能在docker里面部署吗)
* https://www.zabbix.com/
* https://www.nagios.org/
* https://github.com/nicolargo/glances (知乎上看到的工具,目测超好用)
* http://glances.readthedocs.io/en/stable/aoa/cpu.html (glance说明文档)
* http://zhuanlan.zhihu.com/p/20385707 (手写 监控,赞)
* https://github.com/nkrode/RedisLive (redis的监控赞,学习一下)
* https://github.com/XiaoMi/open-falcon (小米开源的监控)
* https://zhuanlan.zhihu.com/p/32764309 (17个开源的运维监控系统)
* http://blog.csdn.net/yuzhihui_no1/article/details/65435471 (rdd数据库 时序图环形 复写)
* http://liubin.org/blog/2016/02/25/tsdb-list-part-1/ (时序数据库)
* https://oss.oetiker.ch/rrdtool/ (rrdtool)

<a id="markdown-11-开源方案" name="11-开源方案"></a>
## 1.1. 开源方案

* influxdb 时序数据库 https://en.wikipedia.org/wiki/InfluxDB https://hub.docker.com/_/influxdb/
* kapacitor 报警把 https://github.com/influxdata/kapacitor https://hub.docker.com/_/kapacitor/
* telegraf 收集数据 https://github.com/influxdata/telegraf  https://hub.docker.com/_/telegraf/
* chronograf 展示 https://github.com/influxdata/chronograf https://hub.docker.com/_/chronograf/
* https://docs.influxdata.com/telegraf/v0.13/introduction/installation/ (telegraf安装手册)

<a id="markdown-12-前端展示" name="12-前端展示"></a>
## 1.2. 前端展示

* https://www.highcharts.com/stock/demo (控件)
* http://glances.readthedocs.io/en/stable/gw/influxdb.html (我擦,直接配置配置就可以可视化啦?!)
* http://zhuanlan.zhihu.com/p/28570033 (10 分钟内快速构建能够承载海量数据的 NG<em>I</em>NX 日志分析与报警平台 - 七牛云的文章 - 知乎)


<a id="markdown-2-核心问题" name="2-核心问题"></a>
# 2. 核心问题

* 数据如何采集?应用程序提供查询接口?写入文件?还是直接提供web接口?
* 采集多台机器是否需要agent?

<a id="markdown-3-时序数据库实践" name="3-时序数据库实践"></a>
# 3. 时序数据库实践

* https://github.com/pldimitrov/Rrd/issues/1  (安装)

```bash
sudo yum install rrdtool-devel rrdtool -y
sudo yum install python34-devel -y
sudo pip3 install rrdtool
```

<a id="markdown-4-glances调试环境搭建" name="4-glances调试环境搭建"></a>
# 4. glances调试环境搭建

```bash
sudo yum install python34-devel -y
git clone https://github.com/nicolargo/glances
cd glances
sudo pip3 install -r requirements.txt

sudo pip3 install bottle requests
sudo pip3 install glances

python3 -m glances -w
```

<a id="markdown-5-使用flask模拟glances小计" name="5-使用flask模拟glances小计"></a>
# 5. 使用flask模拟glances小计

```bash
# 库安装
sudo pip3 install SQLAlchemy
sudo pip3 install flask

sudo yum install openssl-devel -y
sudo pip3 install PyJWT

# 数据库创建
from ymonitor import db

db.create_all()

# 收集资料资源
https://psutil.readthedocs.io/en/latest/#memory


# 模拟cpu负载
sudo yum install stress -y
stress --cpu 2 --timeout 60
```

<a id="markdown-tick-stack方案搭建小计" name="tick-stack方案搭建小计"></a>
# tick stack方案搭建小计

```bash
docker network create influxdb-network

mkdir -p ~/env/influxdb
cd ~/env/influxdb
docker run -d --name influxdb \
    -p 8086:8086 \
    --network influxdb-network \
    -v $PWD:/var/lib/influxdb \
    influxdb

mkdir -p ~/env/chronograf
cd ~/env/chronograf
docker run -d --name chronograf \
    -p 8888:8888 \
    --network influxdb-network \
    -v $PWD:/var/lib/chronograf \
    chronograf --influxdb-url=http://influxdb:8086

# 主机上装telegraf
cat <<EOF | sudo tee /etc/yum.repos.d/influxdb.repo
[influxdb]
name = InfluxDB Repository - RHEL \$releasever
baseurl = https://repos.influxdata.com/rhel/\$releasever/\$basearch/stable
enabled = 1
gpgcheck = 1
gpgkey = https://repos.influxdata.com/influxdb.key
EOF

sudo su - root
export http_proxy=http://host1:1080
export https_proxy=http://host1:1080
yum clean all
yum install telegraf -y
exit

telegraf config | sudo tee /etc/telegraf/telegraf.conf

sudo systemctl start telegraf
sudo systemctl enable telegraf
```


<a id="markdown-6-分析小计" name="6-分析小计"></a>
# 6. 分析小计

```
strace netstat -g &> 1.txt && grep 'open' ./1.txt  > 2.txt

https://www.centos.org/docs/5/html/5.1/Deployment_Guide/s2-proc-meminfo.html
vmstat 内存
open("/proc/meminfo", O_RDONLY)         = 3
open("/proc/stat", O_RDONLY)            = 4
open("/proc/vmstat", O_RDONLY)          = 5

iostat  cpu  / 磁盘I/O
open("/proc/diskstats", O_RDONLY)       = 3
open("/proc/uptime", O_RDONLY)          = 3
open("/proc/stat", O_RDONLY)            = 3

mpstat
open("/proc/interrupts", O_RDONLY)      = 3
open("/proc/softirqs", O_RDONLY)        = 3
open("/proc/uptime", O_RDONLY)          = 3
open("/proc/stat", O_RDONLY)            = 3


tcp 连接数
netstat -ant

open("/proc/net/tcp", O_RDONLY)         = 3
open("/proc/net/tcp6", O_RDONLY)        = 3

udp
netstat -anu

open("/proc/net/udp", O_RDONLY)         = 3
open("/proc/net/udp6", O_RDONLY)        = 3


所有监听
netstat -tuln

如果设置了-p则会读取每一个文件
open("/proc/net/tcp", O_RDONLY)         = 3
open("/proc/net/tcp6", O_RDONLY)        = 3
open("/proc/net/udp", O_RDONLY)         = 3
open("/proc/net/udp6", O_RDONLY)        = 3


静态分析
netstat -s
open("/proc/meminfo", O_RDONLY|O_CLOEXEC) = 3
open("/proc/net/snmp", O_RDONLY)        = 3
open("/proc/net/netstat", O_RDONLY)     = 3
open("/proc/net/sctp/snmp", O_RDONLY)   = -1 ENOENT (No such file or directory)


路由表
netstat -r

open("/etc/nsswitch.conf", O_RDONLY|O_CLOEXEC) = 4
open("/etc/resolv.conf", O_RDONLY|O_CLOEXEC) = 4
open("/etc/host.conf", O_RDONLY|O_CLOEXEC) = 4
open("/etc/hosts", O_RDONLY|O_CLOEXEC)  = 4
open("/etc/networks", O_RDONLY|O_CLOEXEC) = 4



网卡
netstat -i

open("/proc/net/dev", O_RDONLY)         = 6


网卡 similar to ifconfig
netstat -ie

open("/proc/net/dev", O_RDONLY)         = 6
open("/proc/net/if_inet6", O_RDONLY)    = 6


磁盘I/O
网络I/O
CPU
内存
中断
磁盘容量

业务信息
接口?


时间维度:
24小时
一周
一个月

86400 / 3 = 28800 (每天生成)
28800 * 30 = 201600

```
