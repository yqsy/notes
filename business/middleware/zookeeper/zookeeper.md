
<!-- TOC -->

- [1. 说明](#1-说明)
- [2. 安装](#2-安装)
- [3. 使用](#3-使用)
- [4. 参考资料](#4-参考资料)

<!-- /TOC -->

<a id="markdown-1-说明" name="1-说明"></a>
# 1. 说明

```bash



```

<a id="markdown-2-安装" name="2-安装"></a>
# 2. 安装

```bash
mkdir -p ~/env

wget https://mirrors.tuna.tsinghua.edu.cn/apache/zookeeper/zookeeper-3.4.14/zookeeper-3.4.14.tar.gz -O /tmp/zookeeper-3.4.14.tar.gz
tar -xvzf /tmp/zookeeper-3.4.14.tar.gz -C ~/env/
cd ~/env
mv zookeeper-3.4.14 zookeeper

cat > ~/env/zookeeper/conf/zoo.cfg << EOF
tickTime=2000
dataDir=/var/lib/zookeeper
clientPort=2181
EOF

sudo mkdir -p /var/lib/zookeeper
sudo chown `whoami`:`id -g -n` /var/lib/zookeeper

# 开启
~/env/zookeeper/bin/zkServer.sh start-foreground

# 关闭
~/env/zookeeper/bin/zkServer.sh stop

# 删除持久数据
rm /var/lib/zookeeper && sudo mkdir -p /var/lib/zookeeper && sudo chown `whoami`:`id -g -n` /var/lib/zookeeper

```

<a id="markdown-3-使用" name="3-使用"></a>
# 3. 使用

telnet
```bash
telnet localhost 2181

# 查看信息
srvr

ls <path>
get <path>
set <path>
delete <path>
```

<a id="markdown-4-参考资料" name="4-参考资料"></a>
# 4. 参考资料

* https://www.apache.org/dyn/closer.cgi/zookeeper/ (下载连接)
