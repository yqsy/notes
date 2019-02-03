<!-- TOC -->

- [1. 说明](#1-说明)
- [2. 发布合约到开发环境](#2-发布合约到开发环境)
- [3. 部署到rsk测试网络 (分层钱包)](#3-部署到rsk测试网络-分层钱包)
- [4. 参考资料](#4-参考资料)

<!-- /TOC -->


<a id="markdown-1-说明" name="1-说明"></a>
# 1. 说明

本文介绍一下如何将solidity智能合约部署到本地开发环境以及rsk测试网络.

<a id="markdown-2-发布合约到开发环境" name="2-发布合约到开发环境"></a>
# 2. 发布合约到开发环境

```bash
npm install truffle -g

cd /mnt/disk1/linux/reference/test
mkdir turffletest
cd turffletest
truffle init

# 创建合约 & 部署js & 单元测试
truffle create contract SimpleStorage
truffle create migration SimpleStorage
truffle create test SimpleStorage
```

合约复制到`./contracts/SimpleStorage.sol`:
```solidity
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
```

部署脚本复制到`./migrations/xxx_simple_storage.js`
```javascript
var SimpleStorage = artifacts.require("./SimpleStorage.sol");

module.exports = function(deployer) {
  deployer.deploy(SimpleStorage);
};
```

编译 & 部署
```bash
# 部署到开发环境
truffle develop

# 编译
compile

# 部署
migrate

# 获取实例
var simpleStorage
SimpleStorage.deployed().then(instance => simpleStorage = instance)

# 查看
simpleStorage.get().then(bn => bn.toNumber())

# 修改
simpleStorage.set(10)

# 再查看
simpleStorage.get().then(bn => bn.toNumber())

```

<a id="markdown-3-部署到rsk测试网络-分层钱包" name="3-部署到rsk测试网络-分层钱包"></a>
# 3. 部署到rsk测试网络 (分层钱包)

给`truffle-concig.js`增加部署环境:

* https://iancoleman.io/bip39/ (获取助记词)

```js
var HDWalletProvider = require('truffle-hdwallet-provider')

var mnemonic = 'ocean credit monitor scorpion must yard like cram foster blade system devote'
var publicNode = 'https://public-node.testnet.rsk.co:443'

module.exports = {
  networks: {
    rsk: {
      provider: () =>
        new HDWalletProvider(mnemonic, publicNode),
      network_id: '*',
      gas: 2500000,
      gasPrice: 183000
    }
  }
}
```

部署命令:

* https://faucet.testnet.rsk.co/ (给测试网络rsk地址充值)
* https://explorer.testnet.rsk.co/ (测试网浏览器)
* https://explorer.testnet.rsk.co/address/0xc4b5cf245e903ce3d72796951f5380fdfbe57744 (查询余额)

```bash
npm install truffle-hdwallet-provider --save

# 打开rsk网络的控制台
truffle console --network rsk

# 获取区块
web3.eth.getBlockNumber((err, res) => console.log(res))

# 钱包
web3.currentProvider.wallets

# 获取一个账号 m/44'/60'/0'/0/0
# 0x694ec0cbe8f82798c650ca8546f9961b128dbdc25860c24769eab85b7f326b06 (私钥)
# 0xc4b5cf245e903ce3d72796951f5380fdfbe57744 (地址)
var account = Object.keys(web3.currentProvider.wallets)[0]

# 查看帐号
account

# 到faucet充值

# 查询余额
# web3.eth.getBalance(account, (err, res) => console.log(res.toNumber()))
web3.eth.getBalance(account)

# 编译
compile

# 部署
migrate --reset

SimpleStorage.deployed().then(instance => contract = instance)

# 调用接口
contract.set(1)


contract.get()
```

<a id="markdown-4-参考资料" name="4-参考资料"></a>
# 4. 参考资料

* https://truffleframework.com/docs/truffle/reference/truffle-commands
* https://github.com/rsksmart/tutorials/wiki/Module-0-%E2%80%93-A-little-about-DApps-and-Smart-Contracts-(10-minutes) (完整流程) 

