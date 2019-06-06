

<!-- TOC -->

- [1. 说明](#1-说明)
- [2. proxmox](#2-proxmox)
- [3. ubuntu static ip](#3-ubuntu-static-ip)

<!-- /TOC -->

# 1. 说明

* https://www.zhihu.com/question/266743901/answer/422497253 (韦易笑)
* https://github.com/retspen/webvirtmgr/wiki/Setup-Host-Server (libvirt和kvm)
* https://websiteforstudents.com/setup-linux-kvm-kernel-virtualization-module-on-ubuntu-18-04-lts-server/(kvm)
* https://github.com/retspen/webvirtmgr (web前端)
---
* https://www.hiroom2.com/2018/05/08/ubuntu-1804-bridge-en/ (网卡设置参考)
* https://www.jb51.net/article/142818.htm (网卡设置参考)
* https://www.cnblogs.com/kevingrace/p/5739009.html (web设置参考)

---

* KVM: 内核级别的虚拟化功能
* QEMU: 用户操作界面, VNC/SPICE远程终端
* Libvirtd: 虚拟化服务,运行在Hypervisor上提供TCP接口用于操作虚拟机的创建和起停


```bash
# 网卡

INTERFACE=enp3s0
cat << EOF | sudo tee /etc/network/interfaces
auto lo
iface lo inet loopback
auto br0
iface br0 inet dhcp
      bridge_ports ${INTERFACE}
      bridge_stp off
      bridge_maxwait 0
EOF

sudo systemctl restart networking.service

# 修改
/etc/default/ufw

DEFAULT_FORWARD_POLICY="ACCEPT"

sudo systemctl restart ufw.service
```

```bash
# libvirt and kvm

# cd  /etc/apt/sources.list.d
# sudo mv google-chrome.list google-chrome.list.bak

# wget -O - http://retspen.github.io/libvirt-bootstrap.sh | sudo sh

sudo apt-get install qemu qemu-kvm libvirt-bin  bridge-utils  virt-manager

sudo systemctl start libvirtd
sudo systemctl enable libvirtd

```

```bash
# webvirtmgr
sudo apt-get install git python-pip python-libvirt python-libxml2 novnc supervisor nginx 

cd /mnt/disk1/linux/installpack/kvm
git clone git://github.com/retspen/webvirtmgr.git
cd webvirtmgr
sudo pip install -r requirements.txt
./manage.py syncdb
./manage.py collectstatic

cd ..
sudo mv webvirtmgr /var/www/

sudo wget https://gist.githubusercontent.com/yqsy/8dc4504436d38c1f9de7475ec2b1ebb9/raw/432a0e8140fb700c87bb4ecfea55e60edfe8fcb2/gistfile1.txt -O /etc/nginx/conf.d/webvirtmgr.conf

# 添加注释
sudo vim /etc/nginx/sites-enabled/default

sudo service nginx restart

```

```bash
# 这列没法做

sudo service novnc stop
sudo insserv -r novnc
sudo vi /etc/insserv/overrides/novnc

### BEGIN INIT INFO
# Provides:          nova-novncproxy
# Required-Start:    $network $local_fs $remote_fs $syslog
# Required-Stop:     $remote_fs
# Default-Start:     
# Default-Stop:      
# Short-Description: Nova NoVNC proxy
# Description:       Nova NoVNC proxy
### END INIT INFO


```

```bash
#sudo chown -R www-data:www-data /var/www/webvirtmgr

#sudo wget https://gist.githubusercontent.com/yqsy/668fd084079939bd7e8fde4eb7cba96d/raw/2afadb2f109acb65308d0d2b74e533fab242b6c5/gistfile1.txt -O /etc/supervisor/conf.d/webvirtmgr.conf

#sudo service supervisor stop
#sudo service supervisor start

# 升级
cd /var/www/webvirtmgr
sudo git pull
sudo ./manage.py collectstatic
sudo service supervisor restart

# 启动
cd /var/www/webvirtmgr
./manage.py runserver 0:8000

```

```bash
# 监听问题,变更配置

/etc/libvirt/libvirtd.conf

/etc/default/libvirtd

sudo ufw allow 16509

```

```bash
# ui 

virt-manager
```


# 2. proxmox


网络配置

```bash

# /etc/network/interfaces
auto lo
iface lo inet loopback

iface eno1 inet manual

iface eno2 inet manual

auto vmbr0
iface vmbr0 inet static
	address 192.168.0.221
	netmask 255.255.255.0
	gateway 192.168.0.1
	bridge_ports eno1
	bridge_stp off
	bridge_fd 0

# /etc/resolv.conf
search com
nameserver 223.5.5.5
```

指令:
```bash
# 查看各个网卡的ip
ip a

#　开关网卡
ifup 
ifdown

# 下载镜像
cd /var/lib/vz/template/iso

# http://mirrors.aliyun.com/ubuntu-releases/
wget http://mirrors.aliyun.com/ubuntu-releases/18.04.2/ubuntu-18.04.2-live-server-amd64.iso

wget http://mirrors.aliyun.com/ubuntu-releases/18.04.2/ubuntu-18.04.2-desktop-amd64.iso
```

# 3. ubuntu static ip


```bash
# /etc/netplan/50-cloud-init.yaml
network:
	ethernets:
		ens18:
			dhcp4: false
			addresses: [192.168.0.213/24]
			gateway4: 192.168.0.1
			nameservers:
				addresses: [223.5.5.5]
	version: 2


sudo netplan apply
```

