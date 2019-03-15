<!-- TOC -->

- [1. 说明](#1-说明)

<!-- /TOC -->


<a id="markdown-1-说明" name="1-说明"></a>
# 1. 说明

在做实验时方便使用的指令:

```bash
# bx
wget https://github.com/libbitcoin/libbitcoin-explorer/releases/download/v3.2.0/bx-linux-x64-qrcode
sudo mv bx-linux-x64-qrcode /usr/local/bin/bx
chmod +x /usr/local/bin/bx

# 隔离见证地址
sudo wget https://raw.githubusercontent.com/yqsy/notes/master/business/bitcoin/script/getsegwitaddr -O /usr/local/bin/getsegwitaddr
sudo chmod +x /usr/local/bin/getsegwitaddr

# 地址
wget -O ~/.bitcoinaddress.rc https://raw.githubusercontent.com/yqsy/notes/master/business/bitcoin/script/bitcoinaddress.rc

cat >> ~/.zshrc << EOF
source ~/.bitcoinaddress.rc
EOF

# 快捷指令
wget -O ~/.bitcoincmd.rc https://raw.githubusercontent.com/yqsy/notes/master/business/bitcoin/script/bitcoincmd.rc

cat >> ~/.zshrc << EOF
source ~/.bitcoincmd.rc
EOF

# 锁定脚本 => sha256 =>反转 => script hash
wget -O ~/.bitcoinscripthash.rc https://raw.githubusercontent.com/yqsy/notes/master/business/bitcoin/script/bitcoinscripthash.rc

cat >> ~/.zshrc << EOF
source ~/.bitcoinscripthash.rc
EOF

```
