


<!-- TOC -->

- [1. 说明](#1-说明)
- [2. 实践智能合约](#2-实践智能合约)
    - [2.1. truffle](#21-truffle)
    - [2.2. remix](#22-remix)

<!-- /TOC -->

<a id="markdown-1-说明" name="1-说明"></a>
# 1. 说明

* http://www.tryblockchain.org/Solidity-source-mapping.html (solidity 语法说明)
* https://openzeppelin.org/api/docs/get-started.html (solidity安全合约的使用说明)
* https://openzeppelin.org/api/docs/learn-about-tokens.html (openzeppelin关于token的说明)

---
* https://github.com/ethereum/wiki/wiki/JavaScript-API (js api)
* https://github.com/eoshackathon/ipfs_development_tutorial (古哥培训教程)
* https://www.ethereum.org/greeter (开发入门)
* http://ethdocs.org/en/latest/contracts-and-transactions/contracts.html (什么是合约)
* https://solidity.readthedocs.io/en/latest/ (所用语言,类似js)
* https://github.com/ethereum/dapp-bin (示例)
* https://ethereum.org/token#the-code (货币)
* https://ethereum.org/crowdsale#the-code (去中心知识库)

---
* http://blockchainlab.com/pdf/Ethereum_white_paper-a_next_generation_smart_contract_and_decentralized_application_platform-vitalik-buterin.pdf (论文)


<a id="markdown-2-实践智能合约" name="2-实践智能合约"></a>
# 2. 实践智能合约

<a id="markdown-21-truffle" name="21-truffle"></a>
## 2.1. truffle



127.0.0.1:9545
```bash
npm install -g truffle
mkdir testtruffle && cd testtruffle
truffle init
npm init -y
npm install --save-exact openzeppelin-solidity@next
# contracts 目录写合约
# migrations 目录写部署脚本
truffle develop
# 编译
compile
# 部署
migrate
# 重新部署
migrate --reset

# 加载合约
StagesToken.deployed().then(instance => contract = instance)
```

127.0.0.1:8545
```bash
# testrpc
npm install -g ethereumjs-testrpc

truffle compile
truffle migrate
truffle console
```

127.0.0.1:7545 (web测试 ganache)
```bash
truffle unbox webpack

truffle compile
truffle migrate --network ganache
truffle test
npm run lint
npm run dev
npm run build
    
```


发布到ropsten
```bash
# 安装infura.io
npm install truffle-hdwallet-provider --save

# 部署至ropsten
truffle develop
compile
migrate --network ropsten

# 替换合约
migrate --reset --network ropsten
```

truffle.js配置
```
var HDWalletProvider = require("truffle-hdwallet-provider");

var infura_apikey = "50a4afb18ee44d649ad9548c1828ca79";
var mnemonic = "embody save subway region brass benefit eager bike advice ocean favorite have";

module.exports = {
    networks: {
        development: {
            host: "localhost",
            port: 8545,
            network_id: "*"
        },
        ropsten: {
            provider: new HDWalletProvider(mnemonic, "https://ropsten.infura.io/" + infura_apikey),
            network_id: 3,
            gas: 4500000
        }
    }
};
```


* contracts/: 开发者`编写`的智能合约
* migrations/: 用来存放`部署脚本`
* tests/: 用来存放`测试`文件
* truffle.js: Truffle `默认的配置文件`



<a id="markdown-22-remix" name="22-remix"></a>
## 2.2. remix

* https://github.com/ethereum/remix
* https://github.com/ethereum/remix-ide
* https://www.npmjs.com/package/remix-ide (安装方法)
* https://remix.ethereum.org/

```bash
npm install remix-ide -g

cd /mnt/disk1/linux/reference/project/testsol
remix-ide

```

智能合约属性:  
参考: https://github.com/ethereum/wiki/wiki/JSON-RPC#the-default-block-parameter
