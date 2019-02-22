<!-- TOC -->

- [1. 说明](#1-说明)
- [2. 代码组织](#2-代码组织)
- [3. 参考资料](#3-参考资料)

<!-- /TOC -->


<a id="markdown-1-说明" name="1-说明"></a>
# 1. 说明

```bash
go get github.com/ethereum/go-ethereum

cd /mnt/disk1/go/src/github.com/ethereum/go-ethereum
git checkout tags/v1.8.22
git branch -d master
git checkout -b master

go install -v ./...

# 调试
在goland中设置为geth/目录方式调试，因为geth/main.go有依赖到geth/*.go的全局变量，单独运行geth/main.go会产生使用未定义变量的错误.
```

<a id="markdown-2-代码组织" name="2-代码组织"></a>
# 2. 代码组织

```bash
cd /mnt/disk1/go/src/github.com/ethereum/go-ethereum 

# 目录内的源码统计
echo "" > /tmp/1.txt
find . -maxdepth 1 -type d -print0 | while read -d '' -r dir; do
    files=("$dir"/*)
    sum=`find $files -regex '.*\.go' -type f -print0 | xargs -0 wc -l | sort -nr | head -n 1 | awk '{print $1}'`
    printf "%-20s %s \n" "$dir" "$sum" >> /tmp/1.txt
done
sort  -k 2 -nr < /tmp/1.txt

```
源码:
```bash
./vendor             548401 # 其他源码
./swarm              54865  # 存储
./dashboard          41701  # 看板
./p2p                29328  # dht  nat 等
./core               27924  # 核心 虚拟机 类型系统 数据库 
./cmd                23425  # 命令行
./accounts           19071  # 用户系统
./eth                17674  # p2p相关
./whisper            12675  # 消息的加解密
./les                10343  # p2p?
./crypto             7825   # secp256k1
./metrics            6376   # 监控用
./consensus          6183   # 共识 ethhash
./internal           5325   # 内部?
./trie               5114   # 字典树
./common             5028   # 常用组件
./rpc                4749   # rpc接口
./contracts          4337   # 合约相关
./signer             4059   # 签名
./rlp                3487   # 编码解码
./light              3178   # ??
./mobile             3103   # 移动端
./node               2964   # p2p接口? 
./tests              2372 
./miner              2236   # 挖矿
./log                1860   # 日志
./event              1726   # 事件器
./graphql            1533   # 图
./build              1492   # 持续集成
./console            1336   # ?
./params             1091   # 初始参数
./ethdb              988    # 数据库
./ethclient          738    # 客户端
./ethstats           717    # 状态
```


<a id="markdown-3-参考资料" name="3-参考资料"></a>
# 3. 参考资料

* https://github.com/ethereum/go-ethereum/wiki/Developers%27-Guide
