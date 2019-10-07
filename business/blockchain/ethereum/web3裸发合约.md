<!-- TOC -->

- [1. 说明](#1-说明)
- [2. 参考资料](#2-参考资料)

<!-- /TOC -->

# 1. 说明
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

```


```js
// 打开命令行
node

var Web3 = require('web3');
var ethTx = require('ethereumjs-tx');
var web3 = new Web3(new Web3.providers.HttpProvider("http://localhost:8545"));

// 生成合约二进制,并把合约二进制放到交易内
CONTRACT_BINARY="0x60806040523480156100115760006000fd5b505b33600060006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff1602179055505b61005a565b610130806100696000396000f3fe608060405234801560105760006000fd5b506004361060365760003560e01c806360fe47b114603c5780636d4ce63c146068576036565b60006000fd5b60666004803603602081101560515760006000fd5b81019080803590602001909291905050506084565b005b606e60ea565b6040518082815260200191505060405180910390f35b600060009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff16141560e6578060016000508190909055505b5b50565b6000600160005054905060f8565b9056fea265627a7a723158205225946d76d6689f8080d59b1a926a9be0731dcc62f9bda18de6852a4c2df33964736f6c634300050b0032";
CONTRACT_ABI=[{"constant":false,"inputs":[{"internalType":"uint256","name":"n","type":"uint256"}],"name":"set","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"get","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"}]
var contract = web3.eth.contract(CONTRACT_ABI);
var contractData = contract.new.getData({data: CONTRACT_BINARY});
var number = web3.eth.getTransactionCount("0xC8Fcd57eDe5C1633172e130ED95F2Ba3f5fe98D0");
var txParams = { nonce: web3.toHex(number), gasPrice: web3.toHex(183000),gasLimit: web3.toHex(2500000),from: '0xC8Fcd57eDe5C1633172e130ED95F2Ba3f5fe98D0',value: '0x00', data: contractData};

// 签名交易
// var tx = new ethTx(txParams);
var tx = new ethTx.Transaction(txParams);

var privKey = Buffer.from('224ed4e9e740fdd972f467885ef70ef31abeed7dba0c1edb20b63de2b5e21cf6', 'hex');
tx.sign(privKey);
var serializedTx = tx.serialize();
var rawTx = '0x' + serializedTx.toString('hex');

// 发送交易
var TXID=web3.eth.sendRawTransaction(rawTx);
var contractAddress=web3.eth.getTransactionReceipt(TXID).contractAddress;

// 使用函数使用
var contractInstance = contract.at(contractAddress);
var callSetData = contractInstance.set.getData(100)
var number = web3.eth.getTransactionCount("0xC8Fcd57eDe5C1633172e130ED95F2Ba3f5fe98D0");
var txParams = { 
    nonce: web3.toHex(number),
    gasPrice: web3.toHex(2500000), 
    gasLimit: web3.toHex(6800000),
    from: '0xC8Fcd57eDe5C1633172e130ED95F2Ba3f5fe98D0', 
    to: contractAddress,
    value: '0x00', 
    data: callSetData};

// 签名函数使用
var tx = new ethTx.Transaction(txParams);
var privKey = Buffer.from('224ed4e9e740fdd972f467885ef70ef31abeed7dba0c1edb20b63de2b5e21cf6', 'hex');
tx.sign(privKey);
var serializedTx = tx.serialize();
var rawTx = '0x' + serializedTx.toString('hex');

// 发送函数使用
// var TXID=web3.eth.sendRawTransaction(rawTx);
// web3.eth.getTransactionReceipt(TXID)



// 查看
contractInstance.get();

// TODO 调用不成功
```

# 2. 参考资料

* https://github.com/ethereum/wiki/wiki/JavaScript-API#web3-javascript-app-api-for-02xx (web3js 0.2说明)
* https://github.com/ethereum/web3.js/tree/v0.20.6 (web3js 0.2)
* https://ethereum.stackexchange.com/questions/42185/how-to-call-contract-method-using-sendrawtransaction (console 发智能合约)
* https://ethereum.stackexchange.com/questions/8736/how-to-call-my-contracts-function-using-sendtransaction (console调用智能合约函数)
  