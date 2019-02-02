---
title: go锁研究
date: 2018-3-18 20:43:37
categories: [系统底层]
---

<!-- TOC -->

- [1. fdMutex](#1-fdmutex)

<!-- /TOC -->



<a id="markdown-1-fdmutex" name="1-fdmutex"></a>
# 1. fdMutex

一个uint64表示多种状态
* 是否关闭
* 是否正在读
* 是否正在写
* 引用次数 -> decref时如果引用次数为零,及`关闭描述符`
* 读等待数 -> rwlock时要等待锁就会累加 作为increfAndClose close时的`唤醒`(类似信号量), 如果其他goroutine阻塞在poll的话,使用fd.pd.evict()唤醒
* 写等待数 -> 同上
