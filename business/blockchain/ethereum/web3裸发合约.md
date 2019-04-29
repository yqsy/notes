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

# 打开命令行
node

var Web3 = require('web3');
var ethTx = require('ethereumjs-tx');
var web3 = new Web3(new Web3.providers.HttpProvider("http://localhost:8545"));

// 生成合约二进制,并把合约二进制放到交易内
CONTRACT_BINARY="0x608060405234801561001057600080fd5b50336000806101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff160217905550610113806100606000396000f3fe6080604052348015600f57600080fd5b506004361060325760003560e01c806360fe47b11460375780636d4ce63c146062575b600080fd5b606060048036036020811015604b57600080fd5b8101908080359060200190929190505050607e565b005b606860dd565b6040518082815260200191505060405180910390f35b6000809054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff16141560da57806001819055505b50565b600060015490509056fea165627a7a723058203f8d2e22f896e984802e219178a4b53194ec95eb0f1cc92fb1541453b290c2d80029";
CONTRACT_ABI=[{"constant":false,"inputs":[{"name":"n","type":"uint256"}],"name":"set","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"get","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"}]
var contract = web3.eth.contract(CONTRACT_ABI);
var contractData = contract.new.getData({data: CONTRACT_BINARY});
var number = web3.eth.getTransactionCount("0x1b563a38e5f6c6d9fa9206cca6390912de3f1d7d");
var txParams = { nonce: web3.toHex(number), gasPrice: web3.toHex(183000),gasLimit: web3.toHex(2500000),from: '0x1b563a38e5f6c6d9fa9206cca6390912de3f1d7d',value: '0x00', data: contractData};

// 签名交易
var tx = new ethTx(txParams);
var privKey = Buffer.from('99cb1d7c7d7ee79464e24a564bcf36fbb8e7e8c104f28612e723e6f2453e5f38', 'hex');
tx.sign(privKey);
var serializedTx = tx.serialize();
var rawTx = '0x' + serializedTx.toString('hex');

// 发送交易
var TXID=web3.eth.sendRawTransaction(rawTx);
var contractAddress=web3.eth.getTransactionReceipt(TXID).contractAddress;

// 使用函数使用
var contractInstance = contract.at(contractAddress);
var callSetData = contractInstance.set.getData(10)
var number = web3.eth.getTransactionCount("0x1b563a38e5f6c6d9fa9206cca6390912de3f1d7d");
var txParams = { nonce: web3.toHex(number), gasPrice: web3.toHex(183000),gasLimit: web3.toHex(2500000),from: '0x1b563a38e5f6c6d9fa9206cca6390912de3f1d7d', to: contractAddress,value: '0x00', data: callSetData};

// 签名函数使用
var tx = new ethTx(txParams);
var privKey = Buffer.from('99cb1d7c7d7ee79464e24a564bcf36fbb8e7e8c104f28612e723e6f2453e5f38', 'hex');
tx.sign(privKey);
var serializedTx = tx.serialize();
var rawTx = '0x' + serializedTx.toString('hex');

// 发送函数使用
var TXID=web3.eth.sendRawTransaction(rawTx);
web3.eth.getTransactionReceipt(TXID)

// 查看
contractInstance.get();

// TODO 调用不成功
```

# 2. 参考资料

* https://github.com/ethereum/wiki/wiki/JavaScript-API#web3-javascript-app-api-for-02xx (web3js 0.2说明)
* https://github.com/ethereum/web3.js/tree/v0.20.6 (web3js 0.2)
* https://ethereum.stackexchange.com/questions/42185/how-to-call-contract-method-using-sendrawtransaction (console 发智能合约)
* https://ethereum.stackexchange.com/questions/8736/how-to-call-my-contracts-function-using-sendtransaction (console调用智能合约函数)
  