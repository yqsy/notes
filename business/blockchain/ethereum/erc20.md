<!-- TOC -->

- [1. truffle](#1-truffle)
- [2. remix + metamask](#2-remix--metamask)
- [3. erc20常用指令说明](#3-erc20常用指令说明)
- [4. 参考资料](#4-参考资料)

<!-- /TOC -->



<a id="markdown-1-truffle" name="1-truffle"></a>
# 1. truffle

```bash
cd /mnt/disk1/linux/reference/test
mkdir -p erc20test
cd erc20test

truffle init
npm init -y
npm install --save --save-exact openzeppelin-solidity

# 添加智能合约到./contracts, 添加部署脚本到./migrations, 注意文件名称和
# https://github.com/OpenZeppelin/openzeppelin-solidity/blob/master/contracts/examples/SimpleToken.sol

truffle create contract erc20
truffle create migration erc20

truffle develop
compile
migrate --reset
```

<a id="markdown-2-remix--metamask" name="2-remix--metamask"></a>
# 2. remix + metamask


<a id="markdown-3-erc20常用指令说明" name="3-erc20常用指令说明"></a>
# 3. erc20常用指令说明

```bash
# 修改账户
# web3.eth.defaultAccount = web3.eth.accounts[1]

Erc20_SB.deployed().then(instance => contract = instance)


# ERC20Detailed
contract.name()
contract.symbol()
contract.decimals()

# ERC20

# 1. 发行量
contract.totalSupply()

# 2. 某个账户的余额
contract.balanceOf(web3.eth.coinbase)
contract.balanceOf(web3.eth.accounts[1])

# 3. 查询允许别人花多少自己的钱
contract.allowance(web3.eth.coinbase,web3.eth.accounts[1]) 

# 4. 转账
contract.transfer(web3.eth.accounts[1], 5)

# 5. 允许别人转自己多少钱
contract.approve(web3.eth.accounts[1], 5)

# 6. 从from转到to(并且msg.sender必须有数额),并且需要(approve的)
contract.transferFrom(web3.eth.coinbase, web3.eth.accounts[1], 5)

# 7. 增加别人花自己钱的数量
contract.increaseAllowance(web3.eth.accounts[1], 5)

# 8. 减少别人花自己钱的数量
contract.increaseAllowance(web3.eth.accounts[1], 5)

# ERC20Burnable

# 1. 燃烧自己的
contract.burn(100)

# 2. 燃烧_allowed (并且msg.sender必须有数额)
contract.burnFrom(web3.eth.coinbase, 100)
```


<a id="markdown-4-参考资料" name="4-参考资料"></a>
# 4. 参考资料

* https://github.com/OpenZeppelin/openzeppelin-solidity(安装说明)
* https://github.com/OpenZeppelin/openzeppelin-solidity/blob/master/contracts/examples/SimpleToken.sol (引用OpenZeppelin发简单的币)
* https://github.com/ConsenSys/Tokens (3个文件,还是不够简单啊)
