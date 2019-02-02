---
title: uml
date: 2017-11-25 18:58:21
categories: [编程语言]
---

<!-- TOC -->

- [1. 资料](#1-资料)
- [我认为常用的](#我认为常用的)

<!-- /TOC -->

<a id="markdown-1-资料" name="1-资料"></a>
# 1. 资料

* http://www.plantuml.com/plantuml/uml/SyfFKj2rKt3CoKnELR1Io4ZDoSa70000
* http://www.jianshu.com/p/1256e2643923 (21分钟入门uml)
* http://www.jianshu.com/p/e92a52770832 
* http://blog.csdn.net/tianhai110/article/details/6339565 (几种关系的总结)
* https://zhuanlan.zhihu.com/p/22717889 (类图-继承、实现、泛化、依赖、关联、聚合、组合)


![](https://pic3.zhimg.com/80/v2-210b63fc2770591a3f1dbb2925d0c169_hd.jpg)  

![](https://pic2.zhimg.com/80/v2-32bbb1eac0f327d90461441dd14671e8_hd.jpg)  

依赖: A类的方法中,形参是B类的变量,或者B类指针或者B类的引用,A依赖于B  
![](https://pic2.zhimg.com/80/v2-71a518c254924b7723a533752899cdcb_hd.jpg)  

关联: A类有成员变量是B的类型,或者B类的指针类型,则A类关联于B  
![](https://pic2.zhimg.com/80/v2-e1dee21b7274e566d0dcd36f59d1e5da_hd.jpg)  

聚合(关联的特例): 整体与部分的关系,整体和部分可以分开:  
![](https://pic2.zhimg.com/80/v2-34057fc8fe4bbcee939a6982b9f6d3de_hd.jpg)  

组合(关联的特例): 整体与部分的关系,整体和部分不可以分开:  
![](https://pic4.zhimg.com/80/v2-6eacb1a4d9f56c3c09bd805c2c8db01d_hd.jpg)  



<a id="markdown-我认为常用的" name="我认为常用的"></a>
# 我认为常用的


* 用例图
* 类图   --- 类与类之间关系的梳理
* 对象图?
* 包图
* 活动图 --- 功能角度的梳理
* 状态图 --- tcp的状态变迁
* 序列图 --- 不同模块之间的调用流程
* 协作图
* 构件图
* 部署图
