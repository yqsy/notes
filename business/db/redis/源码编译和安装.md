<!-- TOC -->

- [1. 说明](#1-说明)
- [参考资料](#参考资料)

<!-- /TOC -->

<a id="markdown-1-说明" name="1-说明"></a>
# 1. 说明

```bash
cd /mnt/disk1/linux/reference/refer/db
git clone https://github.com/antirez/redis.git
git checkout tags/5.0.3
git branch -d master
git checkout -b master

make -j 12 MALLOC=libc
sudo make install
```

<a id="markdown-参考资料" name="参考资料"></a>
# 参考资料

* https://gist.github.com/LeCoupa/1596b8f359ad8812c7271b5322c30946 (cheat sheet)