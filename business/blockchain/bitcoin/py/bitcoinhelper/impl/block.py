from __future__ import absolute_import, division, print_function, \
    with_statement

from datetime import datetime
from bitcoinhelper.impl.script import *

import io
import struct

class BlockHeader:
    def __init__(self, stream, **kwargs):
        self.nVersion = uint4(stream)
        self.hashPrevBlock = hash32(stream)
        self.hashMerkleRoot = hash32(stream)
        self.nTime = uint4(stream)
        self.nBits = uint4(stream)
        self.nNonce = uint4(stream)

        self.pkcFlag = False
        for k in kwargs.keys():
            if k == "pkcFlag":
                self.pkcFlag = kwargs["pkcFlag"]

        if self.pkcFlag:
            self.cuckooNoncesCount = compactSize(stream)
            self.cuckooNonces = []
            for i in range(0, self.cuckooNoncesCount):
                self.cuckooNonces.append(uint4(stream))

    def __str__(self):
        rtn = "nVersion: 0x{0:x}\n".format(self.nVersion)
        rtn = rtn + "hashPrevBlock: 0x{0}\n".format(hashStr(self.hashPrevBlock))
        rtn = rtn + "hashMerkleRoot: 0x{0}\n".format(hashStr(self.hashMerkleRoot))
        rtn = rtn + "nTime: {0}\n".format(self.decodeTime(self.nTime))
        rtn = rtn + "nBits: 0x{0:x}\n".format(self.nBits)
        rtn = rtn + "nNonce: {0}".format(self.nNonce)

        if self.pkcFlag:
            rtn = rtn + "\ncuckooNonces: {"
            for i in range(0, self.cuckooNoncesCount):
                rtn = rtn + str(self.cuckooNonces[i]) + ","
            rtn = rtn + "}\n"
        return rtn

    def decodeTime(self, time):
        utcTime = datetime.utcfromtimestamp(time)
        return utcTime.strftime("%Y-%m-%d %H:%M:%S.%f+00:00 (UTC)")


class Block:
    def __init__(self, stream, **kwargs):
        self.disablePrefix = False
        self.rskFlag = False
        self.pkcFlag = False

        for k in kwargs.keys():
            if k == "disablePrefix":
                self.disablePrefix = kwargs["disablePrefix"]
            elif k == "rskFlag":
                self.rskFlag = kwargs["rskFlag"]
            elif k == "pkcFlag":
                self.pkcFlag = kwargs["pkcFlag"]

        if not self.disablePrefix:
            self.magicno = uint4(stream)
            self.blockSize = uint4(stream)
        else:
            self.magicno = None
            self.blockSize = None  # TODO

        self.blockHeader = BlockHeader(stream, pkcFlag=self.pkcFlag)

        self.txcount = compactSize(stream)
        self.vtx = []

        for i in range(0, self.txcount):
            if self.rskFlag and i == 0:
                # coinbase rsk second out lock script is RSKBLOCK:hash
                self.vtx.append(Tx(stream, True))
            else:
                self.vtx.append(Tx(stream, False))

    def isMagicNoValid(self):
        return self.magicno == 0xD9B4BEF9

    def isMagicZero(self):
        return self.magicno == 0x0

    def __str__(self):
        str = "blocksize: {0}\n".format(self.blockSize)
        str = str + "txcount: {0}".format(self.txcount)
        return str


