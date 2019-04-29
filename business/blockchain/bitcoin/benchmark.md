<!-- TOC -->

- [1. 说明](#1-说明)

<!-- /TOC -->

# 1. 说明

```bash
bitcoind -fallbackfee=0.0002
```

测试: 

```bash
bg 1000

TMPSEED=`bx seed | bx ec-new`
TMPINFO=`parse_privkey $TMPSEED`
TMPADDR=`echo $TMPINFO | sed -n 13p | awk '{print $2}'`
echo $TMPADDR

for i in `seq 1 8000`; do
bitcoin-cli sendtoaddress $TMPADDR 1.00 "" "" true
done
```
