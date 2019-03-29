<!-- TOC -->

- [1. 说明](#1-说明)
- [2. 安装](#2-安装)

<!-- /TOC -->


<a id="markdown-1-说明" name="1-说明"></a>
# 1. 说明

```bash
cd /mnt/disk1/linux/reference/refer/db
git clone https://github.com/mongodb/mongo
git checkout tags/r4.1.9
git branch -d master
git checkout -b master

```


<a id="markdown-2-安装" name="2-安装"></a>
# 2. 安装

```bash
yaourt -S --noconfirm mongodb-bin

mkdir -p /data/db

sudo mongod
```
