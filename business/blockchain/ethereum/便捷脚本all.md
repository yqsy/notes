<!-- TOC -->

- [1. 说明](#1-说明)

<!-- /TOC -->


# 1. 说明

```bash
# sha3sum
cd /mnt/disk1/linux/reference/refer

git clone https://github.com/maandree/libkeccak
git clone https://github.com/maandree/sha3sum
cd libkeccak
make
sudo make install

cd ../sha3sum
make 
sudo make install

# 地址
wget -O $HOME/.ethereumaddress.rc https://raw.githubusercontent.com/yqsy/notes/master/business/blockchain/ethereum/script/ethereumaddress.rc


cat >> $HOME/.zshrc << EOF
source $HOME/.ethereumaddress.rc
EOF

```

