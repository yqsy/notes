---
title: https权威指南.md
date: 2018-2-6 21:35:37
categories: [读书笔记]
---

<!-- TOC -->

- [1. 我的问题](#1-我的问题)
- [2. 层次](#2-层次)
- [3. ssl tls版本](#3-ssl-tls版本)
- [4. 对称加密算法列表](#4-对称加密算法列表)
- [5. 中间人攻击](#5-中间人攻击)
- [6. TLS](#6-tls)
    - [6.1. 抓包分析](#61-抓包分析)
- [7. 公钥基础设施](#7-公钥基础设施)
- [8. PKI攻击](#8-pki攻击)
- [9. HTTP和浏览器问题](#9-http和浏览器问题)
- [10. 部署](#10-部署)
- [11. 性能优化](#11-性能优化)
- [12. http严格传输安全](#12-http严格传输安全)
- [13. OpenSSL](#13-openssl)
- [14. 指令](#14-指令)
- [15. 配置apache](#15-配置apache)
- [16. 配置nginx](#16-配置nginx)

<!-- /TOC -->


<a id="markdown-1-我的问题" name="1-我的问题"></a>
# 1. 我的问题

* ssh如何做到安全？身份认证?  
  第一次信赖
* ssl/tls如何做到安全？身份认证?  
  证书 + 数字签名


<a id="markdown-2-层次" name="2-层次"></a>
# 2. 层次

所有连接到互联网的设备都有一个共同点，他们依赖安全套接字层(secure soccket layer, ssl) 和传输层安全(transport layer security,tls)

避免伪装攻击，ssl和tls依赖公钥基础设施，public key infrastructure,pki

x|x|x|x
-|-|-|-
7|应用层|应用数据|http/smtp/imap
6|表示层|数据表示，转换和加密|ssl和tls
5|会话层|多连接管理|–
4|传输层|包或流的可靠传输|TCP,UDP
3|网络层|网络节点间的路由和数据转发|IP,IPSEC
2|数据链路层|可靠的本地数据连接(lan)|以太网
1|物理层|直接物理数据连接|cat5


<a id="markdown-3-ssl-tls版本" name="3-ssl-tls版本"></a>
# 3. ssl tls版本

* ssl1没有发布过
* ssl2是失败的协议
* ssl3是重新设计的,沿用到了今天
* tls1.0与ssl3.0相差不大
* tls1.1仅仅修复了一些关键的安全问题
* tls1.2增加了对已验证加密的支持

<a id="markdown-4-对称加密算法列表" name="4-对称加密算法列表"></a>
# 4. 对称加密算法列表

对称加密又称私钥加密，是一种混淆算法，能够让数据在非安全通道上进行安全通信。


1. 对称加密

* 序列密码，密钥序列与明文序列进行异或,例如rc4
* 分组密码，世界上最流行的分组密码是高级加密标准(advanced encryption standard.AES)

相同字节长度输入，相同字节长度输出。

tls最后一字节表示填充长度。

2. 散列函数

将任意长度的输入转化成定长输出的算法。密码学散列函数需要有几个额外的特性:

抗原像性(单向性)给定一个散列，计算上无法构造出它的信息。

抗第二原像性(弱抗碰撞性)，给定一条消息和它的散列，计算上无法找到一条不同消息具有相同的散列

强抗碰撞性，计算上无法找到两条散列相同的消息


散列函数经常被称为指纹，消息摘要，或者简单称为摘要。

最广泛使用的是sha1，输出为160位。强度已经变弱，建议升级为sha256的变种。


3. 消息验证代码

散列函数仅在散列与数据本身分开传输的条件下才能用于验证数据完整性。

当mac message authentication和密文一起发送时，对方就能确认消息并未遭到篡改。

hmac是将散列秘钥和信息以一种安全地方式交织在一起。


4. 分组密码模式

对分组密码的扩展，为了加密任意长度的数据。ECB,CBC,CFB,OFB,CTR,GCM


5. 非对称加密

非对称加密称为公钥加密，一个私钥是秘密的，另一个是公开的。  `加密对称加密算法的秘钥`

* 利用某人的公钥加密，只有对应的私钥能够解开消息
* 如果某人用私钥加密，那么任何人都可以利用对应的公钥解开信息。不提供机密性，但可以用作数字签名。

速度非常慢。RSA是目前普遍部署的非对称加密算法。推荐强度是2048位。



6. 数字签名

digital signature

使用私钥加密过的数据就是签名。可以追加到文档中作为`身份验证`的依据

* 文档hash-> digest -> 私钥加密 -> signature 和文档一起发出去
* signature -> 公钥解密 -> digest == 文章hash?

有个问题是,会遭到中间人的攻击,伪造一对私钥和公钥,所以就有了CA certificate authority,为公钥做认证


7. 随机数生成

在密码学中,所有的安全性都依赖于生成随机数的质量.真正的随机数只能通过观测待定的物理处理器才能得到,没有的话,计算机将关注于收集少量的熵.(按键状态,鼠标移动)

<a id="markdown-5-中间人攻击" name="5-中间人攻击"></a>
# 5. 中间人攻击

* 如果只是监听，称之为被动网络攻击
* 如果攻击者主动改变数据流，或者影响双方对话，我们称之为主动网络攻击(类似运营商给http页面加js)


攻击手段:
* ARP欺骗，mac-ip  
* WPAD劫持，自动获取http代理  
* DNS劫持  
* DNS缓存中毒  
* BGP路由劫持  

<a id="markdown-6-tls" name="6-tls"></a>
# 6. TLS
秘钥交换使用的rsa秘钥用于解密过去所有的会话。其他秘钥不存在这个问题。被称为支持前向保密。

了解tls最好的方式是观察现实中的网络流量。

tls四个核心子协议:握手协议，秘钥规格变更协议。应用数据协议，警报协议


握手流程:

1. 完整的握手，对服务器进行身份验证
2. 恢复之前的会话采用简短握手
3. 对客户端和服务器都进行身份验证握手

完整的握手:

1. 交换各自支持的功能，对需要连接参数达成一致。
2. 验证出示的证书。使用其他方式进行身份验证
3. 对将用于保护的共享主秘钥达成一致
4. 验证握手消息并未被第三方团体修改

证书环节携带服务器X.509证书链。

秘钥交换:

会话安全性取决于主秘钥的48字节的共享秘钥。秘钥交换的目的是计算另一个值。即预主秘钥。

1. RSA

可以使攻击者解码所有加密数据，只要能够访问服务器的私钥。rsa秘钥交换正被慢慢被其他支持前向保密(forward secrecy)所代替

2. DHE_RSA

临时Diffie-Hellman 密钥交换是一种构造完备的算法.有点支持前向保密,缺点是执行缓慢

3. ECDHE_RSA和ECDHE_ECDSA

临时椭圆曲线Diffie-Hellman (ephemeral elliptic curve Diffie-Hellman)密钥交换.提供前向保密.

---
1. RSA密钥交换

是客户端生成预主秘钥(session-key?)使用服务器公钥加密后,发给服务器,服务器解密后就可以得到预主秘钥

缺点是:加密预主密钥的服务器公钥,一般会保持多年不变.

2. Deiffie-Hellman 密钥交换

是一种密钥协定的协议,它使两个团体在不完全的信道上生成共享密钥成为可能.

主动攻击者可以劫持通信信道,冒充对端.所以DH密钥通常与身份验证联合使用.

现实问题:

>>>
    1. DH参数的安全性,不安全的参数,将对会话造成伤害
    2. 参数强度不够,许多库和服务器默认使用弱DH参数,1024,768都是非安全的,2048或以上更安全

3. 椭圆曲线Diffie-Hellman密钥交换

密钥交换原理与DH相似,但它的核心使用了不同的数学基础 


---

身份验证

为了避免重复执行密码操作造成巨大开销,身份验证与密钥交换紧紧捆绑在一起.证书的公钥作为RSA密钥交换的加密密钥


---

加密

TLS可以使用各种方法加密数据, 3DES,AES,ARIR,CAMELLIA,RC4或者SEED等算法,最为广泛的加密算法是AES.

支持3种加密类型:
* 序列密码  
 计算MAC值->加密明文和MAC生成密文
* 分组加密  
 计算MAC值->构造填充(通常是16字节的整数倍)->生成与分组大小一致的不可预期的分组向量->CBC分组模式加密明文,MAC,和填充->将IV和密文一起发送
* 已验证的加密  
......


---
密码套件

密码套件是一组选定的加密基元和其他参数,它可以精确定义如何实现安全,大致由以下属性定义

密钥套件都倾向于使用较长的描述性名称:

TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256

* ECDHE 密钥交换
* RSA 身份认证
* AES 算法
* 128 强度
* GCM 模式
* SHA256 MAC或PRF

列表:  
https://www.iana.org/assignments/tls-parameters/tls-parameters.xhtml

对于身份认证,强度主要依靠证书.更确切地说是证书中的密钥长度和签名算法.RSA密钥交换的强度也依靠证书.

<a id="markdown-61-抓包分析" name="61-抓包分析"></a>
## 6.1. 抓包分析

1. tcp握手
2. client hello (带域名的)
3. server hello Cipher Suite: TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256 (0xc02f)
4. Certificate, Certificate Status, Server Key Exchange, Server Hello Done (证书和签名)
5. Client Key Exchange, Change Cipher Spec, Encrypted Handshake Message (公钥加密得到session-key)
6. New Session Ticket, Change Cipher Spec, Encrypted Handshake Message

<a id="markdown-7-公钥基础设施" name="7-公钥基础设施"></a>
# 7. 公钥基础设施

如何与从未谋面的人进行沟通?如何存储和吊销密钥?如何让现实世界数以百万计的服务器,几十亿人和设备之间安全通信?

PKI就是互联网公钥基础设施,的目标就是实现不同成员在不见面的情况下进行安全通信,采用的模型是基于可信的第三方机构,也就是证书颁发机构(certification authority 或 certificate authority ,CA)签发的证书

* 订阅人
* 登记机构 (registration authority,RA)完成一些证书签发的相关管理工作
* 证书颁发机构 (certification authority, CA) 我们都信任的证书办法机构
* 信赖方 (relying party)是指证书使用者

互联网公钥基础设施可以追溯到X.509.

证书是一个包含公钥,订阅人相关信息以及证书颁发者数字签名的文件,也就是一个让我们可以交换,存储和使用公钥的壳.

PEM是DER使用Base64编码后的ASCII编码格式,ASN.1比较复杂,一般不需要与它打交道

---
证书字段:
* 版本
* 序列号
* 签名算法
* 颁发者
* 有效期
* 使用者
* 公钥

扩展:
* 使用者可选名称
* 名称约束
* 基础约束
* 密钥用法
* 扩展密钥用法
* 证书策略
* CRL分发点
* 颁发机构信息访问
* 使用者密钥标识符
* 授权密钥标识符

<a id="markdown-8-pki攻击" name="8-pki攻击"></a>
# 8. PKI攻击

* 天生缺陷: 所有的CA都可以在不经域名所有者同一的情况下去给任意域名签发证书.中间人攻击??
* 证书碰撞?MD5/SHA-1 ?? 证书碰撞为啥会导致安全问题?CA是验证数字签名的吗?
* 签发不安全的证书(512位密钥)
* windows Internet Explorer支持Web代理自动发现机制(wpad).可以获得受害者https的流量.
* https怎么代理?代理难道不是安全的吗?我觉得代理只能获得主机名!


<a id="markdown-9-http和浏览器问题" name="9-http和浏览器问题"></a>
# 9. HTTP和浏览器问题

HTTP Cookie是一种用来在客户端保存少量数据的扩展机制.对于要设置的每个Cookie,服务器必须制定一对名称和值,以及描述其作用范围和生命周期的元数据.


中间人攻击证书

* 利用安全漏洞
* 伪造证书 (破解一个1024位的私钥只需要100W美元,需要将近1年时间)
* 自签名证书

为什么有这么多无效证书

* 网站的证书和域名不匹配
* 域名覆盖范围不足 www.example.com 和 example.com也要覆盖
* 自签名证书和私有CA.不适合在公开场合使用,因为这类证书无法简单并可靠地与中间人攻击的证书区分开.
* 设备使用的证书,很多设备有基于Web的管理.被制造出来的时候,域名和IP无法确定,无法安装有效的证书.
* 过期的证书
* 错误的配置

<a id="markdown-10-部署" name="10-部署"></a>
# 10. 部署

TLS支持3种算法:

* DSA (被排除,密钥最大只能到1024位)
* RSA ,基本上所有的TLS部署都会支持RSA算法.但是RSA在2048的密钥下,比ECDSA密钥在安全性上更弱且性能更差.
* ECDSA, 是未来的选择.256位密钥比RSA算法快2倍.如果是3072位,在相同加密强度下,ECDSA性能要快6倍.

密钥管理:

* 保证私钥的秘密性(当作最重要的资产来保护)
* 仔细选择随机数生成器 (确保有足够的熵)
* 保护密钥的密码 (避免拷贝时密钥内容被泄漏,要知道从现代文件系统里正真删除数据变得越来越难了)
* 不要随意共享密钥
* 定期更新密钥
* 安全存储密钥,如果密钥时中间或者私有CA用来签发证书的,那丢了很严重(HSM设备解决)

证书类型:

* 域名验证 (domain validated, DV)  (自动,最便宜)
* 组织验证 (organization validated, OV) (需要验证域名拥有者的公司信息)
* 扩展验证 (extended validation, EV)

证书主机名:

请遵守一个简单的规则:只要有一个DNS解析指向你的TLS服务器,就务必保证你的证书包括了这个DNS域名.

证书共享:

* 签发包含所有需要域名的证书: www.example.com example.com log.example.com
* 签发泛域名证书: *.example.com和example.com

签名算法:

对于新申请的证书,要确保使用SHA256或更好的签名算法.

证书链:

实际上我们在部署TLS服务器时真正需要配置的是证书链(certificate chain).一个证书链就是能溯源到一个可信根证书的有序证书列表.

前向保密:

TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256

如上密码套件中的ECDHE是密钥交换算法,不要使用RSA作为密钥交换,因为不能做到前向保密.

性能:

GCM套件是最快的,因此你无需在安全性和速度之间作出取舍.

AES有优势,现在处理器的特殊指令集可以支持AES加速,因此AES在实践使用中要快得多.



<a id="markdown-11-性能优化" name="11-性能优化"></a>
# 11. 性能优化

会话缓存

客户端和服务器在首次建立连接并创建SSL会话时协商好传输密钥,在后续连接中就可以直接复用相同的传输密钥.

复杂体系结构

分布式会话缓存  
使用负载均衡的流量保持功能,保证同一客户端总是被分发到集群中的相同节点  


* 慢启动对https的握手是有很大影响的.可以配置在连接空闲时禁用慢启动.
* 长连接 (chrome 维持连接默认时间是300秒)
* SPDY 可以复用连接. 唤醒了HTTP2.0.
* TCP fast open 时从TCP握手去除一个往返的优化技术


---

TLS优化:

* 使用尽可能少的证书.证书链包含太多证书有可能会导致TCP初始拥塞窗口溢出.你的证书链里面最好有两个证书:一个服务器的证书和一个签发CA的证书
* 提供完整的证书链.不然客户端会花费几秒去查询
* 使用椭圆曲线证书链.私钥长度使用更少位.
* 小心同一张证书绑定过多域名.每增加一个域名都会增加证书的大小.



<a id="markdown-12-http严格传输安全" name="12-http严格传输安全"></a>
# 12. http严格传输安全

http请求重定向至https还有问题:会被截获http明文信息.解决方法是配置HSTS.通过在加密的HTTP响应中包含Strict-Transport-Security头实现网站TSTS

---

强大的部署清单

* 确保Strict-Transport-Security头是在全部主机名的所有加密响应上发出去的
* 确保在根域名上启用HSTS
* 确定指向你的网站的全部路径
* 一开始先用一个短暂的过期时间作为临时策略
* 重定向所有HTTP通信到HTTPS.这将确保用户始终在第一次访问时收到HSTS指令
* 修改你的网站使每个主机名向根域名提交一个请求
* 如果在你的网站面前有一个反向代理,在代理级别集中配置HSTS策略时一个加分项

<a id="markdown-13-openssl" name="13-openssl"></a>
# 13. OpenSSL

OpenSSL项目时安全套接字层(secure sockets layer, SSL)和传输层安全(transport layer security,TLS)协议的一个实现,是大家共同努力开发出的代码可靠,功能齐全,商业级别的开源工具集.


密钥和证书管理

整个过程包括3个步骤  
1. 生成强加密的私钥
2. 常见证书签名申请(centificate signing request, CSR)并且发送给CA
3. 在你的Web服务器上安装CA提供的证书


<a id="markdown-14-指令" name="14-指令"></a>
# 14. 指令

```bash
# 连接SSL服务
openssl s_client -connect www.feistyduck.com:443

# 指定可信证书
openssl s_client -connect www.feistyduck.com:443 -CAfile /etc/ssl/certs/ca-certificates.crt

# 测试支持的密码套件
openssl s_client -connect www.feistyduck.com:443 -cipher RC4-SHA

# 测试会话复用
echo | openssl s_client -connect www.feistyduck.com:443 -reconnect

# 测试心脏出血
openssl s_client -connect www.feistyduck.com:443 -tlsextdebug

```


<a id="markdown-15-配置apache" name="15-配置apache"></a>
# 15. 配置apache

```bash
# 配置服务器私钥
SSLCertificateKeyFile conf/server.key

# 配置服务器证书
SSLCertificateFile conf/server.crt

# 配置CA提供的中间证书链，当服务器是自签名证书时不需要这个指令
SSLCertificateChainFile conf/chain.pem
```

<a id="markdown-16-配置nginx" name="16-配置nginx"></a>
# 16. 配置nginx

```bash
# 私钥
ssl_certificate_key server.key;

# 证书：服务器证书在最前面，后面是所有必要的中间证书，不需要根证书
ssl_certificate server.crt;

```

