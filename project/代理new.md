<!-- TOC -->

- [1. 说明](#1-说明)

<!-- /TOC -->

<a id="markdown-1-说明" name="1-说明"></a>
# 1. 说明

服务器:
```bash
mkdir -p ~/env
cd ~/env
git clone https://github.com/shadowsocks/shadowsocks
cd shadowsocks
git checkout tags/2.9.1
cd shadowsocks
python server.py -p 5000 -k xxx -m aes-256-cfb

mkdir -p ~/env/kcptun
cd ~/env/kcptun
wget https://github.com/xtaci/kcptun/releases/download/v20190325/kcptun-linux-amd64-20190325.tar.gz
tar -xvzf kcptun-linux-amd64-20190325.tar.gz 

./server_linux_amd64 -t "localhost:5000" -l ":5001" -mode fast2
```

客户端:
```bash
./client_linux_amd64 -l :25000 -r my_bwg1:5001 --mode fast2
```
