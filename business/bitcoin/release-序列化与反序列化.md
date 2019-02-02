---
title: 序列化与反序列化
date: 2018-02-01 13:29:12
categories: [business, bitcoin]
---

<!-- TOC -->

- [1. 说明](#1-说明)

<!-- /TOC -->

<a id="markdown-1-说明" name="1-说明"></a>
# 1. 说明

在编程语言中,想让struct与磁盘/网络打交道时,必须使用序列化(serialize)以及反序列化(deserialize)的技术,这是因为字节序有不同的标准(例如网络字节序为大端法,芯片有大端法与小端法),直接把程序内存中的struct提取字节copy到磁盘/网络时,不同的设备/标准读取时会发生错乱的问题.

而在c++语言中,往往需要用户自己量身定制一套规则来实现这个逻辑,在比特币中是这样实现的:

sturct 中 包含宏: `ADD_SERIALIZE_METHODS`, 其作为一个`方便便捷的手段`实现了类的序列化函数:

```c++
template<typename Stream>
void Serialize(Stream& s) const {
    NCONST_PTR(this)->SerializationOp(s, CSerActionSerialize());    
}
```

```c++
template<typename Stream>
void Unserialize(Stream& s) { 
    SerializationOp(s, CSerActionUnserialize());
}
```

而其中的`SerializationOp`则是`元数据`(产生数据的数据),定义了序列化/反序列化时该处理的字段,`Operation ser_action`为行为模版(在编译期决定了READWRITE宏内函数调用的是序列化/反序列化):

```c++
// 举一个例子: CBlockHeader
template <typename Stream, typename Operation>
inline void SerializationOp(Stream& s, Operation ser_action) {
    READWRITE(this->nVersion);
    READWRITE(hashPrevBlock);
    READWRITE(hashMerkleRoot);
    READWRITE(nTime);
    READWRITE(nBits);
    READWRITE(nNonce);
}
```

`READWRITE`为序列化/反序列化两种行为的包装,其在最后调用的是`Serialize`/`Unserialize`,定义了序列化/反序列化的最终行为.

```c++
// 举一个例子: uint8_t  (serialize)
template<typename Stream> inline void Serialize(Stream& s, uint8_t a ) { ser_writedata8(s, a); }

template<typename Stream> inline void ser_writedata8(Stream &s, uint8_t obj)
{
    s.write((char*)&obj, 1);
}

// 举一个例子: uint8_t  (Unserialize)
template<typename Stream> inline void Unserialize(Stream& s, uint8_t& a ) { a = ser_readdata8(s); }

template<typename Stream> inline uint8_t ser_readdata8(Stream &s)
{
    uint8_t obj;
    s.read((char*)&obj, 1);
    return obj;
}
```

不止如上面举例的uint8_t,其他基础类型如下:


* char
* bool
* int8_t / uint8_t
* int16_t / uint16_t
* int32_t / uint32_t
* int64_t / uint64_t
* float / double
* char (&a)[N] / unsigned char (&a)[N]
* ```Span<unsigned char>&```
* ```std::basic_string<C>&```
* ```prevector<N, T>&```
* ```std::vector<T, A>&```
* ```std::pair<K, T>&```
* ```std::map<K, T, Pred, A>&```
* ```std::set<K, Pred, A>&```
* ```std::shared_ptr<const T>&```
* ```std::unique_ptr<const T>&```

以及为每一个类型都提供了模板方法:
```c++
template<typename Stream, typename T>
inline void Serialize(Stream& os, const T& a)
{
    a.Serialize(os);
}

template<typename Stream, typename T>
inline void Unserialize(Stream& is, T&& a)
{
    a.Unserialize(is);
}
```

和文件打交道的例子: 当发生CAutoFile << CBlock时, 将自身CAutoFile作为Stream(接口:read,write)通过全局的
Serialize/Unserialize模板函数定位到类, 再调用类的Serialize/Unserialize函数,并将stream作为参数传入其中:

```c++
// 举一个例子: CAutoFile

class CAutoFile
{
    void read(char* pch, size_t nSize)
    {
        // ... 省略
        if (fread(pch, 1, nSize, file) != nSize)
        // ... 省略
    }

    void write(const char* pch, size_t nSize)
    {
        // ... 省略
        if (fwrite(pch, 1, nSize, file) != nSize)
        // ... 省略
    }

    template<typename T>
    CAutoFile& operator<<(const T& obj)
    {
        // ... 省略
        ::Serialize(*this, obj);
        return (*this);
    }

    template<typename T>
    CAutoFile& operator>>(T&& obj)
    {
        // ... 省略
        ::Unserialize(*this, obj);
        return (*this);
    }
}
```


综上,我们可以总结一个比特币(或c++)序列化/反序列化技术的一个抽象: 

* Stream抽象类提供read,write行为的抽象,与磁盘/网络打交道. 
* 以及 输入(<<) 输出(>>)函数与类型打交道. 

当使用<<或>>与类型打交道时,通过模板类型匹配,在编译期寻找到`类的Serialize/Unserialize`函数,将抽象行为类`(Stream:read/write)的具体实现`作为参数传递进去. 而`类的Serialize/Unserialize`将一个又一个基础类型通过`(Stream:read/write)的具体实现`输入输出到磁盘/网络中.