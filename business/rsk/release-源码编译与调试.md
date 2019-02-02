---
title: 源码编译与调试
date: 2018-09-06 10:33:42
categories: [business, rsk]
---


<!-- TOC -->

- [1. 说明](#1-说明)
- [2. 代码组织](#2-代码组织)

<!-- /TOC -->


<a id="markdown-1-说明" name="1-说明"></a>
# 1. 说明

源码拉取:

```bash
cd /mnt/disk1/linux/reference/refer
git clone --recursive https://github.com/rsksmart/rskj.git
cd rskj
git checkout tags/ORCHID-0.6.0 
git branch -d master
git checkout -b master

chmod +x ./configure.sh
./configure.sh

# 再用 intellij IDEA 加载 build.gradle
```

<a id="markdown-2-代码组织" name="2-代码组织"></a>
# 2. 代码组织

```bash

cd /mnt/disk1/linux/reference/refer/rskj/rskj-core/src/main/java/co/rsk

# 目录内的源码统计
echo "" > /tmp/1.txt
find . -maxdepth 1 -type d -print0 | while read -d '' -r dir; do
    files=("$dir"/*)
    sum=`find $files *.java -type f -print0 | xargs -0 wc -l | sort -nr | head -n 1 | awk '{print $1}'`
    printf "%-20s %s \n" "$dir" "$sum" >> /tmp/1.txt
done
sort  -k 2 -nr < /tmp/1.txt

# rsk目录下的源码统计
find .   *.java -maxdepth 1  -type f -print0 | xargs -0 wc -l | sort -nr | head -n 1 | awk '{print $1}'

```

源码:
```bash
./net                9959  
./peg                8060 
./core               4392 
./rpc                4297 
./mine               3213 
./trie               2407 
./validators         2388 
./config             2319 
./remasc             2009 
./db                 1860 
./scoring            1767 
./util               1188 
./jsonrpc            1103 
./crypto             1100 
./cli                1072 
./metrics            923 
./blocks             910 
./vm                 735 
./panic              701 

./                   1332 # 只搜索当前一层目录的

# 总源码量在51735行左右
```

