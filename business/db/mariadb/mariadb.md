<!-- TOC -->

- [1. 说明](#1-说明)
- [2. 安装](#2-安装)
- [3. 参考资料](#3-参考资料)

<!-- /TOC -->



# 1. 说明

```bash
cd /mnt/disk1/linux/reference/refer/db
git clone https://github.com/MariaDB/server
git checkout tags/mariadb-10.4.3
git branch -d master
git checkout -b master

```

# 2. 安装

```bash
# arch安装mariadb
sudo pacman -S --noconfirm mariadb

# ubuntu安装mariadb
sudo apt install mariadb-server -y

# 创建数据库
sudo mysql_install_db --user=mysql --basedir=/usr --datadir=/var/lib/mysql

# 重置数据库
sudo mv /var/lib/mysql /var/lib/mysql.bak

# 修改root密码
sudo systemctl stop mysql
sudo mysqld_safe --skip-grant-tables &
mysql
UPDATE mysql.user SET Password=PASSWORD('mysql123456') WHERE User='root';
FLUSH PRIVILEGES;
exit
sudo mysqladmin -u root -p shutdown
sudo systemctl start mysql

# 登录
mysql -u root -p
```

# 3. 参考资料

* https://www.ostechnix.com/how-to-reset-mysql-or-mariadb-root-password/ (修改mariadb的密码)