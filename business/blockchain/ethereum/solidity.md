<!-- TOC -->

- [1. 说明](#1-说明)
- [2. 注意点](#2-注意点)
- [3. 参考资料](#3-参考资料)

<!-- /TOC -->

# 1. 说明

存储:
* storage:  指针?
* memory:  值?

变量类型根据参数传递方式的不同可以分为两类: `值类型`和`引用类型`.  
* 值类型在每次赋值或者作为`参数传递`时都会`创建一份拷贝`
* 账户存储和内存
  * 状态变量与部分类型的局部变量(`数组,结构体等复杂类型`)是默认保存在`账户存储`中的
  * 函数的`参数和其他简单类型的局部变量`是保存在`内存`中的

值类型:
* 布尔类型 bool true,false
* 整数类型, int8,int16,...,int256(int)
* 枚举类型, enum ,默认从0开始,依次递增
* 地址类型, address (20字节)

引用类型:  
* 数组: 包括固定长度的`数组Ｔ[k]`，以及运行时动态改变长度的`动态数组T[]`
* 结构体: 结构体可以作为映射或者数组中的元素
* Map: 键值对存储结构


其他:
* delete 只是赋值运算

内置单位,全局变量和函数:
* 货币单位: wei,finney,szabo,ether
* 时间单位
* 区块和交易属性
  * block.blockhash 获取特定区块的散列值
  * block.conbase: 当前区块矿工的账号地址
  * block.difficulty: 当前区块的挖矿难度
  * block.gaslimit: 当前区块的Gas限制
  * block.number: 当前区块编号
  * block.timestamp: 以UNIX时间戳的形式表示当前区块的产生时间
  * msg.data: 表示完整的调用数据
  * msg.gas: 剩余的Gas
  * `msg.sender`: 发送者地址
  * msg.sig: 函数表示符
  * msg.value: 消息转账的以太币数额,单位是wei
  * now: 表示当前时间
  * tx.gasprice: 表示当前交易的Gas价格
  * tx.origin: 表示完整调用链的发起者
* 异常处理
  * assert: 用于处理内部的错误
  * require: `处理输入`或者来自外部模块的错误
  * revert: 中断程序执行并且回退状态改变
* 数学和加密函数
  * addmod: (x+y)%k ,加法支持任意精度
  * mulmod: (x*y)%k , 乘法支持任意精度
  * keccak256: 计算Ethereum-SHA-3 散列值
  * sha3: keccak256别名
  * sha256: 计算SHA-256散列值
  * ripemd160: 计算RIPEMD-160
  * ecrecover: 使用ECDSA算法对地址进行解密,返回解密后的地址
* 与合约相关的变量和函数
  * this: 指代当前合约,可以转换为地址类型
  * selfdestruct: 销毁当前合约,并将全部的以太币余额转账到作为参数传入的地址
  * suicide(address recipient): selfdestruct 函数的别名
  

修饰(修改函数和变量的可见性):
* external:  修饰函数,外部函数,`只能通过其他合约`发送交易的方式来调用
* public: 用于修饰公开的函数/变量,表明该函数/变量既可以在`合约外部访问`,也可以在`合约内部访问`
* internal: 内部函数/变量,只能在`当前合约`或者`继承自当前合约`的其他合约中访问
* private: 私有函数和变量,`只有当前合约内部才可以访问`


其他:
* view: 告诉编译器这个函数进行的是只读操作
* fallback: 当一个合约收到`无法匹配任何函数名的函数`调用或者仅仅用于转账的交易时,fallback函数将被自动执行

# 2. 注意点

* 区块链上智能合约的`所有信息`都是`公开可见`的,即使被private标记的私有变量
* 使用随机数是一件十分微妙的事情,基于安全性考虑,`尽可能避免使用随机数`
* 注意智能合约循环调用问题: 把 `调用合约加钱+股权清零`的先后顺序改成`股权清零+调用合约加钱`
* 注意使用msg.sender进行权限控制,而非tx.origin ??
* 注意uint8,uint16等长度小的整型的溢出
* var 会被编译器默认为uint8
* data会被补齐为32字节

开发建议

* 严格按照 Checks-Effects-Interactions: `检查-生效-交互`
* Fail-Safe 异常-安全,尽可能保障合约中数据的安全
* 限制合约中数字资产的数量,= =  为了安全起见,`最好不要在智能合约中存储大量的数字资产`


# 3. 参考资料

* http://wiki.jikexueyuan.com/project/solidity-zh/introduction-smart-contracts.html (简单学习)
* http://solidity.readthedocs.io/en/v0.4.24/solidity-by-example.html (原版教程)
* http://wiki.jikexueyuan.com/project/solidity-zh/units-globally-available-variables.html (全局变量)
