

<!-- TOC -->

- [1. 资料](#1-资料)
- [2. 安装](#2-安装)
- [3. 缩小体积](#3-缩小体积)
- [4. 网络](#4-网络)
- [5. 开发心得](#5-开发心得)

<!-- /TOC -->


# 1. 资料

* https://hujb2000.gitbooks.io/docker-flow-evolution/content/cn/index.html (Docker入门与实战)
* https://docs.docker.com/engine/getstarted/ (官方文档)
* http://www.docker.org.cn/book/docker/what-is-docker-16.html (docker中文社区)
* https://stackoverflow.com/questions/30494050/how-do-i-pass-environment-variables-to-docker-containers (传递环境变量给docker)
* https://docs.docker.com/engine/admin/volumes/volumes/ (manager data in docker)
* https://nickjanetakis.com/blog/the-3-biggest-wins-when-using-alpine-as-a-base-docker-image (各大base镜像大小)
* https://www.infoq.cn/article/3-simple-tricks-for-smaller-docker-images (缩小镜像)
* https://docs.docker.com/get-started/part2/ (很好的文章)

# 2. 安装

* https://mirrors.tuna.tsinghua.edu.cn/help/docker-ce/ (到这里安装?清华源?不对)
* https://www.docker-cn.com/registry-mirror (中国官方的源)


```bash
https://docs.docker.com/install/linux/docker-ce/ubuntu/

# ubuntu
sudo apt-get remove docker docker-engine docker.io containerd runc

# https://download.docker.com/linux/ubuntu/gpg
# https://download.docker.com/linux/ubuntu
sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common -y; \
curl -fsSL https://mirrors.aliyun.com/docker-ce/linux/ubuntu/gpg | sudo apt-key add -; \
sudo apt-key fingerprint 0EBFCD88; \
sudo add-apt-repository \
   "deb [arch=amd64] https://mirrors.aliyun.com/docker-ce/linux/ubuntu/ \
   $(lsb_release -cs) \
   stable"; \
sudo apt-get update; \
sudo apt-get install docker-ce docker-ce-cli containerd.io -y;
#sudo docker run hello-world;

sudo groupadd docker; \
sudo gpasswd -a $USER docker; \
newgrp docker 


# docker compose
sudo curl -L https://github.com/docker/compose/releases/download/1.24.0/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

# 改变源
mkdir -p /etc/docker
echo \
"{
  \"registry-mirrors\": [\"https://registry.docker-cn.com\"]
}" | sudo tee /etc/docker/daemon.json

# 改变存储的地点 (不能用ntfs!!!)
# 修改 /etc/docker/daemon.json
"graph": "/mnt/disk1/linux/docker",
"storage-driver": "devicemapper",
"experimental":true
```

# 3. 缩小体积

* 多层压缩
* 编译层 和 运行层
* Alpine

# 4. 网络

* host模式, --net=host, 使用宿主机的IP和端口
* container模式, --net=container:NAMEorID, 和一个指定的容器共享IP,端口范围
* none模式, --net=none , 不为容器添加任何网络配置
* bridge模式, --net=bridge , 创建一个docker0的虚拟网卡

```bash
defaultip=$(route | awk '/default/ {print $2}')
echo $defaultip
```

systemd-resolv 
```bash
# (我们不要使用这个)
# ubuntu默认的监听127.0.0.53:53的systemd-resolv服务的配置
/etc/systemd/resolved.conf

# 本地使用的dns服务器的配置 (右边才是真正的运行时dns服务器)
/etc/resolv.conf => /run/systemd/resolve/resolv.conf 

# 查看系统解析
systemd-resolve --status
```

bind9
```bash
# /etc/bind/named.conf.options

#     forward only;
#     forwarders {223.5.5.5;};

# 系统bug
# sudo rm -f /etc/resolv.conf
# sudo ln -s /run/systemd/resolve/resolv.conf /etc/resolv.conf
# reboot
```

dnsmasq
```bash
sudo apt-get install dnsmasq -y

sudo systemctl disable systemd-resolved
sudo systemctl stop systemd-resolved

sudo systemctl enable dnsmasq

# addn-hosts=/etc/dnsmasqhosts
sudo bash -c "cat >> /etc/dnsmasq.conf" << EOF
resolv-file=/etc/resolv.dnsmasq.conf
EOF

sudo bash -c "cat > /etc/resolv.dnsmasq.conf" << EOF
nameserver 223.5.5.5
EOF

# 服务器没有networkmanager 就加
# sudo rm -rf /etc/resolv.conf
# sudo bash -c "cat > /etc/resolv.conf" << EOF
# nameserver 127.0.0.1
# EOF

sudo systemctl restart dnsmasq

# 配置/etc/docker/daemon.json
"dns": ["172.17.0.1"]
```

networkmanager
```bash
sudo systemctl restart network-manager
sudo vim /etc/NetworkManager/NetworkManager.conf
```

* https://www.chenyudong.com/archives/docker-custom-hosts-network-via-dns.html (修改容器内的host)
* https://www.hiroom2.com/2018/05/06/ubuntu-1804-bind-en/ (bind9配置)
* https://askubuntu.com/questions/973017/wrong-nameserver-set-by-resolvconf-and-networkmanager (修改hosts)
* https://askubuntu.com/questions/907246/how-to-disable-systemd-resolved-in-ubuntu (禁止系统的systemd-resolved)

# 5. 开发心得

总结下来,一般程序分为输入,输出和交互

* 输入 =>  1. 命令行flags 2. 环境变量 3. 配置文件
* 输出 => 日志
* 交互 => 1. docker容器访问其他docker容器ipv4 2. docker容器访问宿主机 3. 宿主机访问docker容器

可执行程序一般在 =>  1. /usr/local/bin  2. /usr/bin 中.

我们调试运行程序不可能是docker解决任何问题的,也需要宿主机跑起来程序,然后用gdb,或者ide进行调试.(注释部分docker-compose)  那么最好就是宿主机的配置和docker环境的配置保持一致.

输入:

1. 命令行flags  => 没啥问题
2. 环境变量 => 没啥问题, 宿主机放在 ~/.local/etc/local.sh  中, docker 用docker-compose environment
3. 配置文件 =>  1) 尽量使用特定目录的, /env/xxx/cfg/xxx.cfg.  那容器外内都一致了 2. 如果特定在/etc/xxx/xxx.cfg 可以创建软链接

输出:

日志 => stdout rotatelogs 输出到/env/xxx/log/  容器内外都一致

交互

1. docker容器访问其他docker容器ipv4 -> 
2. docker容器访问宿主机  ->
3. 宿主机访问docker容器  -> 
<!-- 4. 容器跨网络访问其他网络的容器 -->
