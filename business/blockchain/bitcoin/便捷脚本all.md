<!-- TOC -->

- [1. 说明](#1-说明)

<!-- /TOC -->


# 1. 说明

在做实验时方便使用的指令:

```bash
# bx
wget https://github.com/libbitcoin/libbitcoin-explorer/releases/download/v3.2.0/bx-linux-x64-qrcode
sudo mv bx-linux-x64-qrcode /usr/local/bin/bx
chmod +x /usr/local/bin/bx

# 隔离见证地址
sudo wget -O /usr/local/bin/getsegwitaddr https://raw.githubusercontent.com/yqsy/notes/master/business/blockchain/bitcoin/script/getsegwitaddr

sudo chmod +x /usr/local/bin/getsegwitaddr

# 地址
wget -O $HOME/.bitcoinaddress.rc https://raw.githubusercontent.com/yqsy/notes/master/business/blockchain/bitcoin/script/bitcoinaddress.rc

# 快捷指令
wget -O $HOME/.bitcoincmd.rc https://raw.githubusercontent.com/yqsy/notes/master/business/blockchain/bitcoin/script/bitcoincmd.rc

cat >> $HOME/.zshrc << EOF
source $HOME/.bitcoinaddress.rc
EOF

cat >> $HOME/.zshrc << EOF
source $HOME/.bitcoincmd.rc
EOF

```
