<!-- TOC -->

- [1. 和target的关系](#1-和target的关系)
- [2. 难度调整公式](#2-难度调整公式)
- [初始难度](#初始难度)
- [3. 参考资料](#3-参考资料)

<!-- /TOC -->


# 1. 和target的关系

看rsk代码并且需要用到这块知识的时候,写一点来记录. 比特币nBits4个字节表达了target的含义,例如(0x207FFFFF) 表示从右至左占据0x20(32)个byte, 并且头部3个字节是0x7FFFFF, 两次hash头部80字节小端小于target 0x7fffff0000000000000000000000000000000000000000000000000000000000即是比特币的解. 

到了ethereum中, 难度变成了 difficulty. 那它和target的关系是什么呢?

例如:https://etherscan.io/block/7839915,  Difficulty: 2052115396247912

在代码中找到如下:
```go
// verifySeal:

target := new(big.Int).Div(two256, header.Difficulty)
if new(big.Int).SetBytes(result).Cmp(target) > 0 {
    return errInvalidPoW
}
return nil

// 也就是 (1 << 256) / difficulty , 
// diff 越大, target越小, 难度越大
// diff 越小, target越大, 难度越小
```

# 2. 难度调整公式

在比特币中难度调整公式如下:

新难度 / 旧难度 = 固定时间 / 旧时间

在以太坊下难度调整公式如下:

```go
	// diff = (parent_diff +
	//         (parent_diff / 2048 * max(1 - (block_timestamp - parent_timestamp) // 10, -99))
    //        ) + 2^(periodCount - 2)

出块时间为 < 10 秒:　　
parrent_diff + parent_diff / 2048 * (1) + 2^(periodCount - 2)　　

出块时间为 10 ~ 19 秒:
parent_diff + 2^(periodCount - 2)　　

出块时间为 20+ 秒:
parrent_diff + parent_diff / 2048 * (-1) + 2^(periodCount - 2)　　

出块时间为 30+ 秒:
parrent_diff + parent_diff / 2048 * (-2) + 2^(periodCount - 2)　　

逻辑就是diff数值越大难度越大,数值越小难度越小. 不像nBits越大难度越小,越小难度越大(还需要另外搞一个难度).
```

# 初始难度

```go
var (
	DifficultyBoundDivisor = big.NewInt(2048)   // The bound divisor of the difficulty, used in the update calculations.
	GenesisDifficulty      = big.NewInt(131072) // Difficulty of the Genesis block.
	MinimumDifficulty      = big.NewInt(131072) // The minimum that the difficulty may ever be.
	DurationLimit          = big.NewInt(13)     // The decision boundary on the blocktime duration used to determine whether difficulty should go up or not.
)
```

# 3. 参考资料

* https://www.coinwarz.com/difficulty-charts/ethereum-difficulty-chart
* https://ethereum.stackexchange.com/questions/5913/how-does-the-ethereum-homestead-difficulty-adjustment-algorithm-work (以太坊难度计算)