import sys

from impl.index import *


def main():
    if len(sys.argv) < 3:
        print("usage: bip34versioncheck.py {basedirectory} {indexdirectory}")
        exit(0)

    blockIndexs = getblockIndexs(sys.argv[2])

    versionMap = {}

    # version1 最后一个区块227835
    # 则最有一个1000的区间是 226836 ~ 227835
    for i in range(226836, 227836):

        if blockIndexs[i].nVersion not in versionMap:
            versionMap[blockIndexs[i].nVersion] = 1
        else:
            versionMap[blockIndexs[i].nVersion] += 1

    for k, v in versionMap.items():
        print("{0} {1}".format(k, v))


if __name__ == "__main__":
    main()
