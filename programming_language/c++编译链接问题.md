---
title: c++编译链接问题
date: 2018-1-14 19:20:12
categories: [编程语言]
---

<!-- TOC -->

- [1. 资料](#1-资料)
- [2. 我的问题](#2-我的问题)
- [3. 命令](#3-命令)
- [4. 问题解决](#4-问题解决)

<!-- /TOC -->


<a id="markdown-1-资料" name="1-资料"></a>
# 1. 资料

* https://gcc.gnu.org/onlinedocs/gcc/Warning-Options.html (选项说明)

<a id="markdown-2-我的问题" name="2-我的问题"></a>
# 2. 我的问题

使用muduo时,依赖如下:

libmuduo_inspect.a <- libmuduo_http.a <- libmuduo_net.a <- libmuduo_base.a

其测试inspect的工程链接如下,可以正常编译:
```
add_executable(inspector_test tests/Inspector_test.cc)
target_link_libraries(inspector_test muduo_inspect)
```

我在外部编译时需要把所有相关库依赖上才可以编译过,为啥?
```
add_executable(memcached server.cpp)
target_link_libraries(memcached muduo_inspect muduo_http muduo_net muduo_base pthread)
```

<a id="markdown-3-命令" name="3-命令"></a>
# 3. 命令


```
# 查看符号
nm xxx.a

```

<a id="markdown-4-问题解决" name="4-问题解决"></a>
# 4. 问题解决

关键还是在cmake,cmake工程自动分析了依赖

这个是cmake的
```
muduo/net/inspect/CMakeFiles/inspector_test.dir/link.txt:g++   -g -DMUDUO_STD_STRING -DCHECK_PTHREAD_RETURN_VALUE -D_FILE_OFFSET_BITS=64 -Wall -Wextra -Werror -Wconversion -Wno-unused-parameter -Wold-style-cast -Woverloaded-virtual -Wpointer-arith -Wshadow -Wwrite-strings -march=native -std=c++0x -rdynamic -O2 -finline-limit=1000 -DNDEBUG    CMakeFiles/inspector_test.dir/tests/Inspector_test.cc.o  -o ../../../bin/inspector_test -rdynamic ../../../lib/libmuduo_inspect.a ../../../lib/libmuduo_http.a ../../../lib/libmuduo_net.a ../../../lib/libmuduo_base.a -lpthread -lrt 
```

这个是我的
```
memcached/server/CMakeFiles/memcached.dir/link.txt:g++   -g -DMUDUO_STD_STRING -DCHECK_PTHREAD_RETURN_VALUE -D_FILE_OFFSET_BITS=64 -Wall -Wextra -Werror -Wconversion -Wno-unused-parameter -Wold-style-cast -Woverloaded-virtual -Wpointer-arith -Wshadow -Wwrite-strings -march=native -std=c++0x -rdynamic -O0    CMakeFiles/memcached.dir/server.cpp.o  -o ../../bin/memcached  -L/opt/muduo/build/release-install-cpp11/lib -rdynamic -lmuduo_inspect -Wl,-rpath,/opt/muduo/build/release-install-cpp11/lib 
```
