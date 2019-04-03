<!-- TOC -->

- [1. 说明](#1-说明)
- [2. 参考资料](#2-参考资料)

<!-- /TOC -->


<a id="markdown-1-说明" name="1-说明"></a>
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
ansible all -m shell -a "curl -fsSL -H 'Cache-Control: no-cache' https://raw.githubusercontent.com/yqsy/initscript/master/bootstrap.sh | sh"


# gs装软件

```

<a id="markdown-2-参考资料" name="2-参考资料"></a>
# 2. 参考资料

* http://www.ansible.com.cn/docs/intro_getting_started.html#a-note-about-host-key-checking
* http://www.ansible.com.cn/docs/intro_inventory.html (服务器配置文件)
