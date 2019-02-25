<!-- TOC -->

- [1. 说明](#1-说明)
- [2. truffle](#2-truffle)
- [3. console](#3-console)
- [4. postman](#4-postman)
- [5. remix](#5-remix)

<!-- /TOC -->


<a id="markdown-1-说明" name="1-说明"></a>
# 1. 说明

参考之前的文章<私有链>,搭建本地挖矿环境.

<a id="markdown-2-truffle" name="2-truffle"></a>
# 2. truffle

```bash
# 因为部署是通过正式以太坊的接口的,所以需要私钥来进行签名. 而私钥是在以太坊的钱包内的,通过接口解锁指定私钥一段时间即可. 

# 通过console连接到网络
web3.personal.unlockAccount('5351b0ead94e9d5cb69798e1cbc2af99e6764eb7', '123456', 36000)

cat >> /mnt/disk1/linux/reference/test/turffletest/truffle-config.js << EOF
module.exports = {
  networks: {
    local: {
      host: "127.0.0.1",
      port: 8545,             // Custom port
      network_id: '*',       // Custom network
      gas: 6700000,           // Gas sent with each transaction (default: ~6700000)
      gasPrice: 100000000000,  // 20 gwei (in wei) (default: 100 gwei)
      from: '5351b0ead94e9d5cb69798e1cbc2af99e6764eb7',        // Account to send txs from (default: accounts[0])
    },
  }
}
EOF

# 打开控制台  (以太坊本地网rpc,监听8545)
truffle console --network local

# 编译 & 部署
compile
migrate
```

<a id="markdown-3-console" name="3-console"></a>
# 3. console

```bash
# 下载编译器
yaourt -S --noconfirm solidity-git

# 生成源码
cd /mnt/disk1/linux/reference/test
mkdir solctest
cat > /mnt/disk1/linux/reference/test/solctest/SimpleStorage.sol << EOF
pragma solidity >=0.4.21 <0.6.0;

contract SimpleStorage {
    address private deployer;
    uint private storedData;

    constructor() public {
        deployer = msg.sender;
    }

    function set(uint n) public {
        if(msg.sender == deployer)
            storedData = n;
    }

    function get() public view returns (uint) {
        return storedData;
    }
}
EOF

# 编译
# 为什么会提示我下面这个,难道不能用吗?
# Warning: This is a pre-release compiler version, please do not use it in production.
```


<a id="markdown-4-postman" name="4-postman"></a>
# 4. postman

```bash
# 和console应该是一样的,调用eth_sendTransaction的接口,但是为什么会提示那一串字符串?不能用吗
```

<a id="markdown-5-remix" name="5-remix"></a>
# 5. remix

* https://remix.ethereum.org

```bash
# 开启私有链的时候请注意打开rpc
geth --datadir /mnt/disk1/linux/env/ethereum/data1 --networkid 1108 --rpc --rpccorsdomain "*"

# 在web页面上编写合约,编译,发布  (连接到127.0.0.1:8545)
```
