<!-- TOC -->

- [1. 说明](#1-说明)
- [2. 代码组织](#2-代码组织)
- [3. 参考资料](#3-参考资料)

<!-- /TOC -->


<a id="markdown-1-说明" name="1-说明"></a>
# 1. 说明

```bash
go get github.com/ethereum/go-ethereum

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
./vendor             548401 
./swarm              54865 
./dashboard          41701 
./p2p                29328 
./core               27924 
./cmd                23425 
./accounts           19071 
./eth                17674 
./whisper            12675 
./les                10343 
./crypto             7825 
./metrics            6376 
./consensus          6183 
./internal           5325 
./trie               5114 
./common             5028 
./rpc                4749 
./contracts          4337 
./signer             4059 
./rlp                3487 
./light              3178 
./mobile             3103 
./node               2964 
./tests              2372 
./miner              2236 
./log                1860 
./event              1726 
./graphql            1533 
./build              1492 
./console            1336 
./params             1091 
./ethdb              988 
./ethclient          738 
./ethstats           717 
```


<a id="markdown-3-参考资料" name="3-参考资料"></a>
# 3. 参考资料

