<!-- TOC -->

- [1. 说明](#1-说明)

<!-- /TOC -->


<a id="markdown-1-说明" name="1-说明"></a>
# 1. 说明

```bash
# sha3sum
cd /mnt/disk1/linux/reference/refer

git clone https://github.com/maandree/libkeccak
cd libkeccak
make
sudo make install

cd ../sha3sum
make 
sudo make install

# 地址
wget -O ~/.ethereumaddress.rc https://raw.githubusercontent.com/yqsy/notes/master/business/ethereum/script/ethereumaddress.rc


cat >> ~/.zshrc << EOF
source ~/.ethereumaddress.rc
EOF

```

