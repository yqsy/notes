<!-- TOC -->

- [1. 说明](#1-说明)
- [2. 助记词与分层钱包](#2-助记词与分层钱包)
- [3. 参考资料](#3-参考资料)

<!-- /TOC -->


<a id="markdown-1-说明" name="1-说明"></a>
# 1. 说明

```bash
echo "0267572eaf952d22e131187a9651928df079ad24f7fb08324e70c0f161a3a604" | perl -pe 's/([0-9a-f]{2})/chr hex $1/gie'

0xcfaacda3ec2ebac1c7a55a77e907d73a4d2eac1b2c97346fc9e79c347bcb487c
0x020267572eaf952d22e131187a9651928df079ad24f7fb08324e70c0f161a3a604
0267572eaf952d22e131187a9651928df079ad24f7fb08324e70c0f161a3a6046f95b74777e42cf6a253eb5eaed9b2f02d87919bda09bbfdafa3ab96672951b0
0xd2bEB88CFcae4B5732B6F9c092090f7265E49b81

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
