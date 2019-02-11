
<!-- TOC -->

- [1. 说明](#1-说明)

<!-- /TOC -->


<a id="markdown-1-说明" name="1-说明"></a>
# 1. 说明

* 将/rskj/rskj-core/src/main/resources/config/main.conf中的`bootstrap`信息清空
* 启动前重置测试信息. `~/.rsk` 
* 启动前重置日志信息. `/mnt/disk1/linux/reference/refer/rskj/logs`

```bash
# 重置语句
rm -rf ~/.rsk
rm -rf /mnt/disk1/linux/reference/refer/rskj/logs

# 查看日志
more /mnt/disk1/linux/reference/refer/rskj/logs/rsk.log
```
