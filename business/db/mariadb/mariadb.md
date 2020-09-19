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
`
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
sudo mysql -u root -p

# 设置下datagrip就可以登录了
sudo mysql -u root
use mysql;
update user set plugin='' where User='root';
flush privileges;
exit;


# 通过ssh tunel 登录(新)
# ak 艾克 贝吉塔 辉煌
ssh -NL 3311:127.0.0.1:3306 yq@64.64.240.56 -p 26348 -i /d/linux/reference/project/yqinitialize/id_rsa

# 带土 
ssh -NL 3314:127.0.0.1:3306 yq@80.251.223.171 -p 28245 -i /d/linux/reference/project/yqinitialize/id_rsa

# 冰魄 
ssh -NL 3312:127.0.0.1:3306 yq@199.19.105.50  -p 27746 -i /d/linux/reference/project/yqinitialize/id_rsa

# 龙庭
ssh -NL 3313:127.0.0.1:3306 yq@80.251.213.48 -p  26809 -i /d/linux/reference/project/yqinitialize/id_rsa

# 九州
ssh -NL 3314:127.0.0.1:3306 yq@80.251.221.227 -p 27995 -i /d/linux/reference/project/yqinitialize/id_rsa
```


```bash
# 通过ssh tunel 登录 (旧)

# ak 艾克
ssh -NL 3306:127.0.0.1:3306 yq@175.24.15.156 -i /d/linux/reference/project/yqinitialize/id_rsa
# 贝吉塔
ssh -NL 3307:127.0.0.1:3306 yq@175.24.95.64 -i /d/linux/reference/project/yqinitialize/id_rsa

# 带土
ssh -NL 3308:127.0.0.1:3306 yq@212.64.76.143 -i /d/linux/reference/project/yqinitialize/id_rsa

# 冰魄
ssh -NL 3309:127.0.0.1:3306 yq@134.175.145.133 -i /d/linux/reference/project/yqinitialize/id_rsa

# 龙庭
ssh -NL 3311:127.0.0.1:3306 yq@129.204.15.85 -i /d/linux/reference/project/yqinitialize/id_rsa

# 九州
ssh -NL 3310:127.0.0.1:3306 yq@49.235.238.233 -i /d/linux/reference/project/yqinitialize/id_rsa

```

# 3. 参考资料

* https://www.ostechnix.com/how-to-reset-mysql-or-mariadb-root-password/ (修改mariadb的密码)
