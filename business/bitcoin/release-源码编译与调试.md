---
title: 源码编译与调试
date: 2018-02-01 13:29:12
categories: [business, bitcoin]
---


<!-- TOC -->

1. [1. 说明](#1-说明)
2. [2. arch环境](#2-arch环境)
3. [3. 代码组织](#3-代码组织)
4. [4. 参考资料](#4-参考资料)

<!-- /TOC -->

<a id="markdown-1-说明" name="1-说明"></a>
# 1. 说明


```bash
# 环境: kubuntu 18.04

# 获取v0.17.0源码 创建阅读分支
cd /mnt/disk1/linux/reference/refer
git clone https://github.com/bitcoin/bitcoin
cd bitcoin
git checkout tags/v0.17.0 -b readerbranch

# 依赖
sudo add-apt-repository universe
sudo apt-get update

sudo apt-get install build-essential libtool autotools-dev automake pkg-config libssl-dev libevent-dev bsdmainutils python3 libboost-system-dev libboost-filesystem-dev libboost-chrono-dev libboost-test-dev libboost-thread-dev -y

sudo apt-get install software-properties-common -y 
sudo add-apt-repository ppa:bitcoin/bitcoin
sudo apt-get update
sudo apt-get install libdb4.8-dev libdb4.8++-dev -y 

sudo apt-get install libminiupnpc-dev -y

sudo apt-get install libzmq3-dev -y 

sudo apt-get install libqt5gui5 libqt5core5a libqt5dbus5 qttools5-dev qttools5-dev-tools libprotobuf-dev protobuf-compiler -y

sudo apt-get install libqrencode-dev -y 

# 修改configure.ac 关闭优化,改成-O0
252:    [-Og],
253:    [[DEBUG_CXXFLAGS="$DEBUG_CXXFLAGS -Og"]],
611:  CXXFLAGS="$CXXFLAGS -Og"

# 开启附加调试
echo 0 | sudo tee /proc/sys/kernel/yama/ptrace_scope

# 编译调试版本
./autogen.sh && ./configure --enable-debug
make -j 8 && sudo make install
```

添加阅读源码的src/CMakeFile.txt (使用clion可直接启动make编译的程序,并且单步跟踪代码)

```bash
cmake_minimum_required(VERSION 3.12)
project(src)

set(CMAKE_CXX_STANDARD 11)

include_directories(${PROJECT_SOURCE_DIR}/secp256k1/include
        ${PROJECT_SOURCE_DIR}/leveldb/include
        ${PROJECT_SOURCE_DIR}/univalue/include
        ${PROJECT_SOURCE_DIR}
        )


file(GLOB_RECURSE SRCS *.cpp *,h)

add_executable(src ${SRCS})
```

<a id="markdown-2-arch环境" name="2-arch环境"></a>
# 2. arch环境

```bash
sudo pacman -S git base-devel boost libevent python
yaourt -S --noconfirm db4.8

cd /mnt/disk1/linux/reference/refer/bitcoin

./autogen.sh && ./configure --enable-debug  --without-gui --without-miniupnpc

# --disable-wallet

make -j 8 && sudo make install
```

<a id="markdown-3-代码组织" name="3-代码组织"></a>
# 3. 代码组织

统计源码指令: 
```bash
cd /mnt/disk1/linux/reference/refer/bitcoin

# 目录内的源码统计
echo "" > /tmp/1.txt
find . -maxdepth 1 -type d -print0 | while read -d '' -r dir; do
    files=("$dir"/*)
    sum=`find $files -regex '.*\.\(cpp\|c\|h\)' -type f -print0 | xargs -0 wc -l | sort -nr | head -n 1 | awk '{print $1}'`
    printf "%-20s %s \n" "$dir" "$sum" >> /tmp/1.txt
done
sort  -k 2 -nr < /tmp/1.txt

# src目录下的源码统计
find ./ -maxdepth 1  -regex '.*\.\(cpp\|c\|h\)' -type f -print0 | xargs -0 wc -l | sort -nr | head -n 1 | awk '{print $1}'

```

源码:  
```bash
./qt                 280723 # qt *
./bench              126491 # bench mark  *
./test               92572  # 单元测试 *
./secp256k1          18712  # 椭圆曲线加密算法 *
./wallet             17493   
./rpc                7734  
./leveldb            6200   # leveldb *
./script             6031  
./crypto             5712   
./univalue           2401   # json *
./policy             1860  
./interfaces         1438   
./support            864    
./index              716 
./primitives         708 
./consensus          669 
./zmq                652 
./compat             539 
./config             434 

./                   46321  # 只搜索当前一层目录的

# 去除 qt,benchmark,单元测试  以及引用的外部库. 源码大概在8w行左右.
```

<a id="markdown-4-参考资料" name="4-参考资料"></a>
# 4. 参考资料

* https://github.com/bitcoin/bitcoin/blob/v0.17.0/doc/build-unix.md
