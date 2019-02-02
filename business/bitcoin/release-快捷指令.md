

<!-- TOC -->

- [1. 说明](#1-说明)
- [2. 将命令行放到zshrc](#2-将命令行放到zshrc)

<!-- /TOC -->


<a id="markdown-1-说明" name="1-说明"></a>
# 1. 说明

对比特币的常用指令进行包装,方便日常的使用

<a id="markdown-2-将命令行放到zshrc" name="2-将命令行放到zshrc"></a>
# 2. 将命令行放到zshrc

```bash
wget -O ~/.bitcoincmd.rc https://raw.githubusercontent.com/yqsy/notes/master/business/bitcoin/script/bitcoincmd.rc

cat >> ~/.zshrc << EOF
source ~/.bitcoincmd.rc
EOF
```