class Tx:
    def __init__(self, stream, rskFlag):
        self.witness = False

        self.nVersion = uint4(stream)
        self.flags = 0
        self.readVin(stream)

        if len(self.vin) == 0:
            self.flags = uint1(stream)

            if self.flags != 0:
                self.readVin(stream)
                self.readVout(stream, rskFlag)
        else:
            self.readVout(stream, rskFlag)

        if self.flags & 1:
            self.flags ^= 1

            self.witness = True

            for i in range(0, len(self.vin)):
                self.vin[i].scriptWitnessCount = compactSize(stream)
                for j in range(0, self.vin[i].scriptWitnessCount):
                    witnessLen = compactSize(stream)
                    self.vin[i].scriptWitness.append(stream.read(witnessLen))

        if self.flags:
            raise Exception("error")

        self.nLockTime = uint4(stream)

    def readVin(self, stream):
        self.vinCount = compactSize(stream)
        self.vin = []
        for i in range(0, self.vinCount):
            isfirst = False
            if i == 0:
                isfirst = True
            self.vin.append(In(stream, isfirst))

    def readVout(self, stream, rskFlag):
        self.voutCount = compactSize(stream)
        self.vout = []

        if rskFlag:
            # coinbase 0 out
            self.vout.append(Out(stream, False))

            # coinbase 1 out
            self.vout.append(Out(stream, False))

            # btcpool 构建的区块是这样的!
            # coinbase 2 out -> RSKBLOCK:
            self.vout.append(Out(stream, True))
        else:
            for i in range(0, self.voutCount):
                self.vout.append(Out(stream, rskFlag))

    def isWitness(self):
        return self.witness

    def __str__(self):
        str = "nVersion: 0x{0:x}\n".format(self.nVersion)
        str = str + "vincount:{0}\n".format(len(self.vin))
        str = str + "voutcount: {0}\n".format(len(self.vout))
        str = str + "nLockTime: {0}\n".format(self.nLockTime)
        str = str + "--witness: {0}".format(self.isWitness())
        return str


class In:
    def __init__(self, stream, isfirst=False):
        self.prevouthash = hash32(stream)
        self.preoutn = uint4(stream)
        self.scriptSiglen = compactSize(stream)
        self.scriptSig = stream.read(self.scriptSiglen)
        self.nSequence = uint4(stream)
        self.scriptWitnessCount = 0
        self.scriptWitness = []

        self.isfirst = isfirst

    def __str__(self):
        str = "prevout 0x{0} {1}\n".format(hashStr(self.prevouthash), self.preoutn)
        str = str + "scriptSiglen: {0}\n".format(self.scriptSiglen)

        if self.isfirst:
            stream = io.BytesIO(self.scriptSig)
            heightLen = compactSize(stream)
            height = struct.unpack("<h", stream.read(heightLen))[0]

            blktimeLen = compactSize(stream)
            blktime = struct.unpack("<I", stream.read(blktimeLen))[0]

            remianLen = len(self.scriptSig) - heightLen - blktimeLen
            remain = stream.read(remianLen)
            str = str + "scriptSig: {} {} {}\n".format(height, blktime, remain)
        else:
            str = str + "scriptSig: {0}\n".format(scriptToAsmStr(self.scriptSig))
        str = str + "nSequence: 0x{0:x}\n".format(self.nSequence)
        str = str + "scriptWitnesslen: {0}".format(self.scriptWitnessCount)

        if self.scriptWitnessCount != 0:
            str += "\n"

        for i in range(0, self.scriptWitnessCount):
            str = str + "witness[{0}]: {1}".format(i, self.scriptWitness[i].hex())

            if i != self.scriptWitnessCount - 1:
                str = str + "\n"

        return str


class Out:
    def __init__(self, stream, rskFlag):
        self.nValue = uint8(stream)
        self.scriptPubkeylen = compactSize(stream)
        self.scriptPubkey = stream.read(self.scriptPubkeylen)

        self.rskFlag = rskFlag

    def valueFromAmount(self, amount):
        COIN = 100000000
        sign = amount < 0
        abs = 0 - amount if sign else amount
        quotient = int(abs / COIN)
        remainder = int(abs % COIN)
        return "{0:s}{1:d}.{2:d}".format("-" if sign else "", quotient, remainder)

    def __str__(self):
        str = "nValue {0}\n".format(self.valueFromAmount(self.nValue))
        str = str + "scriptPubkeylen: {0}\n".format(self.scriptPubkeylen)

        if self.rskFlag:
            rskBlock = self.scriptPubkey[:9]
            hashHex = self.scriptPubkey[9:]

            str = str + "scriptPubkey: {0} {1}".format(rskBlock.decode("utf-8"), hashHex.hex())
        else:
            str = str + "scriptPubkey: {0}".format(scriptToAsmStr(self.scriptPubkey))
        return str
