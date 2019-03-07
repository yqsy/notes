
<!-- TOC -->

- [1. 说明](#1-说明)
- [2. 参考资料](#2-参考资料)

<!-- /TOC -->


<a id="markdown-1-说明" name="1-说明"></a>
# 1. 说明

* 启动前重置测试信息. `~/.rsk` 
* 启动前重置日志信息. `rskj/logs`
* 将rskj/rskj-core/src/main/resources/config/main.conf中的`bootstrap`信息清空
* 开启rpc可以mine, `rskj/rskj-core/src/main/resources/reference.conf`:

```bash
# 增加modules
modules = [
        {
            name: "mnr",
            version: "1.0",
            enabled: "true"
         },
         #Other enabled modules
         ...
    ]


# 添加miner选项
miner {
    server.enabled = true
    client.enabled = false
    minGasPrice = 59240000

    # this is a hex-encoded, 20-bytes length address where the miner gets the reward
    reward.address = 2340482f28897774204f40aa205497dc1be74d45
}
```


开启:
```bash
# 重置语句
rm -rf ~/.rsk  && rm -rf /mnt/disk1/linux/reference/refer/rskj/rskj-core/logs

# 查看日志
less /mnt/disk1/linux/reference/refer/rskj/rskj-core/logs/rsk.log

# 开启
./gradlew build -x test 
./gradlew run

# 端口
tcp     :4444  -- rpc接口
tcp/udp :5050  -- p2p网络
```

rpc指令:
```bash
# mnr_getWork (eth_getWork)
curl -X POST --data '{"jsonrpc": "2.0", "id":"1", "method": "mnr_getWork", "params": [] }' -H "Content-Type:application/json"  127.0.0.1:4444

# mnr_submitBitcoinBlock,mnr_submitBitcoinBlockTransactions,mnr_submitBitcoinBlockPartialMerkle (eth_submitWork)
curl -X POST --data '{"jsonrpc": "2.0", "method": "mnr_submitBitcoinBlock", "params": ["010000309821be091716ff34ddd54dd79a5d26af10a4214229b78b6e89d490360c000000eb436828fd1883ca69c1c6876174412da9f58f4848a29d7f4d698a7d09eaed593497ee58ffff7f2021393df40101000000010000000000000000000000000000000000000000000000000000000000000000ffffffff1f021402043497ee5808f8000002000000000d2f72736b5f7374726174756d2f000000000240be4025000000001976a914e5e9208d759e89a2e1767f5baeda58f188da206a88ac00000000000000002952534b424c4f434b3a3be5d1c4427993f22f985ff8e99a2b8560b2d1205580867e4eec21123315213b00000000"], "id": 1}' -H "Content-Type:application/json" 127.0.0.1:4444

```

<a id="markdown-2-参考资料" name="2-参考资料"></a>
# 2. 参考资料

* https://github.com/rsksmart/rskj/wiki/Configure-your-RSK-node-to-be-used-from-a-merge-mining-pool (配置可以挖矿)
* https://github.com/rsksmart/rskj/wiki/JSON-RPC-API (挖矿RPC)
* https://github.com/rsksmart/rskj/wiki/JSON-RPC-API-compatibility-matrix (JSON API 列表)
