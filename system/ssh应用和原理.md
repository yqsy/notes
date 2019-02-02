---
title: ssh应用和原理
date: 2017-11-25 20:50:00
categories: [系统底层]
---

<!-- TOC -->

- [1. 资料](#1-资料)
- [2. ssh梳理](#2-ssh梳理)
- [3. 中间人攻击](#3-中间人攻击)

<!-- /TOC -->

<a id="markdown-1-资料" name="1-资料"></a>
# 1. 资料


* http://www.ruanyifeng.com/blog/2011/12/ssh_remote_login.html (SSH 阮一峰)
* https://en.wikipedia.org/wiki/Public-key_cryptography (公钥加密)
* https://en.wikipedia.org/wiki/Secure_Shell (维基解释)
* http://blog.chinaunix.net/uid-21854925-id-3082425.html (ssh详细登陆流程)
* http://blog.csdn.net/brandohero/article/details/8475244 (ssh安全远程登录的身份认证原理)
* https://tlanyan.me/ssh-shadowsocks-prevent-man-in-middle-attack/
* https://security.stackexchange.com/questions/1599/what-is-the-difference-between-ssl-vs-ssh-which-is-more-secure (What is the difference between SSL vs SSH?)


```
      SSL              SSH
+-------------+ +-----------------+
| Nothing     | | RFC4254         | Connection multiplexing
+-------------+ +-----------------+
| Nothing     | | RFC4252         | User authentication
+-------------+ +-----------------+
| RFC5246     | | RFC4253         | Encrypted data transport
+-------------+ +-----------------+
```


<a id="markdown-2-ssh梳理" name="2-ssh梳理"></a>
# 2. ssh梳理

加密
```
      3des-cbc         REQUIRED          three-key 3DES in CBC mode
      blowfish-cbc     OPTIONAL          Blowfish in CBC mode
      twofish256-cbc   OPTIONAL          Twofish in CBC mode,
                                         with a 256-bit key
      twofish-cbc      OPTIONAL          alias for "twofish256-cbc"
                                         (this is being retained
                                         for historical reasons)
      twofish192-cbc   OPTIONAL          Twofish with a 192-bit key
      twofish128-cbc   OPTIONAL          Twofish with a 128-bit key
      aes256-cbc       OPTIONAL          AES in CBC mode,
                                         with a 256-bit key
      aes192-cbc       OPTIONAL          AES with a 192-bit key
      aes128-cbc       RECOMMENDED       AES with a 128-bit key
      serpent256-cbc   OPTIONAL          Serpent in CBC mode, with
                                         a 256-bit key
      serpent192-cbc   OPTIONAL          Serpent with a 192-bit key
      serpent128-cbc   OPTIONAL          Serpent with a 128-bit key
      arcfour          OPTIONAL          the ARCFOUR stream cipher
                                         with a 128-bit key
      idea-cbc         OPTIONAL          IDEA in CBC mode
      cast128-cbc      OPTIONAL          CAST-128 in CBC mode
      none             OPTIONAL          no encryption; NOT RECOMMENDED
```

完整性检查
```
      hmac-sha1    REQUIRED        HMAC-SHA1 (digest length = key
                                   length = 20)
      hmac-sha1-96 RECOMMENDED     first 96 bits of HMAC-SHA1 (digest
                                   length = 12, key length = 20)
      hmac-md5     OPTIONAL        HMAC-MD5 (digest length = key
                                   length = 16)
      hmac-md5-96  OPTIONAL        first 96 bits of HMAC-MD5 (digest
                                   length = 12, key length = 16)
      none         OPTIONAL        no MAC; NOT RECOMMENDED
```

Key Exchange Methods

```
      diffie-hellman-group1-sha1 REQUIRED
      diffie-hellman-group14-sha1 REQUIRED
```



<a id="markdown-3-中间人攻击" name="3-中间人攻击"></a>
# 3. 中间人攻击

貌似没有办法防御,主机的hostkey存放于`/etc/ssh`
