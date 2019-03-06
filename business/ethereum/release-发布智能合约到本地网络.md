<!-- TOC -->

- [1. 说明](#1-说明)
- [2. truffle](#2-truffle)
- [3. console](#3-console)
- [5. remix](#5-remix)
- [6. 参考资料](#6-参考资料)

<!-- /TOC -->


<a id="markdown-1-说明" name="1-说明"></a>
# 1. 说明

参考之前的文章<私有链>,搭建本地挖矿环境.

注意需要开启rpc接口

```bash
geth --datadir /mnt/disk1/linux/env/ethereum/data1 --networkid 1108 --rpc --rpccorsdomain "*"
```

使用账号:

```bash
# bx seed -b 128 | bx mnemonic-new
elevator across vital picnic pluck save guitar series matter purse rude brave

# m/44'/60'/0'/0/0
# seed=`bx mnemonic-to-seed --language en elevator across vital picnic pluck save guitar series matter purse rude brave`
# bx hd-new $seed | bx hd-private -d -i 44 | bx hd-private -d -i 60 | bx hd-private -d -i 0 | bx hd-private -i 0 | bx hd-private -i 0 | bx hd-to-ec

私钥: 99cb1d7c7d7ee79464e24a564bcf36fbb8e7e8c104f28612e723e6f2453e5f38
公钥: 9cb23cd80ba24954c49152ca9afc6fe7798eb009dee47064ffd8ebd055a6c1a3403e60665d61a6455c56fdd37ab5d5f8514865bb2f47a79728f227cafa9e7b82
地址: 1b563a38e5f6c6d9fa9206cca6390912de3f1d7d
```

底层rpc: 在代码中下段跟踪,会发现都调用了SendTransaction. 关键参数是: 

* from: 哪个eth地址发布的
* gasPrice: gas值多少个eth
* gas: gas 上限
* data: 合约

<a id="markdown-2-truffle" name="2-truffle"></a>
# 2. truffle

```bash
# 因为部署是通过正式以太坊的接口的,所以需要私钥来进行签名. 而私钥是在以太坊的钱包内的,通过接口解锁指定私钥一段时间即可. 

cat >> /mnt/disk1/linux/reference/test/turffletest/truffle-config.js << EOF
var HDWalletProvider = require("truffle-hdwallet-provider");
var mnemonic = 'elevator across vital picnic pluck save guitar series matter purse rude brave'

module.exports = {
  networks: {
    local: {
      provider: function() {
        return new HDWalletProvider(mnemonic, "http://127.0.0.1:8545")
      },
      network_id: 1108,
      gas: 2500000,
      gasPrice: 183000
    }   
  }
};
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
solc --bin SimpleStorage.sol 
solc --abi SimpleStorage.sol 

# 命令行发布 (版本注意了)
npm install web3@0.20.1 --save
npm install ethereumjs-tx --save

# 打开命令行
node

```

<a id="markdown-5-remix" name="5-remix"></a>
# 5. remix

* https://remix.ethereum.org

```bash
# 在web页面上编写合约,编译,发布  (连接到127.0.0.1:8545)
```

<a id="markdown-6-参考资料" name="6-参考资料"></a>
# 6. 参考资料

* https://ethereum.stackexchange.com/questions/3149/how-do-you-get-a-json-file-abi-from-a-known-contract-address (如何编译获得abi和bin)
* https://ethereum.stackexchange.com/questions/28870/whats-next-after-compiling-using-solidity-compiler-command-line-and-getting-the (如何使用js库发布合约)
* https://github.com/ethereum/wiki/wiki/JavaScript-API#web3-javascript-app-api-for-02xx (web3js 0.2说明)
* https://github.com/ethereum/web3.js/tree/v0.20.6 (web3js 0.2)
* https://ethereum.stackexchange.com/questions/42185/how-to-call-contract-method-using-sendrawtransaction (console 发智能合约)
* https://ethereum.stackexchange.com/questions/8736/how-to-call-my-contracts-function-using-sendtransaction (console调用智能合约函数)
  