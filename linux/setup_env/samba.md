---
title: samba
date: 2018-02-01 13:29:12
categories: [linux, 搭建环境]
---


<!-- TOC -->

- [1. 资源](#1-资源)
- [2. 安装](#2-安装)

<!-- /TOC -->

<a id="markdown-1-资源" name="1-资源"></a>
# 1. 资源
* https://www.howtoforge.com/samba-server-installation-and-configuration-on-centos-7
* https://serverfault.com/questions/368340/how-to-configure-samba-to-allow-root-user-for-full-control-to-the-particular-sha (allow root)

<a id="markdown-2-安装" name="2-安装"></a>
# 2. 安装

```bash
sudo yum install samba samba-client samba-common -y
sudo mv /etc/samba/smb.conf /etc/samba/smb.conf.bak

sudo bash -c "cat > /etc/samba/smb.conf" << EOF
[vm1]
    comment = Admin Config Share  - Whatever
    path = /
    valid users = yq
    # force user = root
    # force group = root
    # invalid users = xxx
    # admin users = xxx
    writeable = Yes
EOF


sudo systemctl enable smb.service
sudo systemctl enable nmb.service
sudo systemctl restart smb.service
sudo systemctl restart nmb.service

sudo smbpasswd -a yq

sudo systemctl restart smb.service
sudo systemctl restart nmb.service

# windows:
# 清空会话
net use * /del /y
```
