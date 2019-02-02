---
title: cpu
date: 2017-10-23 14:26:38
categories: [linux, 系统管理]
---
<!-- TOC -->

- [1. 资料](#1-资料)
- [2. 查看信息](#2-查看信息)
- [3. 查看cpu信息](#3-查看cpu信息)

<!-- /TOC -->


<a id="markdown-1-资料" name="1-资料"></a>
# 1. 资料

* https://www.anandtech.com/bench/CPU/1603 (cpu benchmark)

<a id="markdown-2-查看信息" name="2-查看信息"></a>
# 2. 查看信息

```bash
# 查看cpu
cat /proc/cpuinfo | grep "physical id" | sort | uniq | wc -l

# 查看每个物理cpu中core的个数
cat /proc/cpuinfo | grep "cpu cores" | uniq

# 显示逻辑CPU的个数
cat /proc/cpuinfo | grep "processor" | wc -l

# 针对进程名看
top -c -p $(pgrep -d',' -f ./client)
```

<a id="markdown-3-查看cpu信息" name="3-查看cpu信息"></a>
# 3. 查看cpu信息
```
cat /proc/cpuinfo

lscpu
```