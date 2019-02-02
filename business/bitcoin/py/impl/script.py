from impl.serialize import *

# push value
OP_0 = 0x00
OP_FALSE = OP_0
OP_PUSHDATA1 = 0x4c
OP_PUSHDATA2 = 0x4d
OP_PUSHDATA4 = 0x4e
OP_1NEGATE = 0x4f
OP_RESERVED = 0x50
OP_1 = 0x51
OP_TRUE = OP_1
OP_2 = 0x52
OP_3 = 0x53
OP_4 = 0x54
OP_5 = 0x55
OP_6 = 0x56
OP_7 = 0x57
OP_8 = 0x58
OP_9 = 0x59
OP_10 = 0x5a
OP_11 = 0x5b
OP_12 = 0x5c
OP_13 = 0x5d
OP_14 = 0x5e
OP_15 = 0x5f
OP_16 = 0x60

# control
OP_NOP = 0x61
OP_VER = 0x62
OP_IF = 0x63
OP_NOTIF = 0x64
OP_VERIF = 0x65
OP_VERNOTIF = 0x66
OP_ELSE = 0x67
OP_ENDIF = 0x68
OP_VERIFY = 0x69
OP_RETURN = 0x6a

# stack ops
OP_TOALTSTACK = 0x6b
OP_FROMALTSTACK = 0x6c
OP_2DROP = 0x6d
OP_2DUP = 0x6e
OP_3DUP = 0x6f
OP_2OVER = 0x70
OP_2ROT = 0x71
OP_2SWAP = 0x72
OP_IFDUP = 0x73
OP_DEPTH = 0x74
OP_DROP = 0x75
OP_DUP = 0x76
OP_NIP = 0x77
OP_OVER = 0x78
OP_PICK = 0x79
OP_ROLL = 0x7a
OP_ROT = 0x7b
OP_SWAP = 0x7c
OP_TUCK = 0x7d

# splice ops
OP_CAT = 0x7e
OP_SUBSTR = 0x7f
OP_LEFT = 0x80
OP_RIGHT = 0x81
OP_SIZE = 0x82

# bit logic
OP_INVERT = 0x83
OP_AND = 0x84
OP_OR = 0x85
OP_XOR = 0x86
OP_EQUAL = 0x87
OP_EQUALVERIFY = 0x88
OP_RESERVED1 = 0x89
OP_RESERVED2 = 0x8a

# numeric
OP_1ADD = 0x8b
OP_1SUB = 0x8c
OP_2MUL = 0x8d
OP_2DIV = 0x8e
OP_NEGATE = 0x8f
OP_ABS = 0x90
OP_NOT = 0x91
OP_0NOTEQUAL = 0x92

OP_ADD = 0x93
OP_SUB = 0x94
OP_MUL = 0x95
OP_DIV = 0x96
OP_MOD = 0x97
OP_LSHIFT = 0x98
OP_RSHIFT = 0x99

OP_BOOLAND = 0x9a
OP_BOOLOR = 0x9b
OP_NUMEQUAL = 0x9c
OP_NUMEQUALVERIFY = 0x9d
OP_NUMNOTEQUAL = 0x9e
OP_LESSTHAN = 0x9f
OP_GREATERTHAN = 0xa0
OP_LESSTHANOREQUAL = 0xa1
OP_GREATERTHANOREQUAL = 0xa2
OP_MIN = 0xa3
OP_MAX = 0xa4

OP_WITHIN = 0xa5

# crypto
OP_RIPEMD160 = 0xa6
OP_SHA1 = 0xa7
OP_SHA256 = 0xa8
OP_HASH160 = 0xa9
OP_HASH256 = 0xaa
OP_CODESEPARATOR = 0xab
OP_CHECKSIG = 0xac
OP_CHECKSIGVERIFY = 0xad
OP_CHECKMULTISIG = 0xae
OP_CHECKMULTISIGVERIFY = 0xaf

# expansion
OP_NOP1 = 0xb0
OP_CHECKLOCKTIMEVERIFY = 0xb1
OP_NOP2 = OP_CHECKLOCKTIMEVERIFY
OP_CHECKSEQUENCEVERIFY = 0xb2
OP_NOP3 = OP_CHECKSEQUENCEVERIFY
OP_NOP4 = 0xb3
OP_NOP5 = 0xb4
OP_NOP6 = 0xb5
OP_NOP7 = 0xb6
OP_NOP8 = 0xb7
OP_NOP9 = 0xb8
OP_NOP10 = 0xb9

