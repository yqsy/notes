<!-- TOC -->

- [1. 说明](#1-说明)
- [2. 源码](#2-源码)
- [3. estimateSmartFee](#3-estimatesmartfee)
- [4. 手续费两极化很严重](#4-手续费两极化很严重)
- [5. 参考资料](#5-参考资料)

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


<a id="markdown-2-源码" name="2-源码"></a>
# 2. 源码

```bash
# sendtoaddress 参数设置为true,根据交易的大小计算出来手续费，再扣掉转账资金的部分作为手续费

# 堆栈:
CWallet::CreateTransaction
SendMoney
sendtoaddress

# 细节
# 计算出来交易的vbytes
nBytes = CalculateMaximumSignedTxSize(txNew, this, coin_control.fAllowWatchOnly);

# 选择费率策略根据大小算出来相应的费用
nFeeNeeded = GetMinimumFee(*this, nBytes, coin_control, ::mempool, ::feeEstimator, &feeCalc);
* 

# 智能估计费率
CBlockPolicyEstimator::estimateSmartFee

# 测试一笔交易得到如下数据,因为设置的-fallbackfee=0.0002,也就是收取0.0002 比特币 / KB. 也就是20聪 / byte
# Fee:3820 *
# Bytes:191 *
```

<a id="markdown-3-estimatesmartfee" name="3-estimatesmartfee"></a>
# 3. estimateSmartFee

费用估算的目的是为了寻找到最合适的价格,使得矿工大概率能够接受,也就是自己的交易能够大概率的被打包到交易池,完成自己交易的目的.

具体费用计算细节很复杂,我只能总结一个大概:   
计算方法是指数加权平均,根据过去的事务所对应的手续是否被打包的数据,推断出来最合适的交易费是多少.


<a id="markdown-4-手续费两极化很严重" name="4-手续费两极化很严重"></a>
# 4. 手续费两极化很严重

比如在区块: https://www.blockchain.com/btc/block/00000000000000000015f34fd213f2a83fdcb81bf8d8a2348fc6dc1ae0f0e1a1 中

* https://www.blockchain.com/btc/tx/5faeb0b36158a6aca8cbd0d465a03f94b0f44e6cc57f244ff656b337c497b001
* https://www.blockchain.com/btc/tx/cea757a572f6de01afabfd55f089c7f9f32f1b89f32549b2836f3e7849ee0230 


这个问题存在的原因是因为,交易的数量有高峰有低谷,那么在高峰时间端用很低的手续费用发送的交易,矿工因为获利少而不愿意打包,矿工又其他手续费更高的交易去打包. 到了低谷的时候,有了更多空闲的空间,几毛钱也是钱,矿工就把交易放到了区块中.

所以同一个区块的手续费在上面的例子中有0.002也有0.00000559.

<a id="markdown-5-参考资料" name="5-参考资料"></a>
# 5. 参考资料

* https://en.bitcoin.it/wiki/Miner_fees (手续费)
* https://bitcointechtalk.com/* 
-core-fee-estimation-27920880ad0 (费用估算介绍)
* https://en.wikipedia.org/wiki/Moving_average#Exponential_moving_average
* https://bitcoinfees.info/ (比特币费用曲线)
