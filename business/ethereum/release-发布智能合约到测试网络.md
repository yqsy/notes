<!-- TOC -->

- [1. 说明](#1-说明)
- [2. turffle](#2-turffle)
- [3. console](#3-console)
- [4. remix](#4-remix)
- [5. 参考资料](#5-参考资料)

<!-- /TOC -->


<a id="markdown-1-说明" name="1-说明"></a>
# 1. 说明


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

<a id="markdown-2-turffle" name="2-turffle"></a>
# 2. turffle

```bash
cat >> /mnt/disk1/linux/reference/test/turffletest/truffle-config.js << EOF
var HDWalletProvider = require("truffle-hdwallet-provider");
var mnemonic = 'elevator across vital picnic pluck save guitar series matter purse rude brave'

module.exports = {
  networks: {
    ropsten: {
      provider: function() {
        return new HDWalletProvider(mnemonic, "https://ropsten.infura.io/v3/50a4afb18ee44d649ad9548c1828ca79")
      },
      network_id: 3
    }   
  }
};
EOF

truffle console --network ropsten
# 编译 & 部署
compile
migrate
```

<a id="markdown-3-console" name="3-console"></a>
# 3. console

```bash

cd /mnt/disk1/linux/reference/test

var Web3 = require('web3');
const web3 = new Web3('http://localhost:8545');
var version = web3.version.api;
console.log(version); 

```

<a id="markdown-4-remix" name="4-remix"></a>
# 4. remix

* https://remix.ethereum.org

```bash
# 和meta mask 进行交互
```

<a id="markdown-5-参考资料" name="5-参考资料"></a>
# 5. 参考资料

* https://infura.io/ (infura)
* https://truffleframework.com/tutorials/using-infura-custom-var publicNode = 'https://public-node.testnet.rsk.co:443'发布到infura)
* https://github.com/trufflesuite/truffle-hdwallet-provider (truffle-hdwallet-provider 模块说明)
* https://faucet.ropsten.be/ (充钱)
* https://faucet.metamask.io/ (充钱)
