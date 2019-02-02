---
title: https
date: 2017-11-28 22:44:46
categories: [微服务]
---



<!-- TOC -->

- [1. 资源](#1-资源)
- [2. docker示例](#2-docker示例)
- [3. 免费签名](#3-免费签名)
- [4. https梳理](#4-https梳理)
- [5. 中间人攻击](#5-中间人攻击)
- [6. 所有文件后缀的含义](#6-所有文件后缀的含义)
- [7. 使用certbot获取证书](#7-使用certbot获取证书)
- [docker proxy  https -> http](#docker-proxy--https---http)

<!-- /TOC -->


<a id="markdown-1-资源" name="1-资源"></a>
# 1. 资源

* https://en.wikipedia.org/wiki/HTTPS (wiki)
* http://www.ituring.com.cn/book/1734 (HTTPS权威指南)
* https://www.zhihu.com/question/21518760/answer/19698894 (解释的很生动) 
* https://www.nginx.com/resources/wiki/start/topics/examples/SSL-Offloader/ (nginx 配置)
* http://nginx.org/en/docs/http/configuring_https_servers.html (nginx如何配置)
* https://developers.google.com/web/fundamentals/security/encrypt-in-transit/enable-https (说明)
* https://www.nginx.com/blog/nginx-https-101-ssl-basics-getting-started/ (https入门)
* http://nginx.org/en/docs/http/ngx_http_ssl_module.html (nginx官方文档配置)
* https://certbot.eff.org/ (这个好像可以直接生成证书)
* https://segmentfault.com/a/1190000005797776 (cerbot快速入门)
* https://hub.docker.com/r/certbot/certbot/ (docker)
* https://www.v2ex.com/t/365967 (简单的实践)
* https://www.zhihu.com/question/21518760/answer/19698894 (消耗的服务器资源)

<a id="markdown-2-docker示例" name="2-docker示例"></a>
# 2. docker示例

* https://github.com/jwilder/nginx-proxy (默认只EXPOSE80端口,需要反向443)
* https://github.com/JrCs/docker-letsencrypt-nginx-proxy-companion
* https://github.com/fatk/docker-letsencrypt-nginx-proxy-companion-examples
* https://github.com/SteveLTN/https-portal
* https://hub.docker.com/r/steveltn/https-portal/

<a id="markdown-3-免费签名" name="3-免费签名"></a>
# 3. 免费签名

* https://letsencrypt.org/
* https://bruceking.site/2017/07/12/how-letsencrypt-works/ (letsencrypt原理)

<a id="markdown-4-https梳理" name="4-https梳理"></a>
# 4. https梳理

* http://blog.csdn.net/is0501xql/article/details/8158327 (SSL协议详解)
* http://www.ruanyifeng.com/blog/2011/08/what_is_a_digital_signature (公钥私钥讲的很清楚)
* https://www.zhihu.com/question/52493697/answer/130813213 (这个还算清楚)


CA会给网站颁发一个证书,包括
* 证书用途
* 网站的公钥
* 网站的加密算法
* 网站的hash算法
* 证书到期时间

把证书做hash,再用ca的私钥加密,得到了数字签名.放在证书末尾一起给到网站.

* 浏览器请求网站,得到证书(会验证证书合法性)和数字签名,把数字签名用公钥解密得到hash值,再计算证书的hash值,相等认证成功
* 双方运行 Diffie Hellman 算法,协商master-key再推导出`session-key`,用于SSL数据流加密,一般用AES
* 以master-key推导出`hash-key`,用于数据完整性检查,一般有MD5,SHA
* 浏览器把http报文用hash key生成一个MAC,放在http报文后,然后用session-key加密所有数据,发送
* 服务器用session-key解密数据,然后用相同的算法计算MAC,如果MAC==MAC,则数据没有篡改

<a id="markdown-5-中间人攻击" name="5-中间人攻击"></a>
# 5. 中间人攻击

* https://www.zhihu.com/question/20744215 (什么是TLS中间人攻击,如何防范这类攻击)

<a id="markdown-6-所有文件后缀的含义" name="6-所有文件后缀的含义"></a>
# 6. 所有文件后缀的含义

* https://www.zhihu.com/question/29620953 


后缀:
* X.509 DER 编码(ASCII)的后缀是： .DER .CER .CRT
* X.509 PAM 编码(Base64)的后缀是： .PEM(也可能是key) .CER .CRT
* 私钥：.key
* 证书请求：.csr

```bash

# 从PEM装换到DER
openssl x509 -inform PEM -in fd.pem -outform DER -out fd.der

# 从DER转换到PEM
openssl x509 -inform DER -in fd.der -outform PEM -out fd.pem

```


<a id="markdown-7-使用certbot获取证书" name="7-使用certbot获取证书"></a>
# 7. 使用certbot获取证书

参考:
* https://certbot.eff.org/#debianstretch-nginx (官网)
* https://linuxstory.org/deploy-lets-encrypt-ssl-certificate-with-certbot/ (经验)

需要:
* 一个域名
* 一个公网IP

内网NAT是不可以的,必须要公网IP(电信不开放80 443)

```bash
mkdir -p ~/cert && cd ~/cert

docker run -it --name nginx1 \
    -v `pwd`/:/cert \
    -p 80:80 \
    -p 443:443 \
    nginx bash

apt-get update
apt-get install python-certbot-nginx -y

certbot  certonly \
    --agree-tos --standalone --installer nginx \
    -d yqsycloud.top -d www.yqsycloud.top \
    --email yqsy021@126.com

cd /cert
cp /etc/letsencrypt/keys/0000_key-certbot.pem ./
cp /etc/letsencrypt/csr/0000_csr-certbot.pem ./
cp /etc/letsencrypt/live/yqsycloud.top/fullchain.pem ./


# 证书只有90天有效期,继续获得
certbot renew
```


<a id="markdown-docker-proxy--https---http" name="docker-proxy--https---http"></a>
# docker proxy  https -> http

```bash
mkdir -p ~/env/testhttps && cd ~/env/testhttps

echo \
"[req]
prompt = no
distinguished_name = dn
req_extensions = ext
input_password = PASSPHRASE
[dn]
CN = localhost
emailAddress = yqsy021@126.com
O = Feisty Duck Ltd
L = London
C = GB
[ext]
subjectAltName = DNS:www.feistyduck.com,DNS:feistyduck.com
" > ./fd.cnf

openssl genpkey -algorithm RSA -pkeyopt rsa_keygen_bits:2048 -out default.key
openssl req -new -config fd.cnf -key default.key -out default.csr
openssl x509 -req -days 365 -in default.csr -signkey default.key -out default.crt

cp default.key test.top.key
cp default.crt test.top.crt

cp default.key www.test.top.key
cp default.crt www.test.top.crt

docker run -d --name nginx1 -e VIRTUAL_HOST=test.top,www.test.top nginx

docker run -d --name nginx-proxy1 -p 80:80 -p 443:443 \
    -v `pwd`/:/etc/nginx/certs \
    -v /var/run/docker.sock:/tmp/docker.sock:ro \
    jwilder/nginx-proxy
```

```bash
# 树莓派
docker pull braingamer/nginx-proxy-arm

docker run -d --name nginx1 -e VIRTUAL_HOST=test.top,www.test.top nginx

mkdir -p ~/env/testhttps && cd ~/env/testhttps

#... 证书

docker run -d --name nginx-proxy1 -p 80:80 -p 443:443 \
    -v `pwd`/:/etc/nginx/certs \
    -v /var/run/docker.sock:/tmp/docker.sock:ro \
    braingamer/nginx-proxy-arm
```
