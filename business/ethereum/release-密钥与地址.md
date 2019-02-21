<!-- TOC -->

- [1. 说明](#1-说明)
- [2. 助记词与分层钱包](#2-助记词与分层钱包)
- [3. 参考资料](#3-参考资料)

<!-- /TOC -->


<a id="markdown-1-说明" name="1-说明"></a>
# 1. 说明

以太坊的地址生成规则相较于比特币来的更简单一些.其规则如下.注意和比特币不同的是,在对公钥进行hash的时候,比特币有`压缩和未压缩的公钥`,分别为`33bytes和65bytes`,比特币使用sha256对两者进行hash产生公钥hash并通过BASE58生成钱包地址. 而在以太坊中没有压缩与未压缩的概念,只有`64bytes "裸"的公钥`,对其直接使用sha3产生地址.

```bash
私钥      ->      公钥     ->       地址  
     secp256k1         Keccak-256       
```

安装库:
```bash
cd /mnt/disk1/linux/reference/refer

git clone https://github.com/maandree/libkeccak
cd libkeccak
make
sudo make install

cd ../sha3sum
make 
sudo make install
```

提供以下shell脚本方便日常使用:

* parse_privkey_eth 解析私钥

指令:
```bash
# 私钥 -> 公钥 -> 地址:
parse_privkey_eth() {
    PRIKEY=$1
    PUBKEY=`bx ec-to-public -u $PRIKEY | sed 's/^04//'`
    ADDRESS=`echo -n $PUBKEY | keccak-256sum -x -l  | tr -d ' -' | tail -c 41`

    echo 私钥: $PRIKEY &&
    echo 公钥: $PUBKEY &&
    echo 地址: $ADDRESS
}

# 创建新私钥
parse_privkey_eth `bx seed | bx ec-new`
```

<a id="markdown-2-助记词与分层钱包" name="2-助记词与分层钱包"></a>
# 2. 助记词与分层钱包

```bash
# 从BIP39网页上生成助记词
# price wash dismiss peasant glass dress green border apple thing slight outside

# 转换成熵
seed=`bx mnemonic-to-seed --language en price wash dismiss peasant glass dress green border apple thing slight outside`

# hd私钥前缀为xprv
hd_prv=`bx hd-new $seed`

# hd公钥前缀为xpub
hd_pub=`bx hd-to-public $hd_prv`

# m/44'/60'/0'/0 的扩展密钥
change_prv=`echo $hd_prv | bx hd-private -d -i 44 | bx hd-private -d -i 60 | bx hd-private -d -i 0 | bx hd-private -i 0`
change_pub=`bx hd-to-public $change_prv`

# 生成每一层的私钥

# m/44'/60'/0'/0/0
echo $change_prv | bx hd-private -i 0 | bx hd-to-ec

# m/44'/60'/0'/0/9
echo $change_prv | bx hd-private -i 9 | bx hd-to-ec
```

<a id="markdown-3-参考资料" name="3-参考资料"></a>
# 3. 参考资料

* https://ethereum.stackexchange.com/questions/3542/how-are-ethereum-addresses-generated/3619#3619 (原理)
* https://iancoleman.io/bip39/ (BIP39生成)
* https://gist.github.com/miguelmota/3793b160992b4ea0b616497b8e5aee2f (指令生成地址)

---
* http://tomeko.net/online_tools/hex_to_file.php?lang=en (将hex转换为bytes文件(128hex=64bytes))
* https://emn178.github.io/online-tools/keccak_256_checksum.html (sha3文件)
* https://emn178.github.io/online-tools/keccak_256.html (sha3 hex)
