---
title: ansible
date: 2018-1-30 23:56:06
categories: [linux, 系统管理]
---
<!-- TOC -->

- [1. 资源](#1-资源)
- [2. 安装实践](#2-安装实践)

<!-- /TOC -->


<a id="markdown-1-资源" name="1-资源"></a>
# 1. 资源

* https://www.ansible.com/ (官网)
* http://docs.ansible.com/ansible/latest/intro_installation.html (安装文档)
* http://ansible-tran.readthedocs.io/en/latest/docs/ (中文文档)
* https://www.ansible.com/resources/get-started (视频教学)

<a id="markdown-2-安装实践" name="2-安装实践"></a>
# 2. 安装实践

* epel
* apt-get
* pip
* source (via github)

```bash
yum install ansible -y

# 添加管理的机器
/etc/ansible/hosts

# 设置无视key check
export ANSIBLE_HOST_KEY_CHECKING=False

al1
dgc1
vul1
vul2
vm1

# ping 所有机器
ansible all -m ping

ansible all -m ping -u user --sudo

ansible all -a "/bin/echo hello"

# cobbler 可以批量装机器

# yum playbook
http://docs.ansible.com/ansible/latest/yum_module.html

# 拷贝文件?
http://docs.ansible.com/ansible/latest/template_module.html

# 当文件改动时
notify:

# 也支持shell哦
http://docs.ansible.com/ansible/latest/shell_module.html

# 打印执行playbook的主机
playbook.yml --list-hosts

ansible-playbook playbook.yml -f 10

# 幂等性很重要
```

web服务example
```bash
---
- hosts: webservers
  vars:
    http_port: 80
    max_clients: 200
  remote_user: root
  tasks:
  - name: ensure apache is at the latest version
    yum: pkg=httpd state=latest
  - name: write the apache config file
    template: src=/srv/httpd.j2 dest=/etc/httpd.conf
    notify:
    - restart apache
  - name: ensure apache is running
    service: name=httpd state=started
  handlers:
    - name: restart apache
      service: name=httpd state=restarted
```

我自己的配置example
```bash
---
- hosts: my-servers
  remote_user: root
  tasks:
  - name: install software
    yum: pkg={{item}} state=latest
    with_items:
      - epel-release
      - glances
      - vim
      - telnet
      - git

  - name: config zsh | install
    yum: pkg=zsh state=latest

  - name: config zsh | remove
    file: path=~/.zshrc state=absent

  - name: config zsh | download
    get_url:
      url: https://raw.githubusercontent.com/yqsy/vim/master/etc/zshrc.zsh
      dest: ~/.zshrc

  - name: config zsh | set as default
    user: name=root shell=/bin/zsh
```
