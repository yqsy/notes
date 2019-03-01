<!-- TOC -->

- [1. 说明](#1-说明)
- [2. 实践](#2-实践)
- [3. 参考资料](#3-参考资料)

<!-- /TOC -->


<a id="markdown-1-说明" name="1-说明"></a>
# 1. 说明

参考以下浏览器:

* https://www.blockchain.com/zh/btc/tx/b3cae20701995b1192ca01aa96a014f02f5190533af057c30995a4ac16c46d99
* https://btc.com/b3cae20701995b1192ca01aa96a014f02f5190533af057c30995a4ac16c46d99
* https://btc.chaintools.io/tx/b3cae20701995b1192ca01aa96a014f02f5190533af057c30995a4ac16c46d99

手续费有以下计算方式,并且实际手续费0.0009:

* 117.188 sat/WU    -- Weight 768
* 468.8 sat/VB      -- Vsize  192
* 234.4 sat/B       -- Size   384

如果Vsize < Size, 表示开启了隔离见证. 算手续费还是按照Vsize为准, 因为有两重含义:

* 未开启隔离见证,那么那么Vsize=Size,用哪个交易单位算都是一样的.
* 开启隔离见证,Vsize相较于Size小了一些,因为计算时会给见证数据打4x折扣. 用Vsize包含了省略额外见证数据手续费的想法. Size会更大一些, sat/B会变小,表示了花少的手续费存更多的数据的含义.
  * 而对于old version来说, 其看到的只有raw交易(没有签名), 那么其sat/B会被认为是更高,所以理所应当会接受

假设手续费为x sat/VB, 没有开启隔离见证, Vsize = Size , 那么手续费y sat/B:

$$\begin{aligned}
x * Vsize = y * Size\\
y = x\\
\end{aligned}$$

假设手续费为x sat/VB, 开启了隔离见证, Vsize < Size, 那么手续费y sat/B:

$$\begin{aligned}
x * Vsize = y * Size\\
y =  \frac{x * Vsize}{Size}\\
y < x
\end{aligned}$$


<a id="markdown-2-实践" name="2-实践"></a>
# 2. 实践



<a id="markdown-3-参考资料" name="3-参考资料"></a>
# 3. 参考资料

* https://en.bitcoin.it/wiki/Miner_fees (手续费)
