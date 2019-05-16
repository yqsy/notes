<!-- TOC -->

- [1. 说明](#1-说明)
- [2. 日志库](#2-日志库)
- [3. 内存16进制打印](#3-内存16进制打印)

<!-- /TOC -->


# 1. 说明

很多时候接手别人的c/c++项目,从代码层面根本看不懂逻辑,因为作者对抽象层次不理解,不知道序列化,反序列化,大小端,而是把结构体放在内存中一锅粥乱炖,作者只管自己达到了自己的目的,而不管这样写别人是否能够看懂,假以时日他自己也看不懂.

这个markdown主要是看不懂代码的时候写一些helper代码,帮助能够理解这个傻逼作者到底写了些什么


# 2. 日志库

```bash
curl https://raw.githubusercontent.com/rxi/log.c/master/src/log.c -o log.c
curl https://raw.githubusercontent.com/rxi/log.c/master/src/log.h -o log.h
```

# 3. 内存16进制打印

```c++
#include <stdint.h>
#include <stdio.h>
#include <string.h>

#include "log.h"

void BytesToStr(const uint8_t* bytes, int bytesLen, char* buffer, int bufferLen) {
    for(int i = 0; i < bytesLen; ++i) {
        uint32_t onebyte = (uint32_t)bytes[i];
        char onebyteStr[10] = {};
        snprintf(onebyteStr, sizeof(onebyteStr), "%02X", onebyte);
        strncat(buffer, onebyteStr, bufferLen - 1);
    }
}

struct Helper
{
    int32_t a;
    int32_t b;
    int32_t c;
    int32_t d;
};

char* GetHelperString(const Helper* helper, char* buffer, int bufferLen) {
    snprintf(buffer, bufferLen, "a:%08X, b:%08X, c:%08X, d:%08X", helper->a, helper->b, helper->c, helper->d);
    return buffer;
}

int main() {
    FILE* fp = fopen("/tmp/helper1", "a+");
    log_set_fp(fp);
    uint8_t bytes[] {0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0A, 0xB, 0xC, 0xD, 0xE, 0xF, 0x10};
    char buffer[1024] = {};
    BytesToStr(bytes, sizeof(bytes), buffer, sizeof(buffer));
    log_info("%s", buffer);

    Helper* helper = (Helper*)bytes;
    char buffer2[49] = {};
    GetHelperString(helper, buffer2, sizeof(buffer2));
    log_info("%s", buffer2);
    fclose(fp);
    return 0;
}

```

