---
title: Memcached
date: 2018-5-10 22:41:03
categories: [项目分析]
---

<!-- TOC -->

- [1. 资源](#1-资源)
- [2. 搭建](#2-搭建)
- [3. 搭建调试版本](#3-搭建调试版本)
- [4. 代码阅读整理](#4-代码阅读整理)
- [5. 接口/使用](#5-接口使用)
- [6. 数据结构选择](#6-数据结构选择)
    - [6.1. Naive key-value (天真的)](#61-naive-key-value-天真的)
    - [6.2. Minimalize critical section](#62-minimalize-critical-section)
    - [6.3. Condensed,save memory](#63-condensedsave-memory)
    - [6.4. Sharded, further reduce contention](#64-sharded-further-reduce-contention)
- [7. 实际数据结构](#7-实际数据结构)
- [8. 内存分配器选择](#8-内存分配器选择)
- [9. 单元测试](#9-单元测试)
- [10. 性能bench](#10-性能bench)

<!-- /TOC -->

<a id="markdown-1-资源" name="1-资源"></a>
# 1. 资源

* https://memcached.org/
* https://github.com/memcached/memcached
* https://hub.docker.com/_/memcached/ (docker)
* https://github.com/docker-library/memcached/blob/master/alpine/Dockerfile (docker file)
* https://www.tutorialspoint.com/memcached/memcached_set_data.htm (turtoial)
* https://github.com/memcached/memcached/blob/master/doc/protocol.txt (协议)
* https://github.com/memcached/memcached/wiki/Install (安装手册)
* https://www.zhihu.com/question/19719997/answer/81930332 (作为mysql缓存)
* https://www.zhihu.com/question/27738066/answer/45475986 (作为mysql缓存)

<a id="markdown-2-搭建" name="2-搭建"></a>
# 2. 搭建

```bash
docker run --name my-memcache -p 11211:11211 -d memcached
```

<a id="markdown-3-搭建调试版本" name="3-搭建调试版本"></a>
# 3. 搭建调试版本

```bash
cd /opt
git clone https://github.com/memcached/memcached.git
cd memcached
git checkout tags/1.5.4
```

```bash
tar -cvzf memcached.tgz  memcached
scp memcached.tgz root@vm1:/opt/
```

* https://stackoverflow.com/questions/9725278/cant-turn-off-gcc-optimizer-makefile-from-automake (automake编译关优化)

```bash
sudo su - root
yum install libevent-devel -y
yum install perl-CPAN -y
yum install perl-Test-Simple -y

cd /opt
tar -xvzf memcached.tgz
cd memcached
./autogen.sh
./configure  CFLAGS="-g -O0"
make && make test && sudo make install
gdbgui --host 0.0.0.0 --args "memcached -u root"
```


<a id="markdown-4-代码阅读整理" name="4-代码阅读整理"></a>
# 4. 代码阅读整理

```
 19827 total
  7757 ./memcached.c
  2029 ./testapp.c
  1812 ./items.c
  1268 ./slabs.c
   856 ./extstore.c
   822 ./logger.c
   808 ./thread.c
   692 ./crawler.c
   459 ./storage.c
   431 ./jenkins_hash.c
   375 ./stats.c
   343 ./crc32c.c
   307 ./assoc.c
   267 ./slab_automove_extstore.c
   196 ./util.c
   190 ./sasl_defs.c
   180 ./bipbuffer.c
   155 ./cache.c
   152 ./slab_automove.c
   149 ./itoa_ljust.c
   124 ./murmur3_hash.c
   113 ./linux_priv.c
   102 ./timedrun.c
    89 ./daemon.c
    44 ./solaris_priv.c
    32 ./sizes.c
    28 ./openbsd_priv.c
    26 ./globals.c
    21 ./hash.c
```

* daemon运行 fork -> 终结父进程 -> setsid创建新session使当前进程成为该session的头进程 -> 改变工作目录至/ ->重定向输入输出至/dev/null
* 使用的是libevent
* 多线程(pthread_create),多线程需要加参数编译(Round-robin 链接)
* 有锁生产者消费者队列 (pthread_mutex_lock)
* hash 算法: http://burtleburtle.net/bob/hash/doobs.html ?? 是这个吗
* hash 算法: MurmurHash3_x86_32 还有 jenkins_hash
* slab 内存处理机制,避免大量的初始化和清理操作 https://en.wikipedia.org/wiki/Slab_allocation
* LRU replacement algorithm

缺点:

* 无安全验证
* 没有持久化

```
日志线程:
main -> logger_init -> start_logger_thread -> pthread_create -> logger_thread (轮询 + sleep) -> logger_thread_read  (fwrite)

记录日志:
LOGGER_LOG -> logger_log -> bipbuf_push

工作线程池:
main->memcached_thread_init
创建线程池, 注册pipe读回调 thread_libevent_process -> conn_new-> 注册 clientfd event_handler -> drive_machine
线程池启动函数为 worker_libevent ,跑 event_base_loop 

主线程监听:
main->server_sockets- > server_socket -> conn_new (状态conn_listening) -> 注册listenfd event_handler -> drive_machine -> 
accept dispatch_conn_new (round robin指定线程处理 push到其线程的消息队列client fd,并通过pipe知会) 切换状态 conn_new_cmd

来事件时:
set tutorialspoint 0 900 9
memcached

conn_new_cmd -> conn_waiting -> conn_read 调用底层read -> case READ_DATA_RECEIVED -> 切换状态conn_parse_cmd -> 
process_command -> process_update_command (set) -> item_alloc -> 切换状态 conn_nread (这时候已经读完了第一句) -> complete_nread (读设置的值) ->
-> complete_nread_ascii -> store_item (关键哈希以及存储) -> out_string(c, "STORED"); -> 切换状态conn_write -> conn_mwrite (复用) -> transmit -> 
sendmsg

接收缓冲区:
以n^2不断递增缓冲区大小realloc  https://www.zhihu.com/question/45323220/answer/98683629

set锁力度:
只锁指针本身Minimalize critical section
static pthread_mutex_t *item_locks; 保护每个hash表
static item** primary_hashtable = 0; 全局的hash表

hash碰撞:
assoc_insert 开链法

对象最大可以存储为多大:
echo -e 'set tutorialspoint 0 900 1048576\r\n' > /tmp/111
dd if=/dev/zero bs=1M count=1 >> /tmp/111
cat /tmp/111 | nc localhost 11211
settings.item_size_max 最大为1024 * 1024 字节 (1M)

关键存储(48字节):
typedef struct _stritem {
    /* Protected by LRU locks */
    struct _stritem *next;
    struct _stritem *prev;
    /* Rest are protected by an item lock */
    struct _stritem *h_next;    /* hash chain next */
    rel_time_t      time;       /* least recent access */
    rel_time_t      exptime;    /* expire time */
    int             nbytes;     /* size of data */
    unsigned short  refcount;
    uint8_t         nsuffix;    /* length of flags-and-length string */
    uint8_t         it_flags;   /* ITEM_* above */
    uint8_t         slabs_clsid;/* which slab class we're in */
    uint8_t         nkey;       /* key length, w/terminating null and padding */
    /* this odd type prevents type-punning issues when we do
     * the little shuffle to save space when not using CAS. */
    union {
        uint64_t cas;
        char end;
    } data[];
    /* if it_flags & ITEM_CAS we have 8 bytes CAS */
    /* then null-terminated key */
    /* then " flags length\r\n" (no terminating null) */
    /* then data with terminating \r\n (no terminating null; it's binary!) */
} item;


setsockopt
* SO_SNDBUF 给发送缓冲区扩容 https://www.zhihu.com/question/67833119/answer/257061904 (没必要别设置)
* SO_REUSEADDR 
* SO_KEEPALIVE (缺省120分钟?) https://www.zhihu.com/search?type=content&q=SO_KEEPALIVE
* SO_LINGER (延迟关闭时间,应该不需要)
* TCP_NODELAY 
```


<a id="markdown-5-接口使用" name="5-接口使用"></a>
# 5. 接口/使用

存储
* set (强行设置)
* add (如果有key,则返回NOT_STORED)
* replace (替换value)
* append (字符串追加)
* prepend (前向追加)
* CAS (Check-And-Set)

检索数据
* get 
* gets
* incr 自增
* decr 自减

统计数据
* stats
* stats items
* stats slabs
* stats sizes
* flush_all


<a id="markdown-6-数据结构选择" name="6-数据结构选择"></a>
# 6. 数据结构选择

<a id="markdown-61-naive-key-value-天真的" name="61-naive-key-value-天真的"></a>
## 6.1. Naive key-value (天真的)
* hash_map<string, value*> (临界区保护整个读写过程)
* hash_map<string, unique_ptr<value>> (不需要删除)
* hash_map<string, value> // 右值


临界区内系统调用
```
hash_map<string,value*> theMap;

string key = xxx;
lock();
value* val = theMap.get(key);
send(val); # 这个系统调用会消耗大量的时间 (10ms)
unlock();
```

临界区内只是拷贝内存
```
string key = xxx;
value val;
lock();
val = *theMap.get(key); # 内存拷贝缩小了一个数量级,100us
unlock();
send(val);
```

<a id="markdown-62-minimalize-critical-section" name="62-minimalize-critical-section"></a>
## 6.2. Minimalize critical section
* hash_map<string, shared_ptr<value>>


临界区拷贝指针
set值时生成新的对象
```
typedef shared_ptr<const value> ValuePtr; # 注意是const的
hash_map<string,ValuePtr> theMap;
ValuePtr val;
lock();
val = theMap.get(key); # 指针拷贝时间更短,<1us
unlock();
send(*val);
```

<a id="markdown-63-condensedsave-memory" name="63-condensedsave-memory"></a>
## 6.3. Condensed,save memory
* hash_map<shared_ptr<item>> (key value放一起 节省空间) (自己实现比较函数)

```
unordered_set<shared_ptr<const Item>, Hash, Equal>
```

<a id="markdown-64-sharded-further-reduce-contention" name="64-sharded-further-reduce-contention"></a>
## 6.4. Sharded, further reduce contention
* 上千个hash_map,每个hash_map都有自己的锁,避免全局锁争用(多线程)

```
struct Shard 
{
    mutex mu_;
    hash_map<...> map_;
};


int x = key.hash() % 1024;
ValuePtr val;
shards[x].mu_.lock();
val = shards[x].map_.get(key);
shard[x].mu_.unlock();


Shard shards[1024];
```


属于半定制的,使用了标准库的hash map和shared ptr,而memcached是全定制的

基本开销是120N,memcached是48N

<a id="markdown-7-实际数据结构" name="7-实际数据结构"></a>
# 7. 实际数据结构

muduo-memcached
```
  int            keylen_;           // key 长度
  const uint32_t flags_;            
  const int      rel_exptime_;      
  const int      valuelen_;         // value长度
  int            receivedBytes_;    // 通过这个构造data_直至完整收到()
  uint64_t       cas_;
  size_t         hash_;             // key产生的hash值 最大值为18446744073709551615 or 0xffffffffffffffff
  char*          data_;             // 存放key + value
```

观察输入输出:
```
# 存
set x 0 20 10\r\n
helloworld\r\n
STORED\r\n

# 取
get x\r\n
VALUE x 0 10\r\n
helloworld\r\n
END\r\n
```


<a id="markdown-8-内存分配器选择" name="8-内存分配器选择"></a>
# 8. 内存分配器选择

* ptmalloc glibc
* tcmalloc

工具:
* perf record (性能热点 生成分析文件)
* perf report (查看时间分配报告)
* google-pprof (cpu profile 可以生成pdf, 新版本in go)
* gperftools (内存profile,旧版本)


<a id="markdown-9-单元测试" name="9-单元测试"></a>
# 9. 单元测试

```bash
prove t/getset.t
```

<a id="markdown-10-性能bench" name="10-性能bench"></a>
# 10. 性能bench

muduo bench.cc代码分析
```
可配参数:
* threads   Number of worker threads
* clients   Number of concurrent clients
* requests  Number of requests per clients
* keys      Number of keys per clients

每个thread都在跑event loop, 将clients以round-robin的方式负载均衡放至到各个event loop中
每个client非阻塞方式send recv达到requests数值

QPS计算:
全部client都连接上作为开始,全部client请求应答到requests数值并shutdown时作为结束. (使用的是CountDownLatch,条件变量包装)
1.0 * clients * requests / seconds
```

```bash
# 默认get,-s set
# 因为memcached默认是4线程,所以bench工具也开了4根线程(我机器8核心)

# (原生)只有13w
./memcached_bench -p 11211 -i 127.0.0.1 -t 4 -c 10 -r 10000

# (原生)有40w
./memcached_bench -p 11211 -i 127.0.0.1 -t 4 -c 100 -r 100000

# (with muduo)有43w
./memcached_bench -p 11211 -i 127.0.0.1 -t 4 -c 100 -r 100000
```
