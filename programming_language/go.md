---
title: go
date: 2017-12-1 21:47:45
categories: [编程语言]
---


<!-- TOC -->

- [1. 资料](#1-资料)
- [2. 其他](#2-其他)
- [3. 错误处理](#3-错误处理)
- [4. 对于json,bencode如何处理](#4-对于jsonbencode如何处理)
- [5. interface使用场景](#5-interface使用场景)

<!-- /TOC -->

<a id="markdown-1-资料" name="1-资料"></a>
# 1. 资料

* http://www.ctolib.com/cheatsheets-go-project.html (开源项目速查)
* https://tour.golang.org/welcome/1 (a tour of go)
* https://github.com/golang/go/wiki/GoGetProxyConfig (go get 使用代理)
* https://www.zhihu.com/question/20862617 (routine 实现)

<a id="markdown-2-其他" name="2-其他"></a>
# 2. 其他

关优化编译
```bash
go install  -gcflags "-N -l"
```


环境变量
```bash

cat >> ~/.profile << EOF
# go godoc gofmt
export PATH=/usr/local/go/bin:\$PATH

# custom location
export GOPATH=\$HOME/go
export PATH=\$GOPATH/bin:\$PATH
EOF
```

<a id="markdown-3-错误处理" name="3-错误处理"></a>
# 3. 错误处理


```
外部输入错误,   1. object无key 2. 类型不对    捕获panic  ??   (范围,数值类型其他判断普通error) ??? 不能捕获的,这是runtime-error!!!
https://blog.golang.org/defer-panic-and-recover
```

* 内部处理错误, return error
* 重要错误,无法挽救 panic


<a id="markdown-4-对于jsonbencode如何处理" name="4-对于jsonbencode如何处理"></a>
# 4. 对于json,bencode如何处理

三种方案
1. 反射到静态定义的类型上 (例如: go json官方解析库, protobuf)
2. 包一层object来给接口调用 (例如:c++)
3. 解析到内置动态类型(例如:go interface, js 原生类型),并提供检查接口 1. 类型 2. key

(3.)代码写起来很啰嗦的(有异常会好一些)
1. interface{} 类型判断
2. object key 判断


<a id="markdown-5-interface使用场景" name="5-interface使用场景"></a>
# 5. interface使用场景

* json,bencode (上面地第三种方案,将动态的外部类型转换到内部的`原生的动态类型上`)
* 范型(容器类(blockqueue),类型分发(codec)) -- `c++范型可以编译期决定,go interface 延迟到运行期`
* 接口 --  `c++实现 范式 class : class , 将具体的实现延迟到运行期`
