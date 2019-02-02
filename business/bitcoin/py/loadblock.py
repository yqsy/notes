import os
import sys

from impl.block import *


def main():
    if len(sys.argv) < 2:
        print("usage: loadblock.py *.blk")
        exit(0)

    with open(sys.argv[1], 'rb') as stream:

        while True:
            if stream.tell() == os.fstat(stream.fileno()).st_size:
                break

            block = Block(stream)

            if block.isMagicZero():
                break

            if not block.isMagicNoValid():
                raise Exception("error")

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
