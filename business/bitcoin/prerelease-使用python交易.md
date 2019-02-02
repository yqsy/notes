---
title: 使用python交易
date: 2018-02-01 13:29:12
categories: [business, bitcoin]
---


<!-- TOC -->

- [1. 说明](#1-说明)
- [2. 参考资料](#2-参考资料)

<!-- /TOC -->

<a id="markdown-1-说明" name="1-说明"></a>
# 1. 说明


```bash
# 拉取源代码 (应该作为库来管理,像nodejs一样指定版本,他这个有问题)
# 问题在于:   setup.py中  packages=find_packages(),  
mkdir -p /mnt/disk1/linux/reference/project/bitcointest
cd /mnt/disk1/linux/reference/project/bitcointest
mkdir lib && cd lib
git clone https://github.com/petertodd/python-bitcoinlib
cd ..

# 将.git删除,直接使用
rm -rf ./lib/python-bitcoinlib/.git

ln -s lib/python-bitcoinlib/bitcoin/ bitcoin

git init .
```

<a id="markdown-2-参考资料" name="2-参考资料"></a>
# 2. 参考资料

* https://github.com/petertodd/python-bitcoinlib

