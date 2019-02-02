---
title: Node.js
date: 2017-11-05 21:52:06
categories: [微服务]
---


<!-- TOC -->

- [1. 简介](#1-简介)
- [2. 应用场景](#2-应用场景)
- [3. 使用Node.js实现反向代理](#3-使用nodejs实现反向代理)
- [4. 实践](#4-实践)

<!-- /TOC -->

<a id="markdown-1-简介" name="1-简介"></a>
# 1. 简介

* https://nodejs.org/en/ (官网)
* https://www.zhihu.com/question/19653241 (优势劣势)
* https://www.zhihu.com/question/37619635 (高性能高并发的本质)
* https://www.zhihu.com/question/24847805/answer/148714624 (nodejs也有协程啦)

Node.js是一个基于Chrome V8引擎的JavaScript运行环境,它使用了一个`事件驱动`且`异步非阻塞I/O`的模型使其轻量且高效,Node.js的包管理器NPM使全球最大的开源库生态系统

<a id="markdown-2-应用场景" name="2-应用场景"></a>
# 2. 应用场景

* I/O密集型Web应用  
 开发I/O密集型应用是Node.js的强项,它充分利用了事件驱动与异步非阻塞技术,能支持大量的并发链接,从而提高了整个系统的吞吐率.不乏优秀的web框架,Express,将基于Node.js的web应用开发过程变得更加简单与高效 http://expressjs.com
 
* web聊天室  
 Node.js是为`实时性`而生的,Web聊天室正符合了这类实时性要求,使用Node.js集成Socket.IO可轻松搭建一个`Web Socket`服务器,http://socket.io/ 开发聊天室教程:http://socket.io/get-started/chat/
* 方面开发命令行工具  
* HTTP代理服务器  
  类似于`Nginx`,`Apache`

<a id="markdown-3-使用nodejs实现反向代理" name="3-使用nodejs实现反向代理"></a>
# 3. 使用Node.js实现反向代理

反向代理通常有以下几种应用场景:
* 使静态资源与动态资源分离
* 实现AJAX跨域访问
* 搭建统一服务网关接口

<a id="markdown-4-实践" name="4-实践"></a>
# 4. 实践

```
# 安装cnpm
npm install -g cnpm --registry=http://r.cnpmjs.org

```