OP_INVALIDOPCODE = 0xff

OPCODE_NAMES = {
    # push value
    OP_0: "0",
    OP_PUSHDATA1: "OP_PUSHDATA1",
    OP_PUSHDATA2: "OP_PUSHDATA2",
    OP_PUSHDATA4: "OP_PUSHDATA4",
    OP_1NEGATE: "-1",
    OP_RESERVED: "OP_RESERVED",
    OP_1: "1",
    OP_2: "2",
    OP_3: "3",
    OP_4: "4",
    OP_5: "5",
    OP_6: "6",
    OP_7: "7",
    OP_8: "8",
    OP_9: "9",
    OP_10: "10",
    OP_11: "11",
    OP_12: "12",
    OP_13: "13",
    OP_14: "14",
    OP_15: "15",
    OP_16: "16",

    # control
    OP_NOP: "OP_NOP",
    OP_VER: "OP_VER",
    OP_IF: "OP_IF",
    OP_NOTIF: "OP_NOTIF",
    OP_VERIF: "OP_VERIF",
    OP_VERNOTIF: "OP_VERNOTIF",
    OP_ELSE: "OP_ELSE",
    OP_ENDIF: "OP_ENDIF",
    OP_VERIFY: "OP_VERIFY",
    OP_RETURN: "OP_RETURN",

    # stack ops
    OP_TOALTSTACK: "OP_TOALTSTACK",
    OP_FROMALTSTACK: "OP_FROMALTSTACK",
    OP_2DROP: "OP_2DROP",
    OP_2DUP: "OP_2DUP",
    OP_3DUP: "OP_3DUP",
    OP_2OVER: "OP_2OVER",
    OP_2ROT: "OP_2ROT",
    OP_2SWAP: "OP_2SWAP",
    OP_IFDUP: "OP_IFDUP",
    OP_DEPTH: "OP_DEPTH",
    OP_DROP: "OP_DROP",
    OP_DUP: "OP_DUP",
    OP_NIP: "OP_NIP",
    OP_OVER: "OP_OVER",
    OP_PICK: "OP_PICK",
    OP_ROLL: "OP_ROLL",
    OP_ROT: "OP_ROT",
    OP_SWAP: "OP_SWAP",
    OP_TUCK: "OP_TUCK",

    # splice ops
    OP_CAT: "OP_CAT",
    OP_SUBSTR: "OP_SUBSTR",
    OP_LEFT: "OP_LEFT",
    OP_RIGHT: "OP_RIGHT",
    OP_SIZE: "OP_SIZE",

    # bit logic
    OP_INVERT: "OP_INVERT",
    OP_AND: "OP_AND",
    OP_OR: "OP_OR",
    OP_XOR: "OP_XOR",
    OP_EQUAL: "OP_EQUAL",
    OP_EQUALVERIFY: "OP_EQUALVERIFY",
    OP_RESERVED1: "OP_RESERVED1",
    OP_RESERVED2: "OP_RESERVED2",

    # numeric
    OP_1ADD: "OP_1ADD",
    OP_1SUB: "OP_1SUB",
    OP_2MUL: "OP_2MUL",
    OP_2DIV: "OP_2DIV",
    OP_NEGATE: "OP_NEGATE",
    OP_ABS: "OP_ABS",
    OP_NOT: "OP_NOT",
    OP_0NOTEQUAL: "OP_0NOTEQUAL",
    OP_ADD: "OP_ADD",
    OP_SUB: "OP_SUB",
    OP_MUL: "OP_MUL",
    OP_DIV: "OP_DIV",
    OP_MOD: "OP_MOD",
    OP_LSHIFT: "OP_LSHIFT",
    OP_RSHIFT: "OP_RSHIFT",
    OP_BOOLAND: "OP_BOOLAND",
    OP_BOOLOR: "OP_BOOLOR",
    OP_NUMEQUAL: "OP_NUMEQUAL",
    OP_NUMEQUALVERIFY: "OP_NUMEQUALVERIFY",
    OP_NUMNOTEQUAL: "OP_NUMNOTEQUAL",
    OP_LESSTHAN: "OP_LESSTHAN",
    OP_GREATERTHAN: "OP_GREATERTHAN",
    OP_LESSTHANOREQUAL: "OP_LESSTHANOREQUAL",
    OP_GREATERTHANOREQUAL: "OP_GREATERTHANOREQUAL",
    OP_MIN: "OP_MIN",
    OP_MAX: "OP_MAX",
    OP_WITHIN: "OP_WITHIN",

    # crypto
    OP_RIPEMD160: "OP_RIPEMD160",
    OP_SHA1: "OP_SHA1",
    OP_SHA256: "OP_SHA256",
    OP_HASH160: "OP_HASH160",
    OP_HASH256: "OP_HASH256",
    OP_CODESEPARATOR: "OP_CODESEPARATOR",
    OP_CHECKSIG: "OP_CHECKSIG",
    OP_CHECKSIGVERIFY: "OP_CHECKSIGVERIFY",
    OP_CHECKMULTISIG: "OP_CHECKMULTISIG",
    OP_CHECKMULTISIGVERIFY: "OP_CHECKMULTISIGVERIFY",

    # expansion
    OP_NOP1: "OP_NOP1",
    OP_CHECKLOCKTIMEVERIFY: "OP_CHECKLOCKTIMEVERIFY",
    OP_CHECKSEQUENCEVERIFY: "OP_CHECKSEQUENCEVERIFY",
    OP_NOP4: "OP_NOP4",
    OP_NOP5: "OP_NOP5",
    OP_NOP6: "OP_NOP6",
    OP_NOP7: "OP_NOP7",
    OP_NOP8: "OP_NOP8",
    OP_NOP9: "OP_NOP9",
    OP_NOP10: "OP_NOP10",

    OP_INVALIDOPCODE: "OP_INVALIDOPCODE",
}


