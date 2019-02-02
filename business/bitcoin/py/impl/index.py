from io import BytesIO
import struct


import plyvel

from impl.serialize import *

BLOCK_HAVE_DATA = 8
BLOCK_HAVE_UNDO = 16


class DBBlockIndex():
    def __init__(self, blkHashraw, dataRaw):
        self.hash = blkHashraw.hex()

        stream = BytesIO(dataRaw)

        self._nVersion = varInt(stream)
        self.nHeight = varInt(stream)
        self.nStatus = varInt(stream)
        self.nTx = varInt(stream)
        if self.nStatus & (BLOCK_HAVE_DATA | BLOCK_HAVE_UNDO):
            self.nFile = varInt(stream)
        if self.nStatus & BLOCK_HAVE_DATA:
            self.nDataPos = varInt(stream)
        if self.nStatus & BLOCK_HAVE_UNDO:
            self.nUndoPos = varInt(stream)

        # block header
        self.nVersion = uint4(stream)
        self.hashPrevBlock = hash32(stream)
        self.hashMerkleRoot = hash32(stream)
        self.nTime = uint4(stream)
        self.nBits = uint4(stream)
        self.nNonce = uint4(stream)


def getblockIndexs(indexDirectory):
    db = plyvel.DB(indexDirectory)
    blockIndexs = []
    for k, v in db.iterator():
        if k[0] == ord('b'):
            blockIndex = DBBlockIndex((k[1:])[::-1], v)
            blockIndexs.append(blockIndex)
    db.close()
    blockIndexs.sort(key=lambda x: x.nHeight)
    return blockIndexs
