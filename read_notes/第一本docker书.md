---
title: 第一本docker书
date: 2017-12-3 15:57:44
categories: [读书笔记]
---

<!-- TOC -->

- [1. p1-简介](#1-p1-简介)
- [2. p2-容器提供了什么](#2-p2-容器提供了什么)
    - [2.1. 提供一个简单、轻量的建模方式](#21-提供一个简单轻量的建模方式)
    - [2.2. 职责的逻辑分离](#22-职责的逻辑分离)
    - [2.3. 快速、高效的开发生命周期](#23-快速高效的开发生命周期)
    - [2.4. 鼓励使用面向服务的架构](#24-鼓励使用面向服务的架构)
- [3. p3-Docker组件](#3-p3-docker组件)
- [4. p8-Docker的技术组件](#4-p8-docker的技术组件)
- [5. p9-Docker社区/资源](#5-p9-docker社区资源)
- [6. p16-Centos安装Docker](#6-p16-centos安装docker)
- [7. p28-Docker守护进程](#7-p28-docker守护进程)
- [8. p31-Docker图形用户界面](#8-p31-docker图形用户界面)
- [9. p33-查看Docker程序是否存在](#9-p33-查看docker程序是否存在)
- [10. p35-运行第一个容器](#10-p35-运行第一个容器)
- [11. p41-获取容器内部的日志](#11-p41-获取容器内部的日志)
- [12. p42-查看容器内的进程](#12-p42-查看容器内的进程)
- [13. p43-在容器内部运行进程](#13-p43-在容器内部运行进程)
- [14. p44-自动重启容器](#14-p44-自动重启容器)
- [15. p45-获取容器的更多信息](#15-p45-获取容器的更多信息)
- [16. p46-解密docker工作原理的目录](#16-p46-解密docker工作原理的目录)
- [17. p47-一次删除所有容器=](#17-p47-一次删除所有容器)
- [18. p51-列出镜像](#18-p51-列出镜像)
- [19. p58-使用Dockerfile](#19-p58-使用dockerfile)
- [20. p67-Dockerfile和构建缓存](#20-p67-dockerfile和构建缓存)
- [21. p68-基于缓存构建的模板](#21-p68-基于缓存构建的模板)
- [22. p68-查看新镜像](#22-p68-查看新镜像)
- [23. p69-从新镜像启动容器](#23-p69-从新镜像启动容器)
- [24. p72-Dockerfile指令](#24-p72-dockerfile指令)
- [25. p84-将镜像推送到Docker Hub](#25-p84-将镜像推送到docker-hub)
- [26. p90-运行自己的Docker Registry](#26-p90-运行自己的docker-registry)
- [27. p92-其他可选的Registry服务](#27-p92-其他可选的registry服务)
- [28. p96-搭建静态测试网站](#28-p96-搭建静态测试网站)
- [29. p98-使用宿主机的目录作为卷](#29-p98-使用宿主机的目录作为卷)
- [30. p102-执行宿主机上的程序](#30-p102-执行宿主机上的程序)
- [31. p104-构建Redis镜像和容器](#31-p104-构建redis镜像和容器)
- [32. p106-Docker自己的网络栈](#32-p106-docker自己的网络栈)
- [33. p110-ip地址硬编码的问题](#33-p110-ip地址硬编码的问题)
- [34. p116-Docker用于持续集成](#34-p116-docker用于持续集成)
- [35. p126-Jenkins作业自动执行](#35-p126-jenkins作业自动执行)
- [36. p132-其他选择](#36-p132-其他选择)
- [37. p138-什么是卷](#37-p138-什么是卷)
- [38. 备份我的dokuwiki](#38-备份我的dokuwiki)
- [39. p142-简易的负载均衡](#39-p142-简易的负载均衡)
- [40. p150-多容器的应用栈(nodejs,redis,elk示范)](#40-p150-多容器的应用栈nodejsrediselk示范)
- [41. p167-使用Fig编配Docker](#41-p167-使用fig编配docker)
- [42. p193-配合Consul,在Docker里运行分布式服务](#42-p193-配合consul在docker里运行分布式服务)
- [43. p202-其他编配工具和组件](#43-p202-其他编配工具和组件)

<!-- /TOC -->



配套源代码:
  * https://github.com/turnbullpress/dockerbook-code

<a id="markdown-1-p1-简介" name="1-p1-简介"></a>
# 1. p1-简介
在计算世界中，容器拥有一段漫长且传奇的历史。容器与管理程序虚拟化（hypervisor
vitualization, HV ) 有所不同，管理程序虚拟化通过中间层将一台或多台独立的机器虚拟运行
于物理硬件之上，而容器则是直接运行在操作系统内核之上的用户空间。因此，容器虚拟化
也被称为“操作系统级虚拟化”， **容器技术可以让多个独立的用户空间运行在同一台宿主机上。**


可以参考王垠所说的,好像有点道理

```
说白了，Docker的原理就是建立一些目录，把系统文件和相关库代码拷贝进去，然后chroot，这样你的代码在里面运行的时候，就以为自己独占一个Linux系统。
```

reference: 
  * http://www.yinwang.org/blog-cn/2016/03/27/docker
  * https://en.wikipedia.org/wiki/Chroot

尽管有诸多局限性，容器还是被广泛部署于各种各样的应用场合。在超大规模的多租户
服务部署、轻量级沙盒以及对安全要求不太高的隔离环境中，容器技术非常流行。**最常见的
一个例子就是“权限隔离监牢” （chroot jail), 它创建一个隔离的目录环境来运行进程。如果
权限隔离监牢中正在运行的进程被入侵者攻破，入侵者便会发现自己“身陷囹圄”， 因为权
限不足被困在容器创建的目录中，无法对宿主机进行进一步的破坏。**

对Docker 来说，它得益于现代Linux 内核特性，如**控件组（control group)**、**命名
空间（namespace)** 技术，容器和宿主机之间的隔离更加彻底，容器有**独立的网络和存储栈**，
还拥有自己的资源管理能力，使得同一台宿主机中的多个容器可以友好地共存。

容器经常被认为是精益技术，因为容器需要的开销有限。和传统的虚拟化以及半虚拟化
(paravirtualization) 相比，**容器运行不需要模拟层（emulation layer) 和管理层（hypervisor
layer)，** 而是使用操作系统的系统调用接口。这降低了运行单个容器所需的开销，也使得宿
主机中可以运行更多的容器。

<a id="markdown-2-p2-容器提供了什么" name="2-p2-容器提供了什么"></a>
# 2. p2-容器提供了什么

Docker 在虚拟化的容器执行环境中增加了一个应用程序部署引擎。该引擎的目标就是提供一个轻量、快速的环境，能够运行开发者的程序，并方便高效地将程序从开发者的笔记本部署到测试环境，然后再部署到生产环境Docker 极其简洁，它所需的全部环境只是一台仅仅安装了兼容版本的Linux 内核和二进制文件最小限的宿主机。

<a id="markdown-21-提供一个简单轻量的建模方式" name="21-提供一个简单轻量的建模方式"></a>
## 2.1. 提供一个简单、轻量的建模方式
Docker 上手非常快，用户只需要几分钟，就可以把自己的程序“Docker 化"（Dockerize )。
Docker 依赖于“写时复制”（copy-on-write ) 模型，使修改应用程序也非常迅速，可以说达
到了“随心所至，代码即改”的境界。

随后，就可以创建容器来运行应用程序了。大多数Docker 容器只需不到1 秒钟即可启
动。由于去除了管理程序的开销，**Docker 容器拥有很高的性能**，同时同一台宿主机中也可
以运行更多的容器，使用户可以尽可能充分地利用系统资源。

<a id="markdown-22-职责的逻辑分离" name="22-职责的逻辑分离"></a>
## 2.2. 职责的逻辑分离
便用Docker, **开发人员只需要关心容器中运行的应用程序**，而运**维人员只需要关心如
何管理容器**。Docker 设计的目的就是要加强开发人员写代码的开发环境与应用程序要部署
的生产环境的一致性，从而降低那种“开发时一切都正常，肯定是运维的问题”的风险。

<a id="markdown-23-快速高效的开发生命周期" name="23-快速高效的开发生命周期"></a>
## 2.3. 快速、高效的开发生命周期
Docker 的目标之一就是缩短代码从开发、测试到部署、上线运行的周期，让你的应用
程序具备**可移植性，易于构建，并易于协作。**


<a id="markdown-24-鼓励使用面向服务的架构" name="24-鼓励使用面向服务的架构"></a>
## 2.4. 鼓励使用面向服务的架构
。Docker **推荐单个容器只运行一个应用程
序或进程**，这样就形成了一个分布式的应用程序模型，在这种模型下**，应用程序或服务都可
以表示为一系列内部互联的容器，从而使分布式部署应用程序，扩展或调试应用程序都变得
非常简单**，同时也提高了程序的内省性。


<a id="markdown-3-p3-docker组件" name="3-p3-docker组件"></a>
# 3. p3-Docker组件

Docker 客户端和服务器  
Docker 是一个客户-服务器（C/S) 架构的程序。Docker 客户端只需向Docker 服务器或
守护进程发出请求，服务器或守护进程将完成所有工作并返回结果。**Docker 提供了一个命
令行工具docker 以及一整套RESTfUl API®** 。你可以在同一台宿主机上运行Docker 守护进
程矛卩客户端，也可以从本地的Docker 客户端连接到运行在另一台宿主机上的远程Docker 守
护进程。


Docker 镜像  
镜像是构建Docker 世界的基石。用户基于镜像来运行自己的容器。镜像也是Docker 生
命周期中的“构建”部分。镜像是基于联合（Union) 文件系统的一种层式的结构， 由一系
列指令一步一步构建出来。例如：

  * 添加一个文件
  * 执行一个命令
  * 打开一个端口

Registry  
Docker 用Registry 来保存用户构建的镜像。Registry 分为公共和私有两种。**Docker 公司
运营的公共Registry 叫做Docker Hub。**用户可以在Docker Hub®注册账号® ，分享并保存自
己的镜像。

**你甚至可以架设自己的私有Registry** 。具体方法我们会在第4 章中讨论。私有Registry
可以受到防火墙的保护，将镜像保存在防火墙后面，以满足一些组织的特殊需求。

Docker 容器  
Docker 可以帮你构建和部署容器，你只需要把自己的应用程序或服务打包放进容器即
可。我们刚刚提到，容器是基于镜像启动起来的，容器中可以运行一个或多个进程。我们可
以认为， **镜像是Docker 生命周期中的构建或打包阶段**，而**容器则是启动或执行阶段。**

总结起来，Dockei容器就是：
  * 一个镜像格式
  * 一系列标准的操作
  * 一个执行环境

Docker 借鉴了标准集装箱的概念。标准集装箱将货物运往世界各地，Docker 将这个模
型运用到自己的设计哲学中，唯一不同的是：集装箱运输货物，而Dockei•运输软件。
每个容器都包含一个软件镜像，也就是容器的“货物”，而且与真正的货物一样，容器
里的软件镜像可以进行一些操作。例如，镜像可以被**创建、启动、关闭、重启以及销毁**

使用Docker, 我们可以快速构建**一个应用程序服务器、一个消息总线、一套实用工具、
一个持续集成（continuous integration, CI) 测试环境或者任意一种应用程序、服务或工具。**
我们可以在本地构建一个完整的测试环境， 也可以为生产或开发快速复制一套复杂的应用程
序栈。可以说，Docker 的应用场景相当广泛。

<a id="markdown-4-p8-docker的技术组件" name="4-p8-docker的技术组件"></a>
# 4. p8-Docker的技术组件
Docker 可以运行于任何安装了现代Linux 内核的x64 主机上。我们**推荐的内核版本是3.8**
或者更高。Docker 的开销比较低，可以用于服务器、台式机或笔记本。它包括以下几个部分。

一个原生的Linux 容器格式，Docker 中称为libcontainer ，或者很流行的容器平台
lxc® 。libcontainer 格式现在是Docker 容器的默认格式。

Linux 内核的命名空间（namespace) ® ，用于隔离文件系统、进程和网络。

  * 文件系统隔离：每个容器都有自己的root 文件系统
  * 进程隔离：每个容器都运行在自己的进程环境中
  * 网络隔离：容器间的虚拟网络接口和IP 地址都是分开的
  * 资源隔离和分组：使用cgroups® (即control group，Linux 的内核特性之一）将CPU和内存之类的资源独立分配给每个Docker 容器。
  * 写时复制 : 文件系统都是通过写时复制创建的，这就意味着文件系统是分层的、快速的，而且占用的磁盘空间更小
  * 日志：容器产生的**STDOUT、STDERR和STDIN**这些IO流都会被收集并记入日志，用来进行日志分析和故障排错。
  * 交互式shell: 用户可以创建一个伪tty 终端，将其连接到STDIN, 为容器提供一个交互式的shell。


<a id="markdown-5-p9-docker社区资源" name="5-p9-docker社区资源"></a>
# 5. p9-Docker社区/资源

  * Docker 官方主页（http://www.docker.com/ )
  * Docker Hub ( http://hub.docker.com)
  * Docker 官方博客（http://blog.docker.com/)
  * Docker 官方文档（http://docs.docker.com/ )
  * Docker 快速入门指南（ http://www.docker.com/tryit/)
  * Docker 的GitHub 源代码（https://github.com/docker/docker)
  * Docker Forge (https://github.com/dockerforge): 收集了各种Docker 工具、组件和服务。
  * Docker 由P件列表（https://groups.google.eom/forum/#lforum/docker-user)。
  * Docker 的IRC 频道（irc.freenode.net )。
  * Docker 的Twitter 主页（http://twitter.com/docker)
  * Docker 的StackOverflow 问答主页（http://stackoverflow.com/search?q=docker)。
  * Docker 官网（http://www.docker.com/ )


<a id="markdown-6-p16-centos安装docker" name="6-p16-centos安装docker"></a>
# 6. p16-Centos安装Docker

内核  
确认是否安装了3.8 或更高的内核版本。
```
uname -a
```

检查Device Mapper   
我们这里使用Device Mapper 作为Docker 的存储驱动，为Docker 提供存储能力。**在Red
Hat 企业版Linux、CentOS 6 或Fedora Core 19 及更高版本宿主机中，应该也都安装了Device
Mapper**, 不过我们还是需要确认一下

```
ls -l /sys/class/misc/device-mapper
grep device-mapper /proc/devices
```

安装  
```
yum -y install docker
```
或  
```
curl https://get.docker.io/ | sudo sh
```

启动和开机启动

在Red Hat 企业版Linux 6  
```
service docker start
service docker enable
```

在Red Hat 企业版7
```
systemctl start docker
systemctl enable docker
```

<a id="markdown-7-p28-docker守护进程" name="7-p28-docker守护进程"></a>
# 7. p28-Docker守护进程
当Docker 软件包安装完毕后，默认会立即启动Docker 守护进程。**守护进程监听
/var/run/docker.sock 这个Unix 套接字文件**，来获取来自客户端的Docker 请求。如
果系统中存在名为docker 的用户组的话，Docker 则会将该套接字文件的所有者设置为该
用户组


修改绑定的网络接口  
```
sudo /usr/bin/docker -d -H tcp://0.0.0.0:2375
```

如果不想指定-H  
指定DOCKER_HOST  
```
export DOCKER_HOST="tcp://0.0.0.0:2375"
```


绑定到非默认的套接字  
```
sudo /usr/bin/docker -d -H unix://home/docker/docker.sock
```

将Docker守护进程绑定到多个地址  
```
sudo /usr/bin/docker -d -H tcp://0.0.0.0:2375 -H unix://home/docker/docker.sock
```

启动和停止Docker  
```
service docker stop
service docker start
```


<a id="markdown-8-p31-docker图形用户界面" name="8-p31-docker图形用户界面"></a>
# 8. p31-Docker图形用户界面

 * Shipyard: 提供了通过管理界面来管理各种Docker 资源（包括容器、镜像、宿主机等）的功能
 * DockerUI：DockerUI 是一个可以与Docker Remote API 交互的Web 界面
 * maDocker: maDocker 是釆用NodeJS 和Backbone 编写的一个Web UI，还处于早期幵发阶段


<a id="markdown-9-p33-查看docker程序是否存在" name="9-p33-查看docker程序是否存在"></a>
# 9. p33-查看Docker程序是否存在
```
sudo docker info
```

<a id="markdown-10-p35-运行第一个容器" name="10-p35-运行第一个容器"></a>
# 10. p35-运行第一个容器
```
docker run -i -t ubuntu /bin/bash
```

  * -i 标志保证容器中STDIN是开启的
  * -t 标志告诉Docker要为创建的容器分配一个伪tty终端.

这样,新创建的容器才能提供一个交互式shell,若要在命令行下创建一个我们能与之进行交互的容器,而不是一个运行后台服务的容器,则这两个参数已经是最基本的参数了.


启动到bash  
```
docker run -t -i jamtur01/static_web:v1
```

```
  -d, --detach         Detached mode: run command in the background
  --detach-keys        Override the key sequence for detaching a container
  --help               Print usage
  -i, --interactive    Keep STDIN open even if not attached
  --privileged         Give extended privileges to the command
  -t, --tty            Allocate a pseudo-TTY
  -u, --user           Username or UID (format: <name|uid>[:<group|gid>])
```

<a id="markdown-11-p41-获取容器内部的日志" name="11-p41-获取容器内部的日志"></a>
# 11. p41-获取容器内部的日志

获取全部的日志  
```
docker logs dokuwiki
```

获取日志的某一个片断  
```
docker logs --tail 10 dokuwiki
```

<a id="markdown-12-p42-查看容器内的进程" name="12-p42-查看容器内的进程"></a>
# 12. p42-查看容器内的进程
```
docekr top dokuwiki
```

<a id="markdown-13-p43-在容器内部运行进程" name="13-p43-在容器内部运行进程"></a>
# 13. p43-在容器内部运行进程
```
docker exec -d dokuwiki touch /etc/new_config_file
```

  * 这里的-d标志表明需要运行一个后台进程

在容器内运行交互命令  

捕捉了容器的会话
```
docker exec -t -i dokuwiki /bin/bash
```

<a id="markdown-14-p44-自动重启容器" name="14-p44-自动重启容器"></a>
# 14. p44-自动重启容器
```
docker run --restart=always
```

<a id="markdown-15-p45-获取容器的更多信息" name="15-p45-获取容器的更多信息"></a>
# 15. p45-获取容器的更多信息
```
docker inspect dokuwiki
```

有选择地获取容器信息  
```
docker inspect --format='{{ .State.Running }}' dokuwiki
```

查看容器的ip地址  
```
docker inspect --format='{{ .NetworkSettings.IPAddress }}' dokuwiki
```

查看所有的ip地址  
```
docker inspect -f '{{.Name}} - {{.NetworkSettings.IPAddress }}' $(docker ps -aq)
```

查看多个容器  
```
docker inspect --format '{{.Name}} {{.State.Running}}' dokuwiki my-proxy
```


<a id="markdown-16-p46-解密docker工作原理的目录" name="16-p46-解密docker工作原理的目录"></a>
# 16. p46-解密docker工作原理的目录
```
/var/lib/docker
```

<a id="markdown-17-p47-一次删除所有容器" name="17-p47-一次删除所有容器"></a>
# 17. p47-一次删除所有容器=
```
docker rm `docker ps -a -q`
```

<a id="markdown-18-p51-列出镜像" name="18-p51-列出镜像"></a>
# 18. p51-列出镜像
```
docker images
```

拉取镜像  
```
docker pull ubuntu
```

拉取了ubuntu仓库中的所有内容


拉取某一个版本的镜像  
```
docker pull fedora:20
```

查找镜像  
```
docker search puppet
```


<a id="markdown-19-p58-使用dockerfile" name="19-p58-使用dockerfile"></a>
# 19. p58-使用Dockerfile
reference: 
  * https://docs.docker.com/engine/reference/builder/
  * https://github.com/kstaken/dockerfile-examples

现在我们并**不推荐使用docker commit 命令**，而应该使用更灵活、更强大的Dockerfile 来构建Docker 镜像。

```
# 1. Version: 0.0.1
FROM ubuntu:14.04
MAINTAINER James Turnbull "james@example.com"
RUN apt-get update
RUN apt-get install -y nginx
RUN echo 'Hi, I am in your container' \
    > /usr/share/nginx/html/index.html
EXPOSE 80
```

  * 每个Dockerf ile 的第一条指令都应该是FROiyLFROM指令指定一个己经存在的镜像，后续指令都将基于该镜像进行，这个镜像被称为基础镜像（base iamge)。
  * 接着指定了MAINTAINER 指令，这条指令会告诉Docker 该镜像的作者是谁，以及作者的电子邮件地址。这有助于标识镜像的所有者和联系方式。
  * 默认情况下，RUN 指令会在shel丨里使用命令包装器/bin/sh -c 来执行
  * 出于安全的原因，Docker 并不会自动打开该端口，而是需要你在使用docker run 运行容器时来指定需要打开哪些端口

基于Dockerfile构建镜像  
```
docker build -t="jamtur01/static_web" .
```

也可以指定标签  
如果没有制定任何标签，Docker 将会自动为鏡像设置一个latest标签。
```
docker build -t="jamtur01/static_web:v1" .
```

从Git仓库构建Docker镜像  
```
docker build -t="jamtur01/static_web:v1" \
git@github.com:jamtur01/docker-static_web
```

这里Docker假设在这个Git 仓库的根目录下存在Dockerfile 文件。

<a id="markdown-20-p67-dockerfile和构建缓存" name="20-p67-dockerfile和构建缓存"></a>
# 20. p67-Dockerfile和构建缓存
然而，有些时候需要确保构建过程不会使用缓存。比如，**如果己经缓存了前面的第3步，
即apt-getupdate,那么Docker将不会再次刷新APT包的缓存。这时你可能需要取得
每个包的最新版本。要想略过缓存功能，可以使用dockerbuild的--no-cache标志**
```
docker build --no-cache -t="jamtur01/static_web"
```

<a id="markdown-21-p68-基于缓存构建的模板" name="21-p68-基于缓存构建的模板"></a>
# 21. p68-基于缓存构建的模板
```
FROM ubuntu:14.04
MAINTAINER James Turnbull "james@example.com"
ENV REFRESHED_AT 2014-07-01
RUN apt-get -qq update
```

这个例子里，我通过ENV 指令来设置了一个名为REFRESHED_AT 的环境变量，**这个环境变量用来表
明该镜像模板最后的更新时间**。最后，我使用了RUN 指令来运行apt-get -qq update
命令。**该指令运行时将会刷新APT 包的缓存，用来确保我们能将要安装的每个软件包都更
新到最新版本。**

就是包的时间戳必须在REFRESHED_AT时间之后,不然就检查一下是否是最新,然后更新到最新

<a id="markdown-22-p68-查看新镜像" name="22-p68-查看新镜像"></a>
# 22. p68-查看新镜像
```
docker images jamtur01/static_web
```

查看镜像是如何构建的  
```
docker history jamtur01/static_web
```

<a id="markdown-23-p69-从新镜像启动容器" name="23-p69-从新镜像启动容器"></a>
# 23. p69-从新镜像启动容器
```
docker run -d -p 80 --name static_web jamtur01/static_web nginx -g "daemon off;"
```

  * -p 该标志用来控制Docker 在运行时应该公开哪些网络端口给外部（ 宿主机)。

  * Docker 可以在宿主机上随机选择一个位于49153 65535 的一个比较大的端口号来映射到容器中的80 端口上。

  * 可以在Docker 宿主机中指定一个具体的端口号来映射到容器中的80 端口上。

查看port  
```
docker port static_web 80
```

指定宿主机的端口号  
```
docker run -d -p 80:80 --name static_web jamtur01/static_web nginx -g "daemon off;"
```


<a id="markdown-24-p72-dockerfile指令" name="24-p72-dockerfile指令"></a>
# 24. p72-Dockerfile指令

使用CMD指令  

```
CMD ["bin/true"]
```

**CMD指令用于指定一个容器启动时要运行的命令。**这有点儿类似于RUN指令，只是RUN
指令是指定镜像被构建时要运行的命令，而CMD是指定容器被启动时要运行的命令。


运行命令放在数组结构中  
需要注意的是，要运行的命令是存放在一个数组结构中的。这将告诉Docker按指定的原
样来运行该命令。然也可以不使用数组儿时指定CMD指令，这时候Docker会在指定的
命令前加上/bin/sh-cc这在执行该命令的时候可能会导致意料之外的行为，**所以
Docker推荐一直使用以数组语法来设置要执行的命令.**

docker run命令可以覆盖CMD指令  
如果我们在Dockerfile里指定了CMD指令，而同时在dockerrun命令行中也指定了要运行的命令，命令行中指
定的命令会覆盖Dockerfile中的CMD指令。



ENTRYPOINT  
有时候，我们希望容器会按照我们想象的那样去工作，
这时候CMD就不太合适了。而ENTRYPOINT指令提供的命令则不容易在启动容器时被覆盖。
实际上，**dockerrun命令行中指定的任何参数都会被当做参数再次传递给ENTRYPOINT指
令中指定的命令.
**
```
ENTRYPOINT ["/usr/sbin/nginx"]
```

```
ENTRYPOINT ["/usr/sbin/nginx", "-g", "daemon off;"]
```


覆盖ENTRYPOINT  
如果确实需要，你也可以在运行时通过dockerrun的--entrypoint标志覆盖ENTRYPOINT指令.


WORKDIR  
我们可以使用该指令为Dockerfile中后续的一系列指令设置工作目录,也可以为最终的容器设置工作目录.

```
WORID /opt/webapp/db
RUN bundle install
WORKDIR /opt/webapp
ENTRYPOINT [ "rackup" ]
```

-w标志在运行时覆盖工作目录  
```
docker run -ti -w /var/log ubuntu pwd
```

ENV  
ENV 指令用来在镜像构建过程中设置环境变量
```
ENV RVM_PATH /home/rvm/
```

添加ENV前缀后执行
```
RVM_PATH=/home/rvm/ gem install unicorn
```

在其他Dockerfile指令中使用环境变量  =
也可以使用docker run 命令行的-e 标志来传递环境变量。
```
ENV TARGET_DIR /opt/app
WORKDIR $TARGET_DIR
```

传递环境变量  
```
docker run -ti -e "WEB_PORT=8080" ubuntu env
```


USER  
USER 指令用来指定该镜像会以什么样的用户去运行
```
USER nginx
```

也可以在 docker run 命令中通过-u选项来覆盖该指令的值
```
docker run -u
```


VOLUME  

VOLUME 指令用来向基于镜像创建的容器添加卷。一个卷是可以存在于一个或者多个容
器内的特定的目录，这个目录可以绕过联合文件系统，并提供如下共享数据或者对数据进行
持久化的功能。

  * 卷可以在容器间共享和重用。

  * 一个容器可以不是必须和其他容器共享卷。

  * 对卷的修改是立时生效的。

  * 对卷的修改不会对更新镜像产生影响。

  * 卷会一直存在直到没有任何容器再使用它。

卷功能让我们可以将数据（如源代码）、数据库或者其他内容添加到镜像中而不是将这些内容提交到镜像中， 并且允许我们在多个容器间共享这些内容。我们可以利用此功能来测试容器和内部的应用程序代码，管理日志，或者处理容器内部的数据库。

```
VOLUME ["/opt/project"]
```
这条指令将会为基于此镜像创建的任何容器创建一个名为/opt/project 的挂载点。我们也可以通过指定数组的方式指定多个卷.

```
VOLUME ["/opt/project", "/data"]
```

ADD  
ADD指令用来将构建环境下的文件和目录复制到镜像中。比如，在安装一个应用程序时。ADD指令需要源文件位置和目的文件位置两个参数

```
ADD software.lic /opt/application/software.lic
```

如果目的地址以/ 结尾，那么Docker 就认为源位置指向的是目录。如果目的地址不是以/ 结尾，那么Docker 就认为源位置指向的是文件。


自动解压缩的魔法  
```
ADD latest.tar.gz /var/www/workpress/
```

这条命令会将归档文件latest.tar.gz解开到/var/www/wordpress/目录下

COPY  
COPY 指令非常类似于ADD, 它们根本的不同是COPY 只关心在构建上下文中复制本地
文件，而不会去做文件提取（extraction) 和解压（decompression) 的工作.

```
COPY conf.d/ /etc/apache2/
```


ONBUILD  
```
ONBUILD ADD . /app/src
ONBUILD RUN cd /app/src & make
```

上面的代码将会在创建的镜像中加入ONBUILD触发器,ONBUILD指令可以在镜像上运行dockerinspect命令来查看

```
FROM ubuntu:14.04
MAINTAINER James Turnbull "james@example.com"
RUN apt-get update
RUN apt-get install -y apache2
ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2
ONBUILD ADD . /var/www/
EXPOSE 80
ENTRYPOINT ["/usr/sbin/apache2"]
CMD ["-D", "FOREGOUND"]
```
在新构建的镜像中包含一条ONBUILD 指令，该指令会使用ADD 指令将构建环境所在的目录下的内容全部添加到镜像中的/var/www/ 目录下。我们可以轻而易举地将这个Docker file 作为一个通用的Web应用程序的模板，可以基于这个模板来构建Web应用程序



<a id="markdown-25-p84-将镜像推送到docker-hub" name="25-p84-将镜像推送到docker-hub"></a>
# 25. p84-将镜像推送到Docker Hub
```
docker push static_web
```

提示**Impossible to push a "root" repository .**

出什么问题了？我们尝试将镜像推送到远程仓库Static_web，但是Docker认为这是
一个root仓库。root仓库是由Docker公司的团队管理的，因此会拒绝我们的推送请求。


自动构建  
除了从命令行构建和推送镜像，DockerHub还允许我们定义自动构建（Automated
Builds)。为了使用自动构建，我们只需要将GitHub或BitBucket中含有Dockerfile文
件的仓库连接到DockerHub即可。**向这个代码仓库推送代码时，将会触发一次镜像构建活
动并创建一个新镜像。在之前该工作机制也被称为可信构建（Trusted Build)。**


删除本地镜像  
```
docker rmi jamtur01/static_web
```

删除所有镜像  
```
docker rmi `docker images -a -q`
```

<a id="markdown-26-p90-运行自己的docker-registry" name="26-p90-运行自己的docker-registry"></a>
# 26. p90-运行自己的Docker Registry
有时候我们可能希望构建和存储包含不想被公开的信息或数据的镜像。这时候我们有以下两种选择。

  * 利用Docker Hub上的私有仓库

  * 在防火墙后面运行你自己的Registry

从容器运行Registry  
```
docker run -p 5000:5000 registry
```

测试新Registry  

使用新Registry为镜像打标签
```
docker tag 22d47c8cb6e5 docker.example.com:5000/jamtur01/static_web
```

为镜像打完标签之后,就能通过docker push命令将它推送到新的Registry中去了.

```
docker push docker.example.com:5000/jamtur01/static_web
```

这个镜像就被提交到了本地的Registry中,并且可以将其使用docker run 命令构建新容器.

从本地Registry构建新的容器  
```
docker run -t -i docker.examp
le.com:5000/jamtur01/
```

这是在防火墙后面部署自己的Docker Registry 的最简单的方式。我们并没有解释如何配
置或者管理Registty。如果想深入了解如何配置认证和管理后端镜像存储方式，以及如何管
S Registry 等详细信息，可以在Docker Registry 文档查看完整的配置和部署说明。


<a id="markdown-27-p92-其他可选的registry服务" name="27-p92-其他可选的registry服务"></a>
# 27. p92-其他可选的Registry服务

Quary  
Quay服务提供了私有的Registry 托管服务，允许你上传公共的或者私有的容器。目前
它提供了免费的无限制的公共仓库托管服务，如果想托管私有仓库，它还提供了一系列的可
伸缩计划。Quay 最近被CoreOS® 收购了，并会被整合到他们的产品中去。


<a id="markdown-28-p96-搭建静态测试网站" name="28-p96-搭建静态测试网站"></a>
# 28. p96-搭建静态测试网站
```
FROM ubuntu:16.04
MAINTAINER James Turnbull "james@example.com"
ENV REFRESHED_AT 2014-06-01

RUN apt-get -qq update && apt-get -qq install nginx

RUN mkdir -p /var/www/html/website
ADD nginx/global.conf /etc/nginx/conf.d/
ADD nginx/nginx.conf /etc/nginx/

EXPOSE 80
```

<a id="markdown-29-p98-使用宿主机的目录作为卷" name="29-p98-使用宿主机的目录作为卷"></a>
# 29. p98-使用宿主机的目录作为卷
```
docker run -d -p 80 --name website \
-v $PWD/website:/var/www/html/website \
jamtur01/nginx nginx
```

<a id="markdown-30-p102-执行宿主机上的程序" name="30-p102-执行宿主机上的程序"></a>
# 30. p102-执行宿主机上的程序
```
FROM ubuntu:14.04
MAINTAINER James Turnbull james@example.com
ENV REFRESHED_AT 2014-06-01

RUN apt-get update
RUN apt-get -y install ruby ruby-dev build-essential redis-tools
RUN gem install --no-rdoc --no-ri sinatra json redis

RUN mkdir -p /opt/webapp

EXPOSE 4576

CMD [ "/opt/webapp/bin/webapp" ]
```

修改宿主机的可执行程序  
```
chmod +x $PWD/webapp/bin/webapp
```

映射磁盘,启动容器  
```
docker run -d -p 4576 --name webapp \
-v $PWD/webapp:/opt/webapp jamtur01/sinatra
```

<a id="markdown-31-p104-构建redis镜像和容器" name="31-p104-构建redis镜像和容器"></a>
# 31. p104-构建Redis镜像和容器
```
FROM ubuntu:14.04
MAINTAINER James Turnbull james@example.com
ENV REFRESHED_AT 2014-06-01
RUN apt-get update
RUN apt-get -y install redis-server redis-tools

EXPOSE 6379
ENTRYPOINT ["/usr/bin/redis-server"]
CMD []
```

构建Redis镜像  
```
docker build -t jamtur01/redis .
```

启动Redis容器  
```
docker run -d -p 6479 --name redis jamtur01/redis
```

在Ubuntu上安装redis-tools包  
```
apt-get -y install redis-tools
```

确认Redis服务器工作是否正常  
```
redis-cli -h 127.0.0.1 -p 49161
```

<a id="markdown-32-p106-docker自己的网络栈" name="32-p106-docker自己的网络栈"></a>
# 32. p106-Docker自己的网络栈
在安装Docker 时，会创建一个新的网络接口， 名字是docker0。每个Docker 容器都
会在这个接口上分配一个IP 地址。

dockerO接口有符合RFC1918的私有IP地址，范围是172.16~172.30。接口本身
的地址172.17.42.1是这个Docker网络的网关地址，也是所有Docker容器的网关地址。

Docker 会默认使用172.17.X.X 作为子网地址，除非已经有别人占用了这个子网。如果
这个子网被占用了，Docker 会在172.16~172.30 这个范围内尝试创建子网。

接口docker0 是一个虚拟的以太网桥，用于连接容器和本地宿主网络.

虚拟子网  
Docker每创建一个容器就会创建一组互联的网络接口。这组接口就像管道的两端（就
是说，从一端发送的数据会在另一端接收到）。这组接口其中一端作为容器里的ethO接口，
而另一端统一命名为类似vethec6a这种名字，作为宿主机的一个端口。**你可以把veth
接口认为是虚拟网线的一端。这个虚拟网线一端插在名为docker0的网桥上，另一端插到
容器里。通过把每个veth*接口绑定到docker0网桥，Docker创建了一个虚拟子网，这个
子网由宿主机和所有的Docker容器共享。**


```
[root@vultr ~]# ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq state UP qlen 1000
    link/ether 56:00:00:5e:55:15 brd ff:ff:ff:ff:ff:ff
    inet 45.76.104.154/23 brd 45.76.105.255 scope global dynamic eth0
       valid_lft 71775sec preferred_lft 71775sec
    inet6 fe80::5400:ff:fe5e:5515/64 scope link 
       valid_lft forever preferred_lft forever
3: docker0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP 
    link/ether 02:42:b6:07:b3:a8 brd ff:ff:ff:ff:ff:ff
    inet 172.17.0.1/16 scope global docker0
       valid_lft forever preferred_lft forever
    inet6 fe80::42:b6ff:fe07:b3a8/64 scope link 
       valid_lft forever preferred_lft forever
27: veth03c17c5@if26: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue master docker0 state UP 
    link/ether 02:25:58:3c:8a:85 brd ff:ff:ff:ff:ff:ff link-netnsid 1
    inet6 fe80::25:58ff:fe3c:8a85/64 scope link 
       valid_lft forever preferred_lft forever
37: veth70f074b@if36: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue master docker0 state UP 
    link/ether 72:fb:94:de:b9:eb brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet6 fe80::70fb:94ff:fede:b9eb/64 scope link 
       valid_lft forever preferred_lft forever
41: veth678308a@if40: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue master docker0 state UP 
    link/ether 2e:29:de:b8:3b:d0 brd ff:ff:ff:ff:ff:ff link-netnsid 3
    inet6 fe80::2c29:deff:feb8:3bd0/64 scope link 
       valid_lft forever preferred_lft forever
```

```
[root@vultr ~]# docker inspect -f '{{.Name}} - {{.NetworkSettings.IPAddress }}' $(docker ps -aq)
/dokuwiki - 172.17.0.4
/utksmbcc - 172.17.0.3
/my-proxy - 172.17.0.2
```

example my-proxy  
```
root@0da6b43b3cbf:/# ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
36: eth0@if37: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default 
    link/ether 02:42:ac:11:00:02 brd ff:ff:ff:ff:ff:ff
    inet 172.17.0.2/16 scope global eth0
       valid_lft forever preferred_lft forever
    inet6 fe80::42:acff:fe11:2/64 scope link 
       valid_lft forever preferred_lft forever
```

iptables  
```
[root@vultr ~]# iptables -t nat -L -n
Chain PREROUTING (policy ACCEPT)
target     prot opt source               destination         
PREROUTING_direct  all  --  0.0.0.0/0            0.0.0.0/0           
PREROUTING_ZONES_SOURCE  all  --  0.0.0.0/0            0.0.0.0/0           
PREROUTING_ZONES  all  --  0.0.0.0/0            0.0.0.0/0           
DOCKER     all  --  0.0.0.0/0            0.0.0.0/0            ADDRTYPE match dst-type LOCAL

Chain INPUT (policy ACCEPT)
target     prot opt source               destination         

Chain OUTPUT (policy ACCEPT)
target     prot opt source               destination         
OUTPUT_direct  all  --  0.0.0.0/0            0.0.0.0/0           
DOCKER     all  --  0.0.0.0/0           !127.0.0.0/8          ADDRTYPE match dst-type LOCAL

Chain POSTROUTING (policy ACCEPT)
target     prot opt source               destination         
MASQUERADE  all  --  172.17.0.0/16        0.0.0.0/0           
POSTROUTING_direct  all  --  0.0.0.0/0            0.0.0.0/0           
POSTROUTING_ZONES_SOURCE  all  --  0.0.0.0/0            0.0.0.0/0           
POSTROUTING_ZONES  all  --  0.0.0.0/0            0.0.0.0/0           
MASQUERADE  all  --  0.0.0.0/0            0.0.0.0/0           
MASQUERADE  tcp  --  172.17.0.2           172.17.0.2           tcp dpt:80

Chain DOCKER (2 references)
target     prot opt source               destination         
RETURN     all  --  0.0.0.0/0            0.0.0.0/0           
DNAT       tcp  --  0.0.0.0/0            0.0.0.0/0            tcp dpt:80 to:172.17.0.2:80

Chain OUTPUT_direct (1 references)
target     prot opt source               destination         

Chain POSTROUTING_ZONES (1 references)
target     prot opt source               destination         
POST_public  all  --  0.0.0.0/0            0.0.0.0/0           [goto] 
POST_public  all  --  0.0.0.0/0            0.0.0.0/0           [goto] 

Chain POSTROUTING_ZONES_SOURCE (1 references)
target     prot opt source               destination         

Chain POSTROUTING_direct (1 references)
target     prot opt source               destination         

Chain POST_public (2 references)
target     prot opt source               destination         
POST_public_log  all  --  0.0.0.0/0            0.0.0.0/0           
POST_public_deny  all  --  0.0.0.0/0            0.0.0.0/0           
POST_public_allow  all  --  0.0.0.0/0            0.0.0.0/0           

Chain POST_public_allow (1 references)
target     prot opt source               destination         

Chain POST_public_deny (1 references)
target     prot opt source               destination         

Chain POST_public_log (1 references)
target     prot opt source               destination         

Chain PREROUTING_ZONES (1 references)
target     prot opt source               destination         
PRE_public  all  --  0.0.0.0/0            0.0.0.0/0           [goto] 
PRE_public  all  --  0.0.0.0/0            0.0.0.0/0           [goto] 

Chain PREROUTING_ZONES_SOURCE (1 references)
target     prot opt source               destination         

Chain PREROUTING_direct (1 references)
target     prot opt source               destination         

Chain PRE_public (2 references)
target     prot opt source               destination         
PRE_public_log  all  --  0.0.0.0/0            0.0.0.0/0           
PRE_public_deny  all  --  0.0.0.0/0            0.0.0.0/0           
PRE_public_allow  all  --  0.0.0.0/0            0.0.0.0/0           

Chain PRE_public_allow (1 references)
target     prot opt source               destination         

Chain PRE_public_deny (1 references)
target     prot opt source               destination         

Chain PRE_public_log (1 references)
target     prot opt source               destination         
```

<a id="markdown-33-p110-ip地址硬编码的问题" name="33-p110-ip地址硬编码的问题"></a>
# 33. p110-ip地址硬编码的问题
```
redis-cli -h 172.17.0.18
```

虽然第一眼看上去这是让容器互联的一个好方案，但可惜的是，这种方法有两个大问题：
**第一，要在应用程序里对Redis 容器的IP 地址做硬编码；第二，如果重启容器，Docker 会
改变容器的IP 地址.**


启动另一个Redis容器  
没有暴露端口!
```
docker run -d -name redis jamtur01/redis
```

让Docker容器互连  
```
docker run -p 4567 --name webapp --link redis:db -t -i \
-v $PWD/webapp:/opt/webapp jamtur01/sinatra \
/bin/bash
```

这次，使用了一个新的标志一link。--link标志创建了两个容器间的父子连接。这
个标志需要两个参数：一个是要连接的容器名字，另一个是连接后容器的别名。**这个例子中，
我们把新容器连接到redis容器，并使用db作为别名。**别名让我们可以访问公开的信息，
而无须关注底层容器的名字。连接让父容器有能力访问子容器，并且把子容器的一些连接细
节分享给父容器，这些细节有助于配置应用程序并使用这个连接。

连接也能得到一些安全上的好处。注意到启动Redis 容器时，并没有使用-p 标志公开
Redis 的端口。因为不需要这么做。通过把容器连接在一起，可以让父容器直接访问任意子
容器的公开端口（比如， 父容器webapp 可以连接到子容器redis 的6379 端口）。更妙的
是，只有使用一link 标志连接到这个容器的容器才能连接到这个端口。**容器的端口不需要
对本地宿主机公开，现在我们己经拥有一个非常安全的模型。通过这个安全模型，就可以限
制容器化应用程序的被攻击面，减少应用暴露的网络。**


再开两个容器连接redis  
```
docker run -p 4567 --name webapp2 --link redis:db
docker run -p 4567 --name webapp3 --link redis:db
```

被连接的容器必须运行在同一个Docker 宿主机上。不同Docker 宿主机上运行的容器无法连接。


webapp的/etc/hosts文件  
```
cat /etc/hosts

172.17.0.31 db
```

```
ping db
64 bytes from db (172.17.0.31): icmp_seq=l ttl=64 time=0. 623 ms
```

查看环境变量  
```
env

DB_NAME=/webapp/db
DB_P0RT_6379_TCP_P0RT=6379
DB_PORT=tcp://172.17.0.31:6379
DB_PORT_6379_TCP=tcp:172.17.0.31:6379
DB_ENV_RE_REFRESHED_AT=2014-06-01
DB_PORT_6379_TCP_ADDR=172.17.0.31
DB_PORT_6379_TCP_PROTO=tcp
```

口以看到不少环境变量，其中一些以DB开头。Docker在连接webapp和redis容器
时，自动创建了这些以DB开头的环境变量。以DB开头是因为DB是创建连接时使用的别名。

这些自动创建的环境变量包含以下信息.

  * 子容器的名字。
  * 容器里运行的服务所使用的协议、IP 和端口号。
  * 容器里运行的不同服务所指定的协议、IP 和端口号。
  * 容器里由Docker 设置的环境变量的值。


web服务器与redis数据库的简单框架  

用于演示Web 应用程序栈的例子终于写完了，这个Web 应用程序栈由以下几部分组成
  * 一个运行Sinatra 的Web 服务器容器。
  * 一个Redis 数据库容器。
  * 这两个容器间的一个安全连接。

可以很容易把这个概念扩展到别的应用程序栈，并用其在本地开发中做复杂的管理，比如:
  * Wordpress、HTML、CSS 和JavaScript
  * Ruby on Rails
  * Django 和Flask
  * Node.js
  * Play ! 
  * 你喜欢的其他框架

<a id="markdown-34-p116-docker用于持续集成" name="34-p116-docker用于持续集成"></a>
# 34. p116-Docker用于持续集成
Dockei很擅长快速创建和处理一个或多个容器。这个能力显然可以为持续集成测试这
个概念提供帮助。在测试场景里，你需要频繁安装软件，或者部署到多台宿主机上，运行测
试，再清理宿主机为下一次运行做准备。

在持续集成环境里，每天要执行好几次安装并分发到宿主机的过程。这为测试生命周期
增加了构建和配置开销。打包和安装也消耗了很多时间，而且这个过程很恼人，尤其是需求
变化频繁或者需要复杂、耗时的处理步骤进行清理的情况下。

Docker 让部署以及这些步骤和宿主机的清理变得开销很低。为了演示这一点，我们将
使用Jenkins CI构建一个测试流水线：首先，构建一个运行Docker 的Jenkins 服务器。**为了
更有意思些，我们会让Docker 递归地运行在Docker 内部。这就和套娃一样！**


<a id="markdown-35-p126-jenkins作业自动执行" name="35-p126-jenkins作业自动执行"></a>
# 35. p126-Jenkins作业自动执行
**可以通过启用SCM轮询，让Jenkins作业自动执行。**它会在有新的改动签入Git仓库后，
触发自动构建。类似的自动化还可以通过提交后的钩子或者GitHub或者Bitbucket仓库的钩
子来完成。

自己的想法:

理想情况下,就是向仓库push一个提交之后,构建服务器的jenkins轮询到了修改,然后将其pull下来打包了一个docker容器,再推送到测试服务器


<a id="markdown-36-p132-其他选择" name="36-p132-其他选择"></a>
# 36. p132-其他选择
在Docker 的生态环境中， 持续集成和持续部署（CI/CD) 是很有意思的一部分。除了与
现有的Jenkins 这种工具集成，也有很多人直接使用Docker 来构建这类工具。

Drone  
Drone 是著名的基于Docker 开发的CI/CD 工具之一。它是一个SaaS 持续集成平台，可
以与GitHub、Bitbucket 和Google Code 仓库关联，支持各种语言，包括Python、Node.js 、
Ruby、Go 等。Drone 在一个Docker 容器内运行加到其中的仓库的测试集。

Shippable  
Shippable 是免费的持续集成和部署服务，基于GitHub 和Bitbucket。它非常快，也很轻
量，原生支持Docker.


<a id="markdown-37-p138-什么是卷" name="37-p138-什么是卷"></a>
# 37. p138-什么是卷
卷是在一个或多个容器中特殊指定的目录，卷会绕过联合文件系统，为持久化数据和共享数据提供几个有用的特性。

  * 卷可以在容器间共享和重用
  * 共享卷时不一定要运行相应的容器
  * 对卷的修改会直接在卷上反映出来
  * 更新镜像时不会包含对卷的修改
  * 卷会一直存在，直到没有容器使用它们

利用卷， 可以在不用提交镜像修改的情况下，向镜像里加入数据（如源代码、数据或者其他内容）， 并且可以在容器间共享这些数据。

卷在Docker宿主机的/var/lib/docker/volumes.

```
docker inspect -f "{{ .Config.Volumes }}" dokuwiki
```

应该是容器内部使用的目录把
```
"Volumes": {
    "/dokuwiki/conf/": {},
    "/dokuwiki/data/": {},
    "/dokuwiki/lib/plugins/": {},
    "/dokuwiki/lib/tpl/": {},
    "/var/log/": {}
},
```

dokuwiki的Dockerfile  
```
# 2. VERSION 0.1
# 3. AUTHOR:         Miroslav Prasil <miroslav@prasil.info>
# 4. DESCRIPTION:    Image with DokuWiki & lighttpd
# 5. TO_BUILD:       docker build -t mprasil/dokuwiki .
# 6. TO_RUN:         docker run -d -p 80:80 --name my_wiki mprasil/dokuwiki


FROM ubuntu:14.04
MAINTAINER Miroslav Prasil <miroslav@prasil.info>

# 7. Set the version you want of Twiki
ENV DOKUWIKI_VERSION 2017-02-19b
ENV DOKUWIKI_CSUM ea11e4046319710a2bc6fdf58b5cda86

ENV LAST_REFRESHED 12. August 2016

# 8. Update & install packages & cleanup afterwards
RUN DEBIAN_FRONTEND=noninteractive \
    apt-get update && \
    apt-get -y upgrade && \
    apt-get -y install wget lighttpd php5-cgi php5-gd php5-ldap php5-curl && \
    apt-get clean autoclean && \
    apt-get autoremove && \
    rm -rf /var/lib/{apt,dpkg,cache,log}

# 9. Download & check & deploy dokuwiki & cleanup
RUN wget -q -O /dokuwiki.tgz "http://download.dokuwiki.org/src/dokuwiki/dokuwiki-$DOKUWIKI_VERSION.tgz" && \
    if [ "$DOKUWIKI_CSUM" != "$(md5sum /dokuwiki.tgz | awk '{print($1)}')" ];then echo "Wrong md5sum of downloaded file!"; exit 1; fi && \
    mkdir /dokuwiki && \
    tar -zxf dokuwiki.tgz -C /dokuwiki --strip-components 1 && \
    rm dokuwiki.tgz

# 10. Set up ownership
RUN chown -R www-data:www-data /dokuwiki

# 11. Configure lighttpd
ADD dokuwiki.conf /etc/lighttpd/conf-available/20-dokuwiki.conf
RUN lighty-enable-mod dokuwiki fastcgi accesslog
RUN mkdir /var/run/lighttpd && chown www-data.www-data /var/run/lighttpd

EXPOSE 80
VOLUME ["/dokuwiki/data/","/dokuwiki/lib/plugins/","/dokuwiki/conf/","/dokuwiki/lib/tpl/","/var/log/"]

ENTRYPOINT ["/usr/sbin/lighttpd", "-D", "-f", "/etc/lighttpd/lighttpd.conf"]
```

<a id="markdown-38-备份我的dokuwiki" name="38-备份我的dokuwiki"></a>
# 38. 备份我的dokuwiki
reference:
https://hub.docker.com/r/mprasil/dokuwiki/

以后加上备份时间,并同步到dropbox之类的云盘.
```
docker run --rm --volumes-from dokuwiki \
-v $(pwd)/dokuwiki-backup:/backup ubuntu \
tar zcvf /backup/dokuwiki-backup.tar.gz /dokuwiki/data/ /dokuwiki/lib/plugins/ /dokuwiki/conf/ /dokuwiki/lib/tpl/ /var/log/
```

<a id="markdown-39-p142-简易的负载均衡" name="39-p142-简易的负载均衡"></a>
# 39. p142-简易的负载均衡

  * 运行多个Apache 容器，这些容器都使用来自james_blog 容器的卷。在这些Apache容器前面加一个负载均衡器，我们就拥有了一个Web 集群。

  * 进一步构建一个镜像，这个镜像把用户提供的源数据复制（如通过git clone) 到卷里。再把这个卷挂载到从jamturol/jekyll镜像创建的容器。这就是一个可迁移的通用方案，而且不需要宿主机本地包含任何源代码。

  * 在上一个扩展基础上可以很容易为我们的服务构建一个Web 前端，这个服务用于从指定的源自动构建和部署网站。这样你就有一个完全属于自己的GitHub Pages 了。


<a id="markdown-40-p150-多容器的应用栈nodejsrediselk示范" name="40-p150-多容器的应用栈nodejsrediselk示范"></a>
# 40. p150-多容器的应用栈(nodejs,redis,elk示范)
在这个例子中，我们会构建一系列的镜像来支持部署多容器的应用。

  * 一个Node 容器，用来服务于Node 应用，这个容器会连接到：
  * 一个Redis 主容器， 用于保存和集群化应用状态，这个容器会连接到：
  * 两个Redis 备份容器，用于集群化应用状态。
  * 一个日志容器，用于捕获应用日志。

Node 应用会运行在一个容器里，后面会挂载以主从模式配置在多个容器里的Redis 集群。

```
git clone https://github.com/turnbullpress/dockerbook-code
```


<a id="markdown-41-p167-使用fig编配docker" name="41-p167-使用fig编配docker"></a>
# 41. p167-使用Fig编配Docker
reference: 

http://www.fig.sh/


<a id="markdown-42-p193-配合consul在docker里运行分布式服务" name="42-p193-配合consul在docker里运行分布式服务"></a>
# 42. p193-配合Consul,在Docker里运行分布式服务

reference:

https://github.com/turnbullpress/dockerbook-code/tree/master/code/7/consul


<a id="markdown-43-p202-其他编配工具和组件" name="43-p202-其他编配工具和组件"></a>
# 43. p202-其他编配工具和组件

Fleet和etcd  
Fleet 和etcd 由CoreOS® 团体发布。Fleet® 是一个集群管理工具，而etcd® 是一个高可用
性的键值数据库，用于共享配置和服务发现。Fleet 与systemd 和etcd —起，为Docker 容器
提供了集群管理和调度能力。可以把Fleet 看作是systemd 的扩展，只是不是工作在主机层
面上，而是工作在集群这个层面上。
它还是相对比较新的项目，目前CoreOS 已经正式发布稳定版。

Kubernetes  
Kubemetes® 是由Google 开源的容器集群管理工具。这个工具可以使用Docker 在多个宿
主机上分发并扩展应用程序。Kubernetes 主要关注需要使用多个容器的应用程序，如弹性分
布式微服务。
这个工具也是新出现的，缺少完整的文档。不过围绕这个工具的社区正在快速壮大。

Apache Mesos  
ApacheMesos® 项目是一个高可用的集群管理工具。Mesos 从Mesos0.20 开始，己经内
置了Docker 集成，允许利用Mesos 使用容器。Mesos 在一些创业公司里很流行，如著名的
Twitter 和AirBnB.

Helios  
Helios® 项目由SpotifV 的团队发布，是一个为了在全流程中发布和管理容器而设计的
Docker 编配平台。这个工具可以创建一个抽象的“作业”（job), 之后可以将这个作业发布
到一个或者多个运行Docker 的Helios 宿主机。

Centurion  
Centurion®是一个基于Docker 的部署工具，由New Relic 团队打造并开源。Centurion 从
Docker Registry 里找到容器，并在一组宿主机上使用正确的环境变量、主机卷映射和端口映
射来运行这个容器。这个工具的目的是帮助开发者利用Docker 做持续部署。

Libswarm  
Docker 公司自己的编配工具，集中围绕Libswarm®而开发。Libswarm 更像是一个库，
或者工具包，用来协助组织网络服务。这个库提供了在分布式系统上连接服务的标准接口。
这个项目开始时专注在为Docker 提供服务，不过现在己经是一个可以集成各种其他服务（包
括本节列出的服务）的服务库。

