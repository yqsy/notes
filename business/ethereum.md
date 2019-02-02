---
title: ethereum
date: 2018-07-12 14:29:58
categories: [business]
---


<!-- TOC -->

- [1. 说明](#1-说明)
- [2. solidity](#2-solidity)
- [3. 详细介绍](#3-详细介绍)
    - [3.1. 场景](#31-场景)
    - [3.2. 开源项目](#32-开源项目)
    - [3.3. 架构](#33-架构)
    - [3.4. 钱包](#34-钱包)
    - [3.5. 存储](#35-存储)
    - [3.6. 防止ASCI的算法](#36-防止asci的算法)
    - [3.7. GAS 价格换算](#37-gas-价格换算)
    - [3.8. 交易包含的信息](#38-交易包含的信息)
    - [3.9. 公有链,私有链,联盟链](#39-公有链私有链联盟链)
- [4. 实践联盟链搭建](#4-实践联盟链搭建)
- [5. 实践智能合约](#5-实践智能合约)
    - [5.1. truffle](#51-truffle)
    - [5.2. remix](#52-remix)
- [6. 智能合约注意点](#6-智能合约注意点)
- [7. 优化知识](#7-优化知识)
- [8. 适用场景](#8-适用场景)
- [9. 常用指令](#9-常用指令)

<!-- /TOC -->

<a id="markdown-1-说明" name="1-说明"></a>
# 1. 说明

* http://www.tryblockchain.org/Solidity-source-mapping.html (solidity 语法说明)
* https://openzeppelin.org/api/docs/get-started.html (solidity安全合约的使用说明)
* https://openzeppelin.org/api/docs/learn-about-tokens.html (openzeppelin关于token的说明)
* https://github.com/comaeio/porosity (反编译)
* https://ropsten.etherscan.io/ (ROPSTEN网络)
* https://etherscan.io/ (区块链浏览器)
* https://ethplorer.io/ (web合约调用)
* https://ethgasstation.info/index.php (gas定价)
* https://etherconverter.online/ (换算)
* https://faucet.ropsten.be/ (充钱)
* https://faucet.metamask.io/ (充钱)
* chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#  (metamask网页)

---
* https://github.com/ethereum/wiki/wiki/JavaScript-API (js api)
* https://github.com/eoshackathon/ipfs_development_tutorial (古哥培训教程)
* https://www.ethereum.org/greeter (开发入门)
* http://ethdocs.org/en/latest/contracts-and-transactions/contracts.html (什么是合约)
* https://solidity.readthedocs.io/en/latest/ (所用语言,类似js)
* https://github.com/ethereum/dapp-bin (示例)
* https://ethereum.org/token#the-code (货币)
* https://ethereum.org/crowdsale#the-code (去中心知识库)

---
* http://blockchainlab.com/pdf/Ethereum_white_paper-a_next_generation_smart_contract_and_decentralized_application_platform-vitalik-buterin.pdf (论文)



<a id="markdown-2-solidity" name="2-solidity"></a>
# 2. solidity

* http://wiki.jikexueyuan.com/project/solidity-zh/introduction-smart-contracts.html (简单学习)
* http://solidity.readthedocs.io/en/v0.4.24/solidity-by-example.html (原版教程)
* http://wiki.jikexueyuan.com/project/solidity-zh/units-globally-available-variables.html (全局变量)



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

<a id="markdown-3-详细介绍" name="3-详细介绍"></a>
# 3. 详细介绍

<a id="markdown-31-场景" name="31-场景"></a>
## 3.1. 场景

* Golem 创造一个全球空闲计算资源的产消市场
* CryptoKitties 基于以太坊区块链的养猫娱乐DApp
* Augur 预测未来真实事件的市场预测平台
* Bancor  以太坊代币之间兑换的交易所DApp  代币是BNT, 有经济学的换算公式, 使得各种代币均能根据其现有价格,总市值等标准与BNT进行交换
* KyberNetwork 数字货币交易所App 跨区块链之间的各种代币之间的交易


`KyberNetwork`

去中心化,无需新人的交易所,内部机制主要由以太坊智能合约实现,代币兑换都是链上交易

* 用户希望向其他用户转账A代币
* 接收方希望收到B代币

用户可以向KyberNetwork的智能合约发送A代币,KyberNetwork在其去中心化的代币存储池中实现兑换出相应价值B代币发送给接收方

链上交易,兑换过程可被立即确认,过程结束后也可追溯,并且用户无需更改以太坊底层协议或其他智能合约协议


<a id="markdown-32-开源项目" name="32-开源项目"></a>
## 3.2. 开源项目
开源项目:
* Go-ethereum: `Geth` 目前使用最为广泛的以太坊客户端,又称Geth
* CPP-ethereum: C++语言实现实现的版本. Windows,Linux和OS X等各个版本的操作系统以及多种硬件平台
* Parity: Rust语言实现的版本
* Pyethapp: python语言实现的版本


浏览器:
* Mist: 以太坊官方开发的工具,浏览各类 DApp的项目
* MetaMask: 浏览器插件, 只需通过MetaMask便可在浏览器上连接以太坊网络,和运行以太坊DApp
* `Etherscan`: 在以太坊以及去中心化智能合约上的区块浏览器

以太坊开发工具: 
* `Web3.js`: 兼容以太坊核心功能的JavaScript库
* ENS-register: Ethereum name service 为以太坊账户提供域名注册服务
* `Solc`: `命令行工具` (编译Solidity成字节码,提供一些智能合约相关的信息)
* `Remix`: `网页终端`整合了`Solidity代码的编写`,调试和运行等功能
* `Truffle`: 针对以太坊Dapp的开发框架, 对Solidity智能合约的开发,测试,部署等进行全流程的管理,帮助开发者更专业地开发以太坊DAPP
* `testrpc`: 模拟以太坊
* `Ganache`: 同上.良好的交互界面,能做到对Transaction的立即执行.
* `TRUFFLE BOXES`: 构建更为复杂的,功能也更为强大的DApp

安全:
* Oyente: python,判断代码中有没有常见的漏洞
* solidity-coverage: Node.js编写的Solidity代码覆盖率测试工具,需要结合测试网络使用
* Solgraph: 将一个智能合约作为输入,输出一个DOT图文件



<a id="markdown-33-架构" name="33-架构"></a>
## 3.3. 架构

![](http://ouxarji35.bkt.clouddn.com/c98ff12076232f60ddccda38376baf1ffd4fe309.jpeg)

账户:  
* 外部账户: 由人存储的,可以存储以太币,是由公钥和私钥控制的账户
* 合约账户: 由`外部账户创建`的账户

外部账户(EOA)由私钥来控制,拥有一对公私钥,地址由公钥来决定,外部账户`不能包含以太坊虚拟机(EVN)代码`

可以用Geth指令创建一个外部账户,生成一个账户地址的过程:
* 设置账户的`私钥`,也就是通常意义的用户密码
* 使用加密算法由`私钥生成对应的公钥`  `secp256k1椭圆曲线密码算法`
* 根据公钥得出相应的账户地址 `SHA3`

合约账户和普通账户最大的不同就是它`还存有智能合约` 

私钥的三种形态: Private Key , Keystore & Password, Memonic code
* 256位数字,私钥最初始的状态
* 以太坊官方钱包,`私钥和公钥`将会以`加密`的方式保存一份JSON文件,存储在keystore目录下,用户需要同事`备份Keystore`和`对应的Password`
* BIP 39 ,随机生成12~24个比较容易记住的单词,该种子通过BIP-0032提案的方式生成确定性钱包??

<a id="markdown-34-钱包" name="34-钱包"></a>
## 3.4. 钱包

钱包:  

目前有多种以太坊钱包, 如Mist以太坊钱包,Parity钱包,Etherwall钱包,Brain钱包等

<a id="markdown-35-存储" name="35-存储"></a>
## 3.5. 存储  

比特币中保存了一棵Merkle树, 以太坊对三种对象设计了3棵Merkle Patrcia树,融合了Merkle树和Trie树的优点
* 状态树
* 交易树
* 收据树

这3三种树帮助以太坊客户端做一些简易的查询,如查询某个账户的余额,某笔交易是否被包含在区块中

`区块,交易`等数据最终存储在`levelDB`数据库中.

以太坊去块头不是只包括一棵MPT树,而是为三种对象设计了3棵树. 分别是 
* 交易树(Transaction Tree): 每个键是交易的序号,值是交易的内容
* 状态树 (State Tree): 状态树用来记录各个账户的状态的树,它需要经常进行更新
* 收据树(Receipt Tree): 代表每笔交易相应的收据

客户端可以轻松地查询以下的内容: 
* 某笔`交易`是否被包含`在特定的区块`中   -> `交易树`
* 查询某个地址在过去的30天中发出某种类型事件的所有实例 -> `收据树`
* 目前某个`账户的余额` -> `状态树`
* 一个`账户是否存在` -> `状态树`
* 假如在某个合约中进行一笔交易,`交易的输出`是什么 -> `状态树`


<a id="markdown-36-防止asci的算法" name="36-防止asci的算法"></a>
## 3.6. 防止ASCI的算法
共识算法:

以太坊有一个专门设计的PoW算法,Ethash算法 `(抵制ASIC)`

为什么能抵制ASCI?   
* https://zhuanlan.zhihu.com/p/35326901
* https://zhuanlan.zhihu.com/p/28830859


<a id="markdown-37-gas-价格换算" name="37-gas-价格换算"></a>
## 3.7. GAS 价格换算

大概就是使用种子产生一个16MB的伪随机缓存,基于缓存再生成一个1GB的数据集,称为DAG,挖矿可以概括为矿工从DAG中`随机`选择元素`并对其进行散列的过程`,DAG也可以理解为一个完整的搜索空间.

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

<a id="markdown-38-交易包含的信息" name="38-交易包含的信息"></a>
## 3.8. 交易包含的信息

一条交易内容包含以下的信息:

* from: 交易`发送者的地址` `必填`
* to: 交易`接收者的地址` 如果`为空`意味这是一个`智能合约`的交易
* value: 发送者要转移给接收者的以太币数量
* data: 如果存在,则表明该交易是一个`创建`或者`调用智能合约交易`
* Gas Limit: 这个交易允许消耗的最大Gas数量
* GasPrice : 表示发送者愿意支付给矿工的Gas价格
* nonce: 区别同一用户发出的不同交易的标记
* hash: 以上信息生成的散列值,`作为交易的ID`
* r,s,v: 交易签名的三个部分,由`发送者的私钥`对交易hash进行签名生成


以太坊中包含3种交易:
* 转账交易: 指定交易的发送者,接收者,转移的以太币数量
* `创建`智能合约交易: 指将合约部署在区块链上,`to`字段是一个空字符串,在`data`字段中指定初始化合约的二进制代码
* `执行`智能合约交易: 需要将`to`字段指定为要调用的智能合约的地址,通过`data`字段指定要调用的方法以及向该方法传递参数

接口
* JSON-RPC
* Web3.JavaScript.API


以太坊域名服务 Ethereum Name Service

以太坊推出了可以将散列地址"翻译"成一个简短易记的地址的ENS命名服务,ENS很像我们平时所熟知的DNS服务,比如A要给B转一笔钱,`当A发起交易时,在收款人地址处不用再填写B的散列地址`.填写B的简单易记的钱包域名`B.myetherwallet.eth`也能正常交易


用户注册域名需要完成以下过程:
* 用户通过交易执行智能合约,`向合约提供自己想要注册的域名`
* 1. 域名被注册 -> 重新提交 || 买域名 2. 正在被竞拍 -> 参加竞标,投入比其他竞标者更高的竞价金  3. 没有被注册或竞拍 -> 用户发起竞拍
* 用户只有一次出价机会,竞价匿名
* 竞价截止后进入揭示环节,所有参加竞标的用户必须揭标. 否则竞价金的99.5%都会进入黑洞
* 揭示之后. 出价最高的用户获得竞标胜利,并将`以第二竞价`的金额获得该域名,多余金额将会退回该账户的钱包
* 在域名持有期内,用户可以将域名绑定到自己的以太坊地址,转移域名的使用权,添加设置子域名等,甚至还可以转让域名的所有权


<a id="markdown-39-公有链私有链联盟链" name="39-公有链私有链联盟链"></a>
## 3.9. 公有链,私有链,联盟链

以太坊公有链,联盟链,私有链特点对比

-|公有链|联盟链|私有链
-|-|-|-
可信权威|(依赖代码)|特定联盟|特定团体
挖矿节点成本|挖矿奖励(以太币)|由特定联盟规定|由特定团体规定
虚拟货币|`用于奖励挖矿节点(以太币)`|`不需要`|`不需要`
结算|可行|可行(如果有虚拟货币)|可行(如果有虚拟货币)
共识算法|工作量证明|使用拜占庭容错算法|权威证明
区块链实现|以太坊协议(比特币核心)|企业级以太坊|企业级以太坊
商业价值|高可用性,低成本的分布式账本|高可用性,低成本的分布式账本,无需中间保证金,透明结算|无需中间保证金,透明结算,直接结算


公有链: 是世界上任何人都可以访问读取的,任何人都可以发送交易并且如果交易有效的话可以将之包括到区块中.

加密数字经济采取工作量证明机制或股权证明机制等方式,将`经济奖励`和`密码学`结合起来. 公有链是真正意义上的完全去中心化的区块链,主要适用于`虚拟货币`,`面向大众的电子商务场景`. 公有链分为主网和测试网络.

* 主网:   所有人都可以`随时地接入网络`,所有加入网络的全节点都可以加入到共识机制中,
* 测试网络: 专门给用户用来开发,测试和调试用的区块链网络,


联盟链: (Consortium Blockchain)

共识过程收到一些预选节点控制的区块链,如`企业,银行`等.  节点`组成`一个`联盟`, 网络中的区块链和节点状态的改写更新由联盟中的各节点达成共识所决定. 而对于网络中其他`非联盟节点`,最多只能够`读取到联盟区快链`中的`全部或部分数据`.

包括信息,金融,能源等多个领域的跨国企业,初创公司和研究机构都投入到`企业级联盟链`的`研发`中. 超级账本(Hyperledger)就属于联盟链架构

联盟链是一种需要参与许可的区块链,是在一群值得新人的参与者中共享的区块链,基于以太坊协议开发的联盟区块链-`Quorum`

在Go语言版本以太坊架构的基础上进行改进,使私有交易的数据只对指定的交易方可见.基于`Raft的一致性协议`和`Istanbul BFT协议`(类似PBFT协议) 


使用这两个一致性协议就避免PoW或PoS的弊端.. 


不过两种协议的使用场景还是有所区别的,在需要支持拜占庭容错的环境中,应该使用`Istanbul BFT`协议而非基于Raft的一致性协议

私有交易:  

网络中对所有节点都能在以太坊原有协议的基础上对`共有状态`达成`共识`,但`私有状态`的`数据库`就各不相同

但是问题就是私有状态的更新无法被其他无关节点认可,所以Quorum在应用层上设计了一套解决方案,其在网络中引入一个`监督节点`. 使得监督节点备份了所有私有交易以及所有节点的私有状态


私有链: 

完全私有的区块链则是更接近于中心化的数据库,私有链的应用场景主要是公司内部的数据库管理,账目审计等. 私有链的主要价值是提供`区块链安全高效`,`公开透明`,`可追溯`,`不可篡改`的特性,

<a id="markdown-4-实践联盟链搭建" name="4-实践联盟链搭建"></a>
# 4. 实践联盟链搭建

* https://github.com/ethereum/go-ethereum/wiki/Private-network (创建私有网络)

```bash
go get github.com/ethereum/go-ethereum
cd ~/go/src/github.com/ethereum/go-ethereum
make geth
mv ./build/bin/geth ~/go/bin/

mkdir -p /home/yq/resource/test/testeth
cd /home/yq/resource/test/testeth
cat > ./genesis.json << EOF
{
    "config": {
        "chainId": 15,
        "homesteadBlock": 0,
        "eip155Block": 0,
        "eip158Block": 0
    },
    "coinbase" : "0x0000000000000000000000000000000000000000",
    "difficulty" : "0x40000",
    "extraData" : "",
    "gasLimit" : "0xffffffff",
    "nonce" : "0x0000000000000042",
    "mixhash" : "0x0000000000000000000000000000000000000000000000000000000000000000",
    "parentHash" : "0x0000000000000000000000000000000000000000000000000000000000000000",
    "timestamp" : "0x00",
    "alloc": { }
}
EOF

# 生成创世纪节点,并设置data目录
geth --datadir ./data/00 init genesis.json

# 开启
geth --datadir ./data/00 --networkid 15 console

# 查看账户
eth.accounts

# 创建
personal.newAccount("123456")
"0xa69f1eafbba46f23892d9e142db356de6a7c9d9b"

# 开始挖矿
miner.start(1)

# 停止挖矿
miner.stop()

# 查看钱包
eth.getBalance(eth.accounts[0]) 
```

在私有网络中建立多个node组成的集群,并互相发现,产生交易

* 每个实例都有独立的数据目录`(--datadir)`
* 每个示例运行都有独立的端口 `(--port和--rpcport)`
* 在集群的情况下,示例之间都必须要知道彼此
* 唯一的ipc通信端点,或者`禁用ipc`


第二个节点与第一个节点连接
```bash
# 第一个节点
geth --datadir ./data/00 --networkid 314590 --ipcdisable --port 61910 --rpcport 8200 console

# 获取enode url
admin.nodeInfo.enode

"enode://9802f2078df03e036319d32006a9009a57c3d90328e641f247bcb29a8452a621532e734d2e541cfc236338bc152e816617bf364878e6c5888fbc8bdc81fd3aed@[::]:61910"

# 第二个节点
geth --datadir ./data/01 init ./genesis.json
geth --datadir ./data/01 --networkid 314590 --ipcdisable --port 61911 --rpcport 8101 --bootnodes "enode://9802f2078df03e036319d32006a9009a57c3d90328e641f247bcb29a8452a621532e734d2e541cfc236338bc152e816617bf364878e6c5888fbc8bdc81fd3aed@127.0.0.1:61910" console

# 打印初始节点
admin.nodeInfo.enode

# 也可以不加那个参数,通过以下把节点加进来
admin.addPeer

# 第二个节点输入
admin.nodeInfo

# 第一个节点输入
net.peerCount
admin.peers

```

转账测试
```bash
# 第二个节点创建账号
personal.newAccount("123456")
"0xc4c5255d8bad7fa64debcd9c9ea9a7a18084f7d9"

# 第一个节点
personal.unlockAccount(eth.accounts[0], "123456")

# 转账
eth.sendTransaction({from: "0xa69f1eafbba46f23892d9e142db356de6a7c9d9b", to: "0xc4c5255d8bad7fa64debcd9c9ea9a7a18084f7d9", value: web3.toWei(1, "ether")})

# 查看派发的
eth.pendingTransactions

# 第二个节点查看资金
eth.getBalance(eth.accounts[0]) 

```

<a id="markdown-5-实践智能合约" name="5-实践智能合约"></a>
# 5. 实践智能合约

<a id="markdown-51-truffle" name="51-truffle"></a>
## 5.1. truffle

* https://web3js.readthedocs.io/en/1.0/web3-eth-accounts.html (web3开发手册)
* https://github.com/ethereum/wiki/wiki/JavaScript-API (web3接口)
* https://truffleframework.com/boxes/webpack
* https://truffle-box.github.io/ (truffle box)
* https://truffleframework.com/docs/truffle/reference/configuration (官方教程)
* https://truffleframework.com/tutorials/using-infura-custom-provider (infura教程)
*  https://truffleframework.com/docs/truffle/reference/configuration (testrpc)
* https://truffleframework.com/tutorials/building-testing-frontend-app-truffle-3 (前置)
* https://truffleframework.com/ganache (ganache)

127.0.0.1:9545
```bash
npm install -g truffle
mkdir testtruffle && cd testtruffle
truffle init
npm init -y
npm install --save-exact openzeppelin-solidity@next
# contracts 目录写合约
# migrations 目录写部署脚本
truffle develop
# 编译
compile
# 部署
migrate
# 重新部署
migrate --reset

# 加载合约
StagesToken.deployed().then(instance => contract = instance)
```

127.0.0.1:8545
```bash
# testrpc
npm install -g ethereumjs-testrpc

truffle compile
truffle migrate
truffle console
```

127.0.0.1:7545 (web测试 ganache)
```bash
truffle unbox webpack

truffle compile
truffle migrate --network ganache
truffle test
npm run lint
npm run dev
npm run build
    
```


发布到ropsten
```bash
# 安装infura.io
npm install truffle-hdwallet-provider --save

# 部署至ropsten
truffle develop
compile
migrate --network ropsten

# 替换合约
migrate --reset --network ropsten
```

truffle.js配置
```
var HDWalletProvider = require("truffle-hdwallet-provider");

var infura_apikey = "50a4afb18ee44d649ad9548c1828ca79";
var mnemonic = "embody save subway region brass benefit eager bike advice ocean favorite have";

module.exports = {
    networks: {
        development: {
            host: "localhost",
            port: 8545,
            network_id: "*"
        },
        ropsten: {
            provider: new HDWalletProvider(mnemonic, "https://ropsten.infura.io/" + infura_apikey),
            network_id: 3,
            gas: 4500000
        }
    }
};
```


* contracts/: 开发者`编写`的智能合约
* migrations/: 用来存放`部署脚本`
* tests/: 用来存放`测试`文件
* truffle.js: Truffle `默认的配置文件`



<a id="markdown-52-remix" name="52-remix"></a>
## 5.2. remix

* https://github.com/ethereum/remix
* https://github.com/ethereum/remix-ide
* https://www.npmjs.com/package/remix-ide (安装方法)
* https://remix.ethereum.org/

```bash
npm install remix-ide -g

cd /mnt/disk1/linux/reference/project/testsol
remix-ide

```

智能合约属性:  
参考: https://github.com/ethereum/wiki/wiki/JSON-RPC#the-default-block-parameter

<a id="markdown-6-智能合约注意点" name="6-智能合约注意点"></a>
# 6. 智能合约注意点

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

<a id="markdown-7-优化知识" name="7-优化知识"></a>
# 7. 优化知识

(侧链SideChains): 它可以让比特币安全的从比特币主链转移到其他区块链,又可以从其他区块链安全地返回比特币主链. `外部嫁接到主链`

分片技术 Sharing: 让以太坊从网络上的`每个节点`都要`验证`每一笔交易的模式,`转型到只需要小部分的节点来验证每一笔交易的模式`.  `将主链进行内部分割`

雷电网络 Raiden Network: 设计源于比特币的`闪电网络(Lightning Network)`. 链下支付网络,不同于`分片`等致力于解决以太坊中`所有交易`的效率,雷电网络解决的是用户账户之间的以太币的转账问题. 不能追溯历史!

下一代以太坊共识 Casper:  Pow消耗大量算力和电力,已经被广为诟病.因此以太坊基金会一直在积极地推进使用`股权证明PoS`替代PoW最为共识协议. 以太坊将它的Pos共识协议`称为Casper`.

* Casper FFG: PoW/Pos混合的共识机制.
* Casper CBC: ...

<a id="markdown-8-适用场景" name="8-适用场景"></a>
# 8. 适用场景

以太坊的主要目标是公有链,数字资产的安全是第一位的,`宁可损失性能,也要保证用户账本的安全`,对性能的任何优化都必须在系统安全的前提下进行

...

<a id="markdown-9-常用指令" name="9-常用指令"></a>
# 9. 常用指令

```bash

# 修改账户
web3.eth.defaultAccount = web3.eth.accounts[1]


# 所属者
contract.owner()

# ERC20Detailed
contract.name()
contract.symbol()
contract.decimals()

# ERC20

# 1. 发行量
contract.totalSupply()

# 2. 某个账户的余额
contract.balanceOf(web3.eth.coinbase)
contract.balanceOf(web3.eth.accounts[1])

# 3. 查询允许别人花多少自己的钱
contract.allowance(web3.eth.coinbase,web3.eth.accounts[1]) 

# 4. 转账
contract.transfer(web3.eth.accounts[1], 5)

# 5. 允许别人转自己多少钱
contract.approve(web3.eth.accounts[1], 5)

# 6. 从from转到to(并且msg.sender必须有数额),并且需要(approve的)
contract.transferFrom(web3.eth.coinbase, web3.eth.accounts[1], 5)

# 7. 增加别人花自己钱的数量
contract.increaseAllowance(web3.eth.accounts[1], 5)

# 8. 减少别人花自己钱的数量
contract.increaseAllowance(web3.eth.accounts[1], 5)

# ERC20Burnable

# 1. 燃烧自己的
contract.burn(100)

# 2. 燃烧_allowed (并且msg.sender必须有数额)
contract.burnFrom(web3.eth.coinbase, 100)

```
