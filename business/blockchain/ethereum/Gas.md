<!-- TOC -->

- [1. 说明](#1-说明)
- [2. 参考资料](#2-参考资料)

<!-- /TOC -->


<a id="markdown-1-说明" name="1-说明"></a>
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


<a id="markdown-2-参考资料" name="2-参考资料"></a>
# 2. 参考资料

* 指令消耗的gas (https://github.com/djrtwo/evm-opcode-gas-costs/blob/master/opcode-gas-costs_EIP-150_revision-1e18248_2017-04-12.csv)
* https://ethereum.stackexchange.com/questions/3/what-is-meant-by-the-term-gas (ethereum stackexchange)
* https://ethgasstation.info/index.php (gas定价)
* https://etherconverter.online/ (换算)
* 