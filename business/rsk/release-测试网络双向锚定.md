---
title: 双向锚定
date: 2018-09-06 10:33:42
categories: [business, rsk]
---


<!-- TOC -->

- [1. 说明](#1-说明)
- [2. BTC-RBTC](#2-btc-rbtc)
- [3. RBTC-BTC](#3-rbtc-btc)
- [4. 参考资料](#4-参考资料)

<!-- /TOC -->

<a id="markdown-1-说明" name="1-说明"></a>
# 1. 说明

之前<发布智能合约>使用的RBTC是通过faucet直接获取的.本文介绍一下如何将BTC转换成RBTC,并且如何从RBTC转换成BTC.

<a id="markdown-2-btc-rbtc" name="2-btc-rbtc"></a>
# 2. BTC-RBTC

(1) 获取比特币测试网络地址:

* https://iancoleman.io/bip39/#english

```bash
# 我们取助记词 recipe truly salute identify student sick happy charge mouse ranch exotic panic 的 m/44'/1'/0'/0/0

P2PKH地址: n4k9FudCGqwAkNRYhvwKiMzD9WM84ckdNh
私钥WIF: cUwwf5969qwsTAnruFsMHSZhWZ2mAnK2G5TNXFH9QCBsstm3vFLM
```

(2) 给比特币测试网络地址充值:

* https://coinfaucet.eu/en/btc-testnet/ (充值)
* https://live.blockcypher.com/btc-testnet/address/n4k9FudCGqwAkNRYhvwKiMzD9WM84ckdNh/ (查询余额)


(3) 在MyCrypto中获取锚定的P2SH地址:

* https://mycrypto.com/

```bash
# 固定的P2SH锁定地址
2N1N5mdHWmRUfv49f7GnUeFfuyLcBQK7hj2
```

(4) 向比特币P2SH地址打款 (使用bitpay选择testnet网络)

* https://github.com/bitpay/copay/releases
* https://bitpay.com/wallet (snap-不行)
* https://docs.snapcraft.io/installing-snap-on-manjaro-linux/6807 (snap-不行)

```bash
yaourt -S --noconfirm copay
```

(5) 将比特币私钥转换成rsk私钥

* https://utils.rsk.co/
* https://github.com/rsksmart/utils (源码)

```bash
RSK Private Key: dbca0a7ef597cbfed214a08d4e94ffee794edaea8d47b504c8a3dd521785d067
RSK Address: 2340482f28897774204f40aa205497dc1be74d45
```

(6) 查询

* https://explorer.testnet.rsk.co/ (查询rsk的余额度)


<a id="markdown-3-rbtc-btc" name="3-rbtc-btc"></a>
# 3. RBTC-BTC


<a id="markdown-4-参考资料" name="4-参考资料"></a>
# 4. 参考资料

* https://github.com/rsksmart/rskj/wiki/BTC-RBTC-conversion (相互转换说明)
* https://github.com/rsksmart/rskj/wiki/Whitelisting-in-RSK (白名单说明)
* https://en.bitcoin.it/wiki/List_of_address_prefixes (比特币地址前缀)
* https://en.bitcoin.it/wiki/Testnet (bitcoin testnet wiki)
* https://gitter.im/rsksmart/getting-started (gitter群-求助把P2PKH地址加入到白名单)
