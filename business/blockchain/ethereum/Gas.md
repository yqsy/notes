<!-- TOC -->

- [1. 说明](#1-说明)
- [2. 价格换算](#2-价格换算)
- [3. 参考资料](#3-参考资料)

<!-- /TOC -->


# 1. 说明

在接触Gas前我一直有一个问题: 为什么要有gas,智能合约消耗的资源直接用eth来衡量不行吗?

这样理解就明白了: 就像比特币一样,用`sat/B`来衡量交易费. 先要计算出来`交易的大小`,然后根据交易的大小算出来费用是多少. 这里的中间单位是`交易大小`.而在以太坊中,中间单位是`合约的运行时消耗`,因为以太坊支持图灵完备的智能合约,拥有循环,递归?等操作,所以单独的字节码大小不能衡量出来运行时的消耗,所以需要`gas`这样一个中间层来表示`合约的运行时消耗`.

在以太坊的代码中我们观察到以下结构体:

```go
type txdata struct {
    // 省略
    Price        *big.Int        `json:"gasPrice" gencodec:"required"`
    GasLimit     uint64          `json:"gas"      gencodec:"required"`
    Payload      []byte          `json:"input"    gencodec:"required"`
    // 省略
}
```

在一个交易数据结构中包含`gasPrice,gas(Limit)`两个字段.  


# 2. 价格换算

价格表:

单位|维值
-|-
wei|1 wei
Kwei|1e3 wei
Mwei|1e6 wei
Gwei|1e9 wei
microether|1e12 wei
milliether|1e15 wei
ether|1e18 wei

Gas(汽油) 是用来衡量一笔交易锁消耗的计算资源的基本单位,当以太坊节点执行一笔交易所需的计算步骤越多,那么这笔交易消耗的Gas越多

一笔普通的转账交易会消耗21,000Gas,而一个创建智能合约的交易可能会消耗几万,甚至几百万Gas

目前以太坊客户端默认的GasPrice是0.000000001 Ether/Gas

Gas Limit:  

保护用户免收错误代码影响以致消耗过多的交易费, 如果Gas Used小于Gas Limit,那么矿工执行过程中会发现`Gas已被耗尽`而`交易没有执行完成`,此时矿工会`回滚到程序执行前的状态`

换句话说 `GasPrice * GasLimit` 表示用户愿意为一笔交易支付的`最高金额`, 因为如果没有Gas Limit限制,那么某些恶意的用户可能会发送一个`数十亿步骤的交易`并且没有人能够处理它,所以会导致拒绝服务攻击.


# 3. 参考资料

* 指令消耗的gas (https://github.com/djrtwo/evm-opcode-gas-costs/blob/master/opcode-gas-costs_EIP-150_revision-1e18248_2017-04-12.csv)
* https://ethereum.stackexchange.com/questions/3/what-is-meant-by-the-term-gas (ethereum stackexchange)
* https://ethgasstation.info/index.php (gas定价)
* https://etherconverter.online/ (换算)
