---
title: Nginx
date: 2018-01-02 14:08:11
categories: [微服务]
---


<!-- TOC -->

- [1. 资料](#1-资料)
- [2. 简要记录](#2-简要记录)
- [3. 负载均衡配置](#3-负载均衡配置)
    - [3.1. 一般轮询规则](#31-一般轮询规则)
    - [3.2. 加权轮询](#32-加权轮询)
- [4. 细节](#4-细节)

<!-- /TOC -->


<a id="markdown-1-资料" name="1-资料"></a>
# 1. 资料

* https://raw.githubusercontent.com/nginx/nginx/master/conf/nginx.conf  (默认配置)
* https://github.com/nginx/nginx/blob/master/conf/fastcgi.conf (fastcgi配置)

<a id="markdown-2-简要记录" name="2-简要记录"></a>
# 2. 简要记录
```bash
负载均衡方法: 轮询,加权轮询,ip hash(避免前端用户的session在后端多个节点上共享的问题,问题是不能高可用)

# 使日志文件可写(其实还是sudo用户启动把)
sudo chmod -R 777 /var/log/nginx/

# 重读配置
sudo nginx -s reload

# 检查版本
nginx -v 

# 检查 配置文件(-c是指定配置文件)
sudo nginx -t -c  

# 配置自动调整worker process数量
worker_processes auto;

# 配置文件的引入
include file;

# 防止惊群
accept_mutex on | off;

# 最大连接数
worker_connections  1024;

# 日志相关
access_log path[format[buffer=size]];

# 超时时间
keepalive_timeout  65;

# 单连接请求数上线
keeplive_requests number;

# 默认根文件?
/usr/share/nginx/html/

# 块
全局

events {
    
}

http{
    server {  # 虚拟主机,无需为每个网站对应运行一组Nginx进程

        location { # 基于请求字符串进行匹配,对特定的请求进行处理

        }
    }
}
```

<a id="markdown-3-负载均衡配置" name="3-负载均衡配置"></a>
# 3. 负载均衡配置

<a id="markdown-31-一般轮询规则" name="31-一般轮询规则"></a>
## 3.1. 一般轮询规则

```
upstream backend
{
    server 192.168.1.2:80;
    server 192.168.1.3:80;
    server 192.168.1.4:80;
}

server
{
    listen 80;
    server_name www.myweb.com
    index index.html index.htm
    location / {
        proxy_pass http://backend;
        proxy_set_header Host &host;
    }
}

```


<a id="markdown-32-加权轮询" name="32-加权轮询"></a>
## 3.2. 加权轮询
```
基于上面

upstream backend
{
    server 192.168.1.2:80 weight=5;
    server 192.168.1.3:80 weight=2;
    server 192.168.1.4:80;
}
```



<a id="markdown-4-细节" name="4-细节"></a>
# 4. 细节

```
工作进程是由主进程生成的(使用了fork函数并有一个单项的管道)

```
