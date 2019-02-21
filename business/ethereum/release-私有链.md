<!-- TOC -->

- [1. 说明](#1-说明)
- [2. 参考资料](#2-参考资料)

<!-- /TOC -->


<a id="markdown-1-说明" name="1-说明"></a>
# 1. 说明

```bash
mkdir -p /mnt/disk1/linux/env/ethereum/

cat > ./genesis.json << EOF
{
    "config": {
        "chainId": 15,
        "homesteadBlock": 0,
        "eip155Block": 0,
        "eip158Block": 0
    },
    "difficulty": "200000000",
    "gasLimit": "2100000",
    "alloc": {
        "7df9a875a174b3bc565e6424a0050ebc1b2d1d82": { "balance": "300000" },
        "f41c74c9ae680c1aa78f42e5647a62f353b7bdde": { "balance": "400000" }
    }
}
EOF

rm -rf /mnt/disk1/linux/env/ethereum/data1

mkdir -p /mnt/disk1/linux/env/ethereum/data1

# 通过创世配置创建初始化数据
geth --datadir /mnt/disk1/linux/env/ethereum/data1 init ./genesis.json

# 开启节点
geth --datadir /mnt/disk1/linux/env/ethereum/data1 --networkid 15

# 生bootstrap节点
# bootnode --genkey=boot.key
# bootnode --nodekey=boot.key

# 主节点链接到bootstrap节点
# geth --datadir /mnt/disk1/linux/env/ethereum/data1 --networkid 15 --bootnodes <bootnode-enode-url-from-above>

# 挖矿
geth  --mine --minerthreads=1 --etherbase=0x0000000000000000000000000000000000000000

```

<a id="markdown-2-参考资料" name="2-参考资料"></a>
# 2. 参考资料

* https://github.com/ethereum/go-ethereum/wiki/Private-network
* https://github.com/ethereum/go-ethereum/wiki/Setting-up-private-network-or-local-cluster