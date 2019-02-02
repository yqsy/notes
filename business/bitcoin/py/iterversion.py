import sys

from impl.index import *


def main():
    if len(sys.argv) < 3:
        print("usage: iterversion.py {basedirectory} {indexdirectory}")
        exit(0)

    versionHeightsMap = {}

    blockIndexs = getblockIndexs(sys.argv[2])

    for blockIndex in blockIndexs:
        if blockIndex.nVersion not in versionHeightsMap:
            heights = []
            heights.append(blockIndex.nHeight)
            versionHeightsMap[blockIndex.nVersion] = heights
        else:
            versionHeightsMap[blockIndex.nVersion].append(blockIndex.nHeight)

    for k, v in versionHeightsMap.items():
        print("version: {0:12x} num: {1:8d} firstHeight: {2:8d} lastHeight: {3:8d}".format(k, len(v), v[0],
                                                                                           v[len(v) - 1]))


if __name__ == "__main__":
    main()
