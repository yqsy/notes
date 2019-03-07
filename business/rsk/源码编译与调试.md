<!-- TOC -->

- [1. 说明](#1-说明)
- [2. 代码组织](#2-代码组织)
- [3. 参考资料](#3-参考资料)

<!-- /TOC -->


<a id="markdown-1-说明" name="1-说明"></a>
# 1. 说明

源码拉取:

```bash
cd /mnt/disk1/linux/reference/refer
git clone --recursive https://github.com/rsksmart/rskj.git
cd rskj
git checkout tags/ORCHID-0.6.0
git branch -d master
git checkout -b master

chmod +x ./configure.sh
./configure.sh

# 再用 intellij IDEA 加载 build.gradle

# 测试网络添加参数
-Dblockchain.config.name=testnet

# 本地网络添加参数
-Dblockchain.config.name=regtest

# 在intellij IDEA添加运行项目
# Main Class: co.rsk.Start
# Working directory: /path-to-code/rskJ
# Use classpath of module: rskj-core_main
# JRE need to be set as: Default (1.8 - SDK of 'rsk-core_main' module)

# 命令行编译/运行 
./gradlew build -x test 
./gradlew run
```

<a id="markdown-2-代码组织" name="2-代码组织"></a>
# 2. 代码组织

```bash
cd /mnt/disk1/linux/reference/refer/rskj/rskj-core/src/main/java/co/rsk

# 目录内的源码统计
echo "" > /tmp/1.txt
find . -maxdepth 1 -type d -print0 | while read -d '' -r dir; do
    files=("$dir"/*)
    sum=`find $files -regex '.*\.java' -type f -print0 | xargs -0 wc -l | sort -nr | head -n 1 | awk '{print $1}'`
    printf "%-20s %s \n" "$dir" "$sum" >> /tmp/1.txt
done
sort  -k 2 -nr < /tmp/1.txt

# rsk目录下的源码统计
find *.java -maxdepth 1  -type f -print0 | xargs -0 wc -l | sort -nr | head -n 1 | awk '{print $1}'
```

源码:
```bash
./net                9293  # DHT相关
./peg                7394  # 双向锚定相关
./core               3726  # 核心区块链相关
./rpc                3631  # rpc接口,应该兼容以太坊
./mine               2478  # 挖矿 
./trie               1741  # 字典树
./validators         1722  # 验证区块
./config             1653  # 配置
./remasc             1343  # ?
./db                 1194  # 数据库
./scoring            1101  # 分数
./util               522   # 常用功能
./jsonrpc            437   # json rpc的包装
./crypto             434   # SHA3 Keccak256
./cli                406   # 命令行解析
./metrics            257   # hash速度测试
./blocks             244   # 区块读写包装,用的还是以太坊的结构?
./vm                 69    # bitset
./panic              35    # panic函数

./                   666 # 只搜索当前一层目录的

# 源码大概在4w行左右
```

引用的ethereum的源码:
```bash
./vm                 9214  # EVM 虚拟机
./net                7673  # DHT
./core               5564  # 区块,帐号,交易
./crypto             3262  # ECIES
./util               3152  # 辅助源码
./rpc                2961  # rpc函数接口
./config             2763  # 配置
./db                 2365  # 数据库
./solidity           956   # solc编译器
./datasource         614   # 数据库包装
./sync               524   # 同步?
./listener           433   # 监听
./validator          353   # 验证规则
./json               186   # json辅助代码
./facade             186   # ?

./                   164   # 
```

<a id="markdown-3-参考资料" name="3-参考资料"></a>
# 3. 参考资料

* https://github.com/rsksmart/rskj 
* https://guides.gradle.org/building-java-applications/
