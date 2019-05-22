

<!-- TOC -->

- [1. 资料](#1-资料)
- [2. 安装](#2-安装)
- [3. 缩小体积](#3-缩小体积)
- [4. 网络](#4-网络)

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
