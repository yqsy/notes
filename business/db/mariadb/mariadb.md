<!-- TOC -->

- [1. 说明](#1-说明)
- [2. 安装](#2-安装)

<!-- /TOC -->



<a id="markdown-1-说明" name="1-说明"></a>
# 1. 说明

```bash
cd /mnt/disk1/linux/reference/refer/db
git clone https://github.com/MariaDB/server
git checkout tags/mariadb-10.4.3
git branch -d master
git checkout -b master

```

<a id="markdown-2-安装" name="2-安装"></a>
# 2. 安装

```bash
sudo pacman -S --noconfirm mariadb

# 创建数据库
sudo mysql_install_db --user=mysql --basedir=/usr --datadir=/var/lib/mysql
```

启动:
```bash
sudo systemctl start mariadb.service
sudo systemctl stop mariadb.service
sudo systemctl status mariadb.service
```

设置密码:
```bash
# 设置root密码
# mysqladmin -u root password 'new-password'
# mysqladmin -u root -h yq-pc password 'new-password'

# 初始化设置　（包括密码）
mysql_secure_installation

# 修改密码
use mysql;
update user set password=password("123456") where user="root";
flush privileges;
quit;

# 记住datagrip 密码存储方式设置为 inkeepass
```

重置数据库:
```bash
sudo mv /var/lib/mysql /var/lib/mysql.bak
```

操作:
```bash
# 登录
mysql -u root -p
```
