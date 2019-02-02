---
title: c++包管理
date: 2017-12-16 21:03:45
categories: [编程语言]
---


<!-- TOC -->

- [1. 资料](#1-资料)
- [2. 实践](#2-实践)
- [3. 配置文件](#3-配置文件)
- [4. Boost](#4-boost)
- [5. muduo](#5-muduo)
- [6. glibc](#6-glibc)

<!-- /TOC -->



<a id="markdown-1-资料" name="1-资料"></a>
# 1. 资料

* https://conan.io/
* http://docs.conan.io/en/latest/introduction.html (文档)
* https://bintray.com/conan/conan-transit (从原conan转移的)
* https://en.wikipedia.org/wiki/List_of_software_package_management_systems (操作系统包管理)
* https://en.wikipedia.org/wiki/Binary_repository_manager (二进制包管理)
* http://mall.csdn.net/product/1237 (jfrog)
* https://jfrog.com/


<a id="markdown-2-实践" name="2-实践"></a>
# 2. 实践


``` bash
# 安装conan
pip install conan

conan remote add community https://api.bintray.com/conan/conan-community/conan

conan search Boost* -r=community

```

<a id="markdown-3-配置文件" name="3-配置文件"></a>
# 3. 配置文件
```
vim /root/.conan/profiles/default
```

修改成:
```
[build_requires]
[settings]
os=Linux
arch=x86_64
compiler=clang++
compiler.version=3.4.2
compiler.libcxx=libstdc++11
build_type=Release
[options]
[env]
```




<a id="markdown-4-boost" name="4-boost"></a>
# 4. Boost

* http://www.boost.org/doc/libs/1_61_0/more/getting_started/unix-variants.html

```
wget https://dl.bintray.com/boostorg/release/1.65.1/source/boost_1_65_1.tar.gz

# 或
scp boost_1_65_1.tar.gz root@vm1:/root/reference/package

tar -xvzf boost_1_65_1.tar.gz
cd boost_1_65_1
./bootstrap.sh --prefix=/usr/local
./b2 install --with-system --with-program_options --with-test --with-log

# 头文件
/usr/local/include/boost

# lib库
/usr/local/lib/libboost_system.a
```


所有的库
```
[root@yqsy boost_1_65_1]# ./b2 --show-libraries
The following libraries require building:
    - atomic
    - chrono
    - container
    - context
    - coroutine
    - date_time
    - exception
    - fiber
    - filesystem
    - graph
    - graph_parallel
    - iostreams
    - locale
    - log
    - math
    - metaparse
    - mpi
    - program_options
    - python
    - random
    - regex
    - serialization
    - signals
    - stacktrace
    - system
    - test
    - thread
    - timer
    - type_erasure
    - wave
```

该死的,这个版本的muduo都编译不过,还是用yum的1.5.3吧
```
sudo yum install boost-devel -y
```

<a id="markdown-5-muduo" name="5-muduo"></a>
# 5. muduo

* https://github.com/chenshuo/muduo-tutorial

1.0.9版本 (c++98)
```
sudo su - root
mkdir -p /opt/muduo-1.0.9
cd /opt/muduo-1.0.9
wget https://github.com/chenshuo/muduo/archive/v1.0.9.tar.gz
tar -xvzf v1.0.9.tar.gz
cd muduo-1.0.9
sed -i 's/# -DMUDUO_STD_STRING/-DMUDUO_STD_STRING/g'  CMakeLists.txt
BUILD_TYPE=release ./build.sh -j2
BUILD_TYPE=release ./build.sh install
```

11版本
```
sudo su - root
rm -rf /opt/muduo-1.0.9/
mkdir -p /opt/muduo
cd /opt/muduo
git clone https://github.com/chenshuo/muduo
cd muduo
git checkout -b cpp11 origin/cpp11
sed -i 's/# -DMUDUO_STD_STRING/-DMUDUO_STD_STRING/g'  CMakeLists.txt
BUILD_TYPE=release ./build.sh -j2
BUILD_TYPE=release ./build.sh install
```

<a id="markdown-6-glibc" name="6-glibc"></a>
# 6. glibc
可以让visual code 找到头文件
```
yum install glibc-devel.i686 -y
```
