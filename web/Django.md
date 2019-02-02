---
title: Django
date: 2018-1-31 22:10:29
categories: [web]
---


<!-- TOC -->

- [1. 资源](#1-资源)
- [2. 实践](#2-实践)
- [3. with docker](#3-with-docker)

<!-- /TOC -->

<a id="markdown-1-资源" name="1-资源"></a>
# 1. 资源
* https://docs.djangoproject.com/en/2.0/contents/ (初始教学)
* https://docs.djangoproject.com/en/2.0/ref/models/expressions/#avoiding-race-conditions-using-f (解决web服务器的race condition)
* https://docs.djangoproject.com/en/2.0/howto/static-files/ (静态文件)
* https://docs.djangoproject.com/en/2.0/intro/reusable-apps/ (打包)
* https://docs.djangoproject.com/en/2.0/topics/ (全部文档)
* https://code.ziqiangxuetang.com/django/django-tutorial.html (中文文档)

<a id="markdown-2-实践" name="2-实践"></a>
# 2. 实践

```bash
Python 3.6.2
pip 9.0.1 from c:\python36\lib\site-packages (python 3.6)

pip install django

# 显示版本
python -m django --version

# 创建一个工程
django-admin startproject mysite

# An app can be in multiple projects.
python manage.py startapp polls

# 运行工程
python manage.py runserver 0:8000

# 生成数据库结构?是的,可以看到migrations目录中有生成的文件
python manage.py makemigrations polls

# 生成sql (其实也不用执行啦)
python manage.py sqlmigrate polls 0001

# 在数据库创建model (默认是sqlite)
python manage.py migrate

# 交互访问源码模块
python manage.py shell 

# 单元测试
python manage.py test polls

# 导入模块
from polls.models import Question, Choice

# 创建用户名密码
python manage.py createsuperuser

# 打包整个工程??
python setup.py sdist

# 从tar包安装??
pip install --user dist/django-xxx-0.1.tar.gz

# 卸载??
pip uninstall dist/django-xxx-0.1.tar.gz
```

<a id="markdown-3-with-docker" name="3-with-docker"></a>
# 3. with docker

```
docker pull django:latest
```
