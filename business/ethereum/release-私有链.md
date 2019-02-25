<!-- TOC -->

- [1. 说明](#1-说明)
- [2. 参考资料](#2-参考资料)

<!-- /TOC -->


<a id="markdown-1-说明" name="1-说明"></a>
# 1. 说明

```bash
mkdir -p /mnt/disk1/linux/env/ethereum/ && cd /mnt/disk1/linux/env/ethereum/

# 创建两个帐号
parse_privkey_eth `bx seed | bx ec-new`

# 帐号一:
私钥: 69763535777a502633560c27d366f41d1e478a21e38e53b4b56eba6486428eb3
公钥: 3f0e10100b22d81caf89bf55e802f7218808ad2bcfc5fcb659dc37ee2a6a3544986d8d5b31d071378a52588ab82e6caf2c0d5feafb6750b05d5313f8b000a6ad
地址: d0ab1fc3648c3bc5838be6dd4efcbeb3a4a50a6d

# 帐号二:
私钥: 5477e912eb487f6a9878527474d053de4b05981944f32a87ed106f6fa84cdf67
公钥: b8715e165f29b33d63ffd62ac892960cbcf4ab5cce33ca9444322d3381a1f867a1c1756617ace8c103c2fb93b266f8af6faa42d2f35c61d1b2e32375db4d3908
地址: abe0d7e816468f9a4b5b46e515fa4dd02d2418a4

# 挖矿帐号:
私钥: 6c2f62fe367e43a29546ccbea84740be00d42efcde81fe9e96cc80a2039e4e89
公钥: e1af61498eccd7706ac307ab4645037f465360f28633831c35b14020cc4481b7648bb054dcf50977c895015078f6b2f45688b20ff379df5f79cd5b9ec65983ac
地址: 5351b0ead94e9d5cb69798e1cbc2af99e6764eb7

cat > /mnt/disk1/linux/env/ethereum/genesis.json << EOF
{
    "config": {
        "chainId": 15,
        "homesteadBlock": 0,
        "eip155Block": 0,
        "eip158Block": 0
    },
    "difficulty": "0",
    "gasLimit": "2100000",
    "alloc": {
        "d0ab1fc3648c3bc5838be6dd4efcbeb3a4a50a6d": { "balance": "300000" },
        "abe0d7e816468f9a4b5b46e515fa4dd02d2418a4": { "balance": "400000" }
    }
}
EOF

rm -rf /mnt/disk1/linux/env/ethereum/data1 && mkdir -p /mnt/disk1/linux/env/ethereum/data1

# 通过创世配置创建初始化数据
geth --datadir /mnt/disk1/linux/env/ethereum/data1 init /mnt/disk1/linux/env/ethereum/genesis.json

# 开启节点
geth --datadir /mnt/disk1/linux/env/ethereum/data1 --networkid 1108

# 窗口连接
geth attach ipc:/mnt/disk1/linux/env/ethereum/data1/geth.ipc
    
# 挖矿
personal.importRawKey('6c2f62fe367e43a29546ccbea84740be00d42efcde81fe9e96cc80a2039e4e89', '123456')

# 列出帐号
personal.listAccounts

# 设置挖矿帐号
miner.setEtherbase(web3.eth.accounts[0])

# 查询余额
web3.fromWei(web3.eth.getBalance(web3.eth.coinbase).toNumber(), 'ether')

# 挖矿
miner.start(1)

# 显示区块数量
web3.eth.blockNumber

# 查询余额
web3.fromWei(web3.eth.getBalance(web3.eth.coinbase).toNumber(), 'ether')
```

<a id="markdown-2-参考资料" name="2-参考资料"></a>
# 2. 参考资料

* https://github.com/ethereum/go-ethereum/wiki/Private-network
* https://github.com/ethereum/go-ethereum/wiki/Setting-up-private-network-or-local-cluster

