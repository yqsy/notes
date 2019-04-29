<!-- TOC -->

- [1. 说明](#1-说明)
- [2. 参考资料](#2-参考资料)

<!-- /TOC -->


# 1. 说明

```bash

sudo pip install ansible

sudo mkdir -p /etc/ansible
sudo chown `whoami`:`id -g -n` /etc/ansible

# 增加地址
sudo vim /etc/ansible/hosts 

ansible all -m ping
ansible all -a "/bin/echo hello"

# 初始化
ansible all -m shell -a "rm -rf ~/.antigen"
ansible all -m shell -a "rm -rf ~/.zshrc"
ansible all -m shell -a "curl -fsSL -H 'Cache-Control: no-cache' https://gitee.com/yqsy/initscript/raw/master/bootstrap.sh | bash"

# 是否允许密码登录
ansible all -m shell -a "sudo grep PasswordAuthentication /etc/ssh/sshd_config"
ansible all -m shell -a "sudo netstat -tulpn"
ansible all -m shell -a "sudo w"
ansible all -m shell -a "sudo last -n 20"
```

# 2. 参考资料

* http://www.ansible.com.cn/docs/intro_getting_started.html#a-note-about-host-key-checking
* http://www.ansible.com.cn/docs/intro_inventory.html (服务器配置文件)
