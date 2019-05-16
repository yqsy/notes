
<!-- TOC -->

- [1. 说明](#1-说明)
- [2. 安装](#2-安装)
- [3. 使用](#3-使用)
- [4. 参考资料](#4-参考资料)

<!-- /TOC -->

# 1. 说明

# 2. 安装

```bash
sudo ln -s /mnt/disk1/linux/env /

wget https://mirrors.tuna.tsinghua.edu.cn/apache/zookeeper/zookeeper-3.4.14/zookeeper-3.4.14.tar.gz -O /tmp/zookeeper-3.4.14.tar.gz
mkdir -p /env/zookeeper
tar -xvzf /tmp/zookeeper-3.4.14.tar.gz -C /env/zookeeper --strip 1

cat > /env/zookeeper/conf/zoo.cfg << EOF
tickTime=2000
dataDir=/var/lib/zookeeper
clientPort=2181
EOF

sudo mkdir -p /var/lib/zookeeper
sudo chown `whoami`:`id -g -n` /var/lib/zookeeper

# 开启
/env/zookeeper/bin/zkServer.sh start-foreground

# 关闭
/env/zookeeper/bin/zkServer.sh stop

# 删除持久数据
sudo rm -rf /var/lib/zookeeper && sudo mkdir -p /var/lib/zookeeper && sudo chown `whoami`:`id -g -n` /var/lib/zookeeper

```

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

# 4. 参考资料

* https://www.apache.org/dyn/closer.cgi/zookeeper/ (下载连接)
