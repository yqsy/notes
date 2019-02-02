---
title: html5websocket权威指南
date: 2018-02-06 17:34:34
categories: [读书笔记]
---


<!-- TOC -->


<!-- /TOC -->


html5 websocket权威指南

http1.0 1.1 只能满足通信方式:从客户端到服务器，然后从服务器到客户端。

因为http是用于文档共享的。而不是丰富的交互性应用程序。而我们在桌面上习以为常的程序现在已经进入web


半双工协议。同一时刻流量只能单向流动。

每次只能发一个请求。下一个请求要等请求返回时才能发送。


解决方法是:http轮询，长轮询，流化。

长轮询，long polling 称为Comet, 反向AJAX,

前端AJAX得到数据后再次发送查询请求。

流化是客户端发送一个请求，服务器发送并维护一个持续更新和保持打开的开放响应，每当服务器有需要交付给客户端的信息时。它就更新响应。

但是连接一直保持打开。代理和防火墙可能缓存响应。导致信息交付的延迟增加。

websocket。全双工，双向，单socket.

websocket服务器的实现多种多样。例如Apache mod_pyweb-socket,jetty,Socket.IO和kaazing的WebSocket Gateway

如果只需要服务向其客户端广播或者推送消息，而不需要交互。那么使用html5的sse，Server-Sent Event.


WebRTC包含可以让浏览器相互之间实时通信的api.

格式

ws://echo.websocket.org

纯事件驱动。注册回调函数。


客户端用javascript即可访问，主流浏览器都支持。

在某种程度上，http的流行也造成了互联网的退化，浏览器能通过url寻找服务器资源，但是服务器却无法主动向客户端发送资源。


特性|TCP|HTTP|WebSocket
-|-|-|-
寻址|ip地址和端口|url|url
并发传输|全双工|半双工|全双工
内容|字节流|mime消息|文本和二进制消息
消息定界|否|是|是
连接定向|是|否|是



顺序，消息边界


osi设计时没有考虑互联网

* 物理
* 链路
* 网络
* 传输
* 会话
* 表示
* 应用

为互联网设计的tcp/ip协议模型只由4个层次组成:
* 链路
* 网络
* 传输
* 应用



握手初始于一个http请求，包含一个首标–upgrade: websocket

有哈希检验服务端是否支持websocket

以帧frame作为边界

很少有一个消息超过一个帧

协议支持扩展

xmpp，可扩展消息与现场处理协议，xml的流化

消息传递是一种架构风格，特征是在独立的组件之间发送异步消息，实现松耦合系统。

使用STOMP协议可以实现pub/sub

消息传播技术

队列:

任意数量生产者向队列发布消息，每条消息只能由一个客户端接收

主题:

向多个消费者传递消息的传播机制

ActiveMQ支持主题和队列。STOMP最初开发就是用于ActiveMQ.

一个新标准化的开放消息传递协议是AMQP。Advanced Message Queuing Protocol

* SNMP简单网络管理协议
* SOAP简单对象访问协议
* SMTP简单邮件传输协议

ESB Enterprise Service Bus在websocket的帮助下，可以安全地扩展到任何web设备上

使用websocket和远程帧缓冲remote framebuffer协议将vnc扩展到web上，

amqp
xmpp stomp
http websocket
tcp /tls


* 转发代理
* 透明代理
* 反向代理