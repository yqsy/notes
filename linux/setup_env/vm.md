

<!-- TOC -->

- [1. 指令](#1-指令)

<!-- /TOC -->

# 1. 指令


```bash
# 显示所有的磁盘
VBoxManage list hdds

# 修改大小
VBoxManage modifyhd /mnt/disk1/linux/vms/vm1/vm1.vdi --resize 307200

# 进虚拟机修改大小
sudo parted -l

# 删除分区,增加新分区
sudo fdisk /dev/sda

sudo resize2fs /dev/sda2
```
