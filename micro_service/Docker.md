

<!-- TOC -->

- [1. 资料](#1-资料)
- [2. 安装](#2-安装)
- [3. 指令](#3-指令)

<!-- /TOC -->


# 1. 资料

* https://hujb2000.gitbooks.io/docker-flow-evolution/content/cn/index.html (Docker入门与实战)
* https://docs.docker.com/engine/getstarted/ (官方文档)
* http://www.docker.org.cn/book/docker/what-is-docker-16.html (docker中文社区)
* https://stackoverflow.com/questions/30494050/how-do-i-pass-environment-variables-to-docker-containers (传递环境变量给docker)
* https://docs.docker.com/engine/admin/volumes/volumes/ (manager data in docker)
* https://nickjanetakis.com/blog/the-3-biggest-wins-when-using-alpine-as-a-base-docker-image (各大base镜像大小)


# 2. 安装

* https://mirrors.tuna.tsinghua.edu.cn/help/docker-ce/ (到这里安装?清华源?不对)
* https://www.docker-cn.com/registry-mirror (中国官方的源)


```bash
https://docs.docker.com/install/linux/docker-ce/ubuntu/

# ubuntu
sudo apt-get remove docker docker-engine docker.io containerd runc

sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo apt-key fingerprint 0EBFCD88
sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io
sudo docker run hello-world

sudo groupadd docker
sudo gpasswd -a $USER docker
# newgrp docker 
```

```bash
# 改变源

mkdir -p /etc/docker
echo \
"{
  \"registry-mirrors\": [\"https://registry.docker-cn.com\"]
}" > /etc/docker/daemon.json
```

```bash
yum install docker -y
systemctl start docker
systemctl enable docker

systemctl status docker

yum install docker-compose -y
# https://github.com/certbot/certbot/issues/5104
pip install requests urllib3 pyOpenSSL --force --upgrade

```

# 3. 指令

```bash

# 运行就删除
docker run -it --rm debian bash
docker run -it --rm nginx bash

-i, --interactive                 Keep STDIN open even if not attached
-t, --tty                         Allocate a pseudo-TTY
--rm                          Automatically remove the container when it exits

# 附加到容器
docker exec -it xxx bash;

# 暂停和删除所有容器
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)

# 删除none标签的images
docker rmi $(docker images -f "dangling=true" -q)

# 含义
RUN set -ex; 

-e 遇到错误时退出
-x 打印执行语句



```
