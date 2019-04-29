<!-- TOC -->

- [1. 说明](#1-说明)
- [参考资料](#参考资料)

<!-- /TOC -->

# 1. 说明

阅读:
```bash
cd /mnt/disk1/linux/reference/refer/db
git clone https://github.com/antirez/redis.git
git checkout tags/5.0.3
git branch -d master
git checkout -b master

make -j 12 MALLOC=libc
sudo make install
```

安装:
```bash
sudo ln -s /mnt/disk1/linux/env /

cd /env
wget http://download.redis.io/releases/redis-5.0.4.tar.gz -O /tmp/redis-5.0.4.tar.gz
tar -xvzf /tmp/redis-5.0.4.tar.gz -C /env/
cd redis-5.0.4
make -j 12
sudo make install

```

# 参考资料

* https://gist.github.com/LeCoupa/1596b8f359ad8812c7271b5322c30946 (cheat sheet)