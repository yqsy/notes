from __future__ import absolute_import, division, print_function, \
    with_statement

import io
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../'))

from bitcoinhelper.impl.block import *


def main():
    if len(sys.argv) < 2:
        print("usage: parseblockbtc.py blockHex")
        exit(0)

    print("block hex: {}".format(sys.argv[1]))

    f = io.BytesIO(bytearray.fromhex(sys.argv[1]))

    block = Block(f, disablePrefix=True, pkcFlag=True)

    print("\n===block===")
    print(block)
    print(block.blockHeader)

    print("\n==transactions===")
    for i in range(len(block.vtx)):
        tx = block.vtx[i]
        print("\n===transaction[{0}]===".format(i))
        print(tx)

        for k in range(len(tx.vin)):
            print("\n===vin[{0}]===".format(k))
            print(tx.vin[k])

        for j in range(len(tx.vout)):
            print("\n===vout[{0}]===".format(j))
            print(tx.vout[j])

    print("")


if __name__ == "__main__":
    main()
