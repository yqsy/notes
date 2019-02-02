from datetime import datetime
from impl.script import *

class BlockHeader:
    def __init__(self, stream):
        self.nVersion = uint4(stream)
        self.hashPrevBlock = hash32(stream)
        self.hashMerkleRoot = hash32(stream)
        self.nTime = uint4(stream)
        self.nBits = uint4(stream)
        self.nNonce = uint4(stream)

    def __str__(self):
        str = "nVersion: 0x{0:x}\n".format(self.nVersion)
        str = str + "hashPrevBlock: 0x{0}\n".format(hashStr(self.hashPrevBlock))
        str = str + "hashMerkleRoot: 0x{0}\n".format(hashStr(self.hashMerkleRoot))
        str = str + "nTime: {0}\n".format(self.decodeTime(self.nTime))
        str = str + "nBits: 0x{0:x}\n".format(self.nBits)
        str = str + "nNonce: {0}".format(self.nNonce)
        return str

    def decodeTime(self, time):
        utcTime = datetime.utcfromtimestamp(time)
        return utcTime.strftime("%Y-%m-%d %H:%M:%S.%f+00:00 (UTC)")


class Block:
    def __init__(self, stream):
        self.magicno = uint4(stream)
        self.blockSize = uint4(stream)
        self.blockHeader = BlockHeader(stream)

        self.txcount = compactSize(stream)
        self.vtx = []

        for i in range(0, self.txcount):
            self.vtx.append(Tx(stream))

    def isMagicNoValid(self):
        return self.magicno == 0xD9B4BEF9

    def isMagicZero(self):
        return self.magicno == 0x0

    def __str__(self):
        str = "blocksize: {0}\n".format(self.blockSize)
        str = str + "txcount: {0}".format(self.txcount)
        return str


class Tx:
    def __init__(self, stream):
        self.witness = False

        self.nVersion = uint4(stream)
        self.flags = 0
        self.readVin(stream)

        if len(self.vin) == 0:
            self.flags = uint1(stream)

            if self.flags != 0:
                self.readVin(stream)
                self.readVout(stream)
        else:
            self.readVout(stream)

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
            self.vin.append(In(stream))

    def readVout(self, stream):
        self.voutCount = compactSize(stream)
        self.vout = []
        for i in range(0, self.voutCount):
            self.vout.append(Out(stream))

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
    def __init__(self, stream):
        self.prevouthash = hash32(stream)
        self.preoutn = uint4(stream)
        self.scriptSiglen = compactSize(stream)
        self.scriptSig = stream.read(self.scriptSiglen)
        self.nSequence = uint4(stream)
        self.scriptWitnessCount = 0
        self.scriptWitness = []

    def __str__(self):
        str = "prevout 0x{0} {1}\n".format(hashStr(self.prevouthash), self.preoutn)
        str = str + "scriptSiglen: {0}\n".format(self.scriptSiglen)
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
    def __init__(self, stream):
        self.nValue = uint8(stream)
        self.scriptPubkeylen = compactSize(stream)
        self.scriptPubkey = stream.read(self.scriptPubkeylen)

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
        str = str + "scriptPubkey: {0}".format(scriptToAsmStr(self.scriptPubkey))
        return str
