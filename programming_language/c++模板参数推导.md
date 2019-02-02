---
title: c++模板参数推导
date: 2018-10-09 10:32:15
categories: [编程语言]
---


<!-- TOC -->

- [1. 说明](#1-说明)
- [结果](#结果)

<!-- /TOC -->

<a id="markdown-1-说明" name="1-说明"></a>
# 1. 说明

* https://zh.wikipedia.org/wiki/%E5%8F%B3%E5%80%BC%E5%BC%95%E7%94%A8 (右值)
* https://zh.wikipedia.org/wiki/%E6%A8%A1%E6%9D%BF%E5%8F%82%E6%95%B0%E6%8E%A8%E5%AF%BC (模板参数推导)
* https://github.com/yqsy/testtemplate (我的测试)
* https://www.cnblogs.com/zpcdbky/p/4483479.html (参考)

编译器比较函数模板的形参(template parameter)与对应的调用实参(argument used in the function call) 的类型, 来确定模板参数的类型.


梳理:

* T
* const T
* T*
* const T*
* T&
* const T&

--- 

* T&&

引用折叠规则

(引入一下右值的作用):
* 移动语义
* 完美转发
---

* const T&...
* T&&...

--- 
按照我的分析,推导过程中,涉及的变量分为:
* 传入实参类型
* 推导形参类型
* 函数内实际参数类型

例如
```c++
template<typename T>
void foo(T* t) {
    *t = 1;    
}

const int* d = nullptr;


// 传入实参类型: const int*
// 推导形参类型(T): int
// 实际参数类型(t): int* 
// 所以上面的是无法运行的,问题: 传入实参带const,实际参数不带const,无法赋值

```

<a id="markdown-结果" name="结果"></a>
# 结果


```
T
传递实参         ->         推导形参(T)        -> 实际参数(t)
int             ->         int               ->  int
const int       ->         int               ->  int
int *           ->         int*              ->  int*
const int *     ->         int const*        ->  int const*
int&            ->         int               ->  int
const int&      ->         int               ->  int
--------------------
const T
传递实参         ->         推导形参(T)        -> 实际参数(t)
int             ->         int               ->  const int
const int       ->         int               ->  const int
int *           ->         int*              ->  const int*
const int *     ->         int const*        ->  const int const*
int&            ->         int               ->  const int
const int&      ->         int               ->  const int
--------------------
T*(这个有问题 const int * 应该被推导成 T=const int的)
传递实参         ->         推导形参(T)        -> 实际参数(t)
int *           ->         int               ->  int*
const int *     ->         int               ->  int*
--------------------
const T*
传递实参         ->         推导形参(T)        -> 实际参数(t)
int *           ->         int               ->  const int*
const int *     ->         int               ->  const int*
--------------------
T&
传递实参         ->         推导形参(T)        -> 实际参数(t)
int             ->         int               ->   int &
const int       ->         int               ->   int &
int *           ->         int*              ->   int* &
const int *     ->         int const*        ->   int const* &
int&            ->         int               ->   int &
const int&      ->         int               ->   int &
--------------------
const T&
传递实参         ->         推导形参(T)        -> 实际参数(t)
int             ->         int               ->  const int &
const int       ->         int               ->  const int &
int *           ->         int*              ->  const int* &
const int *     ->         int const*        ->  const int const* &
int&            ->         int               ->  const int &
const int&      ->         int               ->  const int &

```


```bash
T&
传递实参      ->  推导形参(T)   ->   实际参数(t)
A&           ->  A           ->  A&
A&&          ->  A            ->  A&    (这里就有语义问题了)


# 引用折叠,完美转发
T&&
传递实参      ->  推导形参(T)   ->   实际参数(t)
A&          ->   A&           ->   A&
A&&         ->   A            ->   A&&

# 引用塌缩规则
* T& &变为T&
* T& &&变为T&
* T&& &变为T&
* T&& &&变为T&&

```
