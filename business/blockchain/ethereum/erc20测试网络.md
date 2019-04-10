<!-- TOC -->

- [1. truffle](#1-truffle)
- [2. remix + metamask](#2-remix--metamask)
- [3. erc20常用指令说明](#3-erc20常用指令说明)
- [4. 参考资料](#4-参考资料)

<!-- /TOC -->



<a id="markdown-1-truffle" name="1-truffle"></a>
# 1. truffle



<a id="markdown-2-remix--metamask" name="2-remix--metamask"></a>
# 2. remix + metamask


<a id="markdown-3-erc20常用指令说明" name="3-erc20常用指令说明"></a>
# 3. erc20常用指令说明

```bash
# 修改账户
web3.eth.defaultAccount = web3.eth.accounts[1]


# 所属者
contract.owner()

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

* https://github.com/OpenZeppelin/openzeppelin-solidity/blob/master/contracts/token/ERC20/ERC20.sol
* https://github.com/ConsenSys/Tokens