# 传出1.pc 迭代指针 2. opcodeRet 操作符号 3. pvchRet (如果是数据流,则返回相应数据) 4. True,False
def getScriptOp(pc, script):
    opcodeRet = OP_INVALIDOPCODE
    pvchRet = b''

    end = len(script)

    if pc >= end:
        return pc, opcodeRet, pvchRet, False

    opcode = script[pc]
    pc += 1

    if opcode <= OP_PUSHDATA4:
        nSize = 0
        if opcode < OP_PUSHDATA1:
            nSize = opcode
        elif opcode == OP_PUSHDATA1:
            # 1byte
            if end - pc < 1:
                return pc, opcodeRet, pvchRet, False
            nSize = script[pc]
            pc += 1
        elif opcode == OP_PUSHDATA2:
            # 2byte
            if end - pc < 2:
                return pc, opcodeRet, pvchRet, False
            nSize = struct.unpack('H', script[pc: pc + 2])[0]
            pc += 2

        elif opcode == OP_PUSHDATA4:
            # 4byte
            if end - pc < 4:
                return pc, opcodeRet, pvchRet, False
            nSize = struct.unpack('I', script[pc:pc + 4])[0]
            pc += 4

        if end - pc < 0 or (end - pc) < nSize:
            return pc, opcodeRet, pvchRet, False

        pvchRet = script[pc:pc + nSize]
        pc += nSize

    opcodeRet = opcode
    return pc, opcodeRet, pvchRet, True


def scriptToAsmStr(script):
    str = ""

    pc = 0

    while pc < len(script):
        if len(str) != 0:
            str += " "

        pc, opcode, pvch, ok = getScriptOp(pc, script)

        if not ok:
            str += "[error]"
            return str

        if 0 <= opcode and opcode <= OP_PUSHDATA4:
            if len(pvch) <= 4:
                d = 0
                if len(pvch) == 1:
                    d = ord(pvch)
                elif len(pvch) == 2:
                    d = struct.unpack('H', pvch)[0]
                elif len(pvch) == 4:
                    d = struct.unpack('I', pvch)[0]
                str += "{0}".format(d)
            else:
                str += pvch.hex()
        else:
            try:
                str += OPCODE_NAMES[opcode]
            except KeyError:
                str += "OP_UNKNOWN"
    return str
