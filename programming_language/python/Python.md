
<!-- TOC -->

- [1. 资源](#1-资源)
- [2. 套路](#2-套路)

<!-- /TOC -->

# 1. 资源

* http://www.oschina.net/translate/open-sourcing-a-python-project-the-right-way (以正确的方式开源python)
* https://www.zhihu.com/question/19900260 (使用python会降低程序员的能力吗)



# 2. 套路

```bash
from __future__ import absolute_import, division, print_function, \
    with_statement
    
# absolute_import: 绝对引入
# division: 精确除法, python3 不需要
# print_function: 打印加括号, pytho3 不需要
# with_statement: with特性, python3 不需要

```
