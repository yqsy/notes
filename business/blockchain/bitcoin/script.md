

<!-- TOC -->

- [1. 说明](#1-说明)

<!-- /TOC -->

# 1. 说明



Multisig outputs (BIP 11)

```bash
# scriptPubKey (prev out)
OP_CHECKMULTISIG
n
{pubkey}...{pubkey}
m

# scriptSig (in)
...signatures...
OP_0
```

Transaction Puzzle (猜谜吗)

```bash
# scriptPubKey (prev out)
OP_EQUAL
<given_hash>
OP_HASH256

# scriptSig (in)
<data> ?
```


Incentivized finding of hash collisions

```bash
# scriptPubKey (prev out)
OP_EQUAL
OP_SHA1
OP_SWAP
OP_SHA1
OP_VERIFY
OP_NOT
OP_EQUAL
OP_2DUP

# scriptSig (in)
<preimage2>
<preimage1>
```

