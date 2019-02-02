---
title: 学习RSA
date: 2018-01-02 14:15:28
categories: [math]
---


<!-- TOC -->

- [1. 说明](#1-说明)
- [2. 质数](#2-质数)
- [3. 互质](#3-互质)
- [4. 积性函数](#4-积性函数)
- [5. 欧拉函数](#5-欧拉函数)
- [6. 同余](#6-同余)
- [7. 欧拉定理](#7-欧拉定理)
- [8. 模逆元](#8-模逆元)
- [9. 参考资料](#9-参考资料)

<!-- /TOC -->



<a id="markdown-1-说明" name="1-说明"></a>
# 1. 说明

RSA的过程:

1. 随意选择两个大的`质数`p和q,`N = pq`
2. 根据欧拉函数,求得`φ(N) = φ(p)φ(q) = (p-1)(q-1)`
3. 选择整数e, 满足`1 < e < φ(N)`,并且e与φ(N)互质
4. 求e关于φ(N)的模逆元,命名为d `(ed ≡ 1 (mod φ(N)))`

(N,e)是公钥. (N,d)是私钥. 

对于明文m:  

* 加密: c ≡ (m^e) (mod N)
* 解密: m ≡ (c^d) (mod N)

解密原理:

c^d ≡ (m^ed) (mod N)

已知: ed ≡ 1 (mod φ(N)) , 即 ed = 1 + h*φ(N). 由欧拉定理: a ^ φ(n) ≡ 1 (mod n) 得到:   
m^ed = m ^ (1 + h*φ(N)) = m * (m^φ(N))^h ≡ m(1)^h (mod N) ≡ m (mod N)  
m^ed ≡ m (mod N)  

<a id="markdown-2-质数" name="2-质数"></a>
# 2. 质数

> 指在大于1的自然数中,除了1和该数自身外,无法被其他自然数整除的数.大于1的自然数若不是质数,即称之为合数.

```python
# 编程思路:对正整数N,如果用2到根号n的所有整数去除,均无法整除,则n为质数

from math import sqrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

# 打印1000以内的质数
for i in range(2, 1000):
    if is_prime(i):
        print(i)
```

<a id="markdown-3-互质" name="3-互质"></a>
# 3. 互质

> 在数论中,如果两个或两个以上的`整数`的最大公约数是1,则称它们为互质.

```python
# 欧几里得算法(辗转相除法), 求最大公约数

def gcd(a, b):
     while b != 0:
        t = a % b
        a = b
        b = t
    return a

# 求8和10的最大公约数
gcd(8,10)
```

<a id="markdown-4-积性函数" name="4-积性函数"></a>
# 4. 积性函数

> 在数论中,积性函数是指一个定义域为正整数n的算数函数f(n).有如下性质: f(1) = 1, 且当a与b互质时,f(ab)=f(a)(b)

所以 pq互质时,N = pq, `φ(N) = φ(p)φ(q)`

<a id="markdown-5-欧拉函数" name="5-欧拉函数"></a>
# 5. 欧拉函数

> 在数论中,对正整数n,欧拉函数φ(n)是小于或等于n的正整数与n互质的数的数目.

根据欧拉函数性质: 当n为质数时,φ(n) = n - 1.  (因为质数与小于它的每一个正整数都构成互质关系)

所以: `φ(p)φ(q) = (p - 1)(q - 1).`


<a id="markdown-6-同余" name="6-同余"></a>
# 6. 同余

> 在数论中.同余是一种等价关系.当两个整数处以同一个正整数,获得相同余数,则二整数同余.

<a id="markdown-7-欧拉定理" name="7-欧拉定理"></a>
# 7. 欧拉定理

> 若n,a为正整数,且n,a互质数(即gcd(a,n)=1),则 a ^ φ(n) ≡ 1 (mod n)

<a id="markdown-8-模逆元" name="8-模逆元"></a>
# 8. 模逆元

> 一整数a对同余n之模逆元是指满足以下公式的整数b:  a^-1 ≡ b (mod n) 也可写作 ab ≡ 1 (mod n)

<a id="markdown-9-参考资料" name="9-参考资料"></a>
# 9. 参考资料

* http://code.activestate.com/recipes/578838-rsa-a-simple-and-easy-to-read-implementation/ (python example)
* https://zh.wikipedia.org/wiki/RSA%E5%8A%A0%E5%AF%86%E6%BC%94%E7%AE%97%E6%B3%95 (RSA维基百科)
* https://zh.wikipedia.org/zh/%E7%B4%A0%E6%95%B0 (质数维基百科)
* https://zh.wikipedia.org/wiki/%E4%BA%92%E8%B3%AA (互质维基百科)
* https://zh.wikipedia.org/wiki/%E7%A9%8D%E6%80%A7%E5%87%BD%E6%95%B8 (积性函数维基百科)
* https://zh.wikipedia.org/wiki/%E6%AC%A7%E6%8B%89%E5%87%BD%E6%95%B0 (欧拉函数维基百科)
* https://zh.wikipedia.org/wiki/%E6%AC%A7%E6%8B%89%E5%AE%9A%E7%90%86_(%E6%95%B0%E8%AE%BA) (欧拉定理维基百科)
* https://zh.wikipedia.org/wiki/%E6%A8%A1%E5%8F%8D%E5%85%83%E7%B4%A0 (模逆元维基百科)
