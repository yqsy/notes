---
title: pic生成图片
date: 2017-12-12 07:35:15
categories: [coding]
---

<!-- TOC -->

- [1. 资源](#1-资源)
- [2. 使用](#2-使用)

<!-- /TOC -->



<a id="markdown-1-资源" name="1-资源"></a>
# 1. 资源

* http://liangshaocong.me/tool/unix-draw-tool-pic/


<a id="markdown-2-使用" name="2-使用"></a>
# 2. 使用

```bash
yum install texlive-epstopdf -y

pic ttcp.pic | groff | ps2eps > ttcp.eps
epstopdf ttcp.eps
```

https://github.com/chenshuo/recipes/blob/master/tpc/ttcp.pic
```
.PS
C: box invis "client"
line from C.s down 1.8
line right 0.04
line left 0.08 down 0.12
line right 0.04
line down 1

S: box invis "server" at C+(3,0)
line from S.s down 1.8
line right 0.04
line left 0.08 down 0.12
line right 0.04
line down 1

arrow from C.s-(0, 0.2) to S.s-(0, 0.4) "SessionMessage(num=1024, len=8192)" "" aligned

arrow from C.s-(0, 0.5) to S.s-(0, 0.7) "PayloadMessage(len=8192+4)" "" aligned thickness 1.5 width 0.08
arrow <- from C.s-(0, 1.0) to S.s-(0, 0.8) "Ack(=8192)" "" aligned
box invis "1     " at C.s-(0,0.5)

arrow from C.s-(0, 1.1) to S.s-(0, 1.3) "PayloadMessage(len=8192+4)" "" aligned thickness 1.5 width 0.08
arrow <- from C.s-(0, 1.6) to S.s-(0, 1.4) "Ack(=8192)" "" aligned
box invis "2     " at C.s-(0,1.1)

arrow from C.s-(0, 2.1) to S.s-(0, 2.3) "PayloadMessage(len=8192+4)" "" aligned thickness 1.5 width 0.08
arrow <- from C.s-(0, 2.6) to S.s-(0, 2.4) "Ack(=8192)" "" aligned
box invis "1024          " at C.s-(0,2.1)

box invis "......" at C.s-(-1.5, 1.82)
.PE
```

效果:
![](http://ouxarji35.bkt.clouddn.com/snipaste_20171212_073859.png)
