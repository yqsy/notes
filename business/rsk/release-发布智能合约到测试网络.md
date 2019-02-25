<!-- TOC -->

- [1. truffle](#1-truffle)
- [2. console](#2-console)
- [3. postman](#3-postman)
- [4. remix](#4-remix)
- [5. 参考资料](#5-参考资料)

<!-- /TOC -->


<a id="markdown-1-truffle" name="1-truffle"></a>
# 1. truffle

给`truffle-concig.js`增加部署环境:

* https://iancoleman.io/bip39/ (获取助记词)

```bash
cat >> /mnt/disk1/linux/reference/test/turffletest/truffle-config.js << EOF
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
EOF
```

部署命令:

* https://faucet.testnet.rsk.co/ (给测试网络rsk地址充值)
* https://explorer.testnet.rsk.co/ (测试网浏览器)
* https://explorer.testnet.rsk.co/address/0xc4b5cf245e903ce3d72796951f5380fdfbe57744 (查询余额)

```bash
npm init
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

<a id="markdown-2-console" name="2-console"></a>
# 2. console

<a id="markdown-3-postman" name="3-postman"></a>
# 3. postman

<a id="markdown-4-remix" name="4-remix"></a>
# 4. remix

<a id="markdown-5-参考资料" name="5-参考资料"></a>
# 5. 参考资料

* https://truffleframework.com/docs/truffle/reference/truffle-commands
* https://github.com/rsksmart/tutorials/wiki/Module-0-%E2%80%93-A-little-about-DApps-and-Smart-Contracts-(10-minutes) (完整流程) 
* https://github.com/rsksmart/rskj/wiki/rsk-public-nodes (测试网络开放的权限)
