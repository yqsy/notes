---
title: shell
date: 2017-11-03 21:41:00
categories: [linux, 系统管理]
---

<!-- TOC -->

- [1. 特性](#1-特性)
    - [1.1. 快捷键](#11-快捷键)
- [2. 使用场景](#2-使用场景)
- [3. 竖杠的含义](#3-竖杠的含义)
- [4. 各种符号含义](#4-各种符号含义)
- [5. 运算符号](#5-运算符号)
    - [5.1. 文件类型运算符](#51-文件类型运算符)
    - [5.2. 文件权限运算符](#52-文件权限运算符)
    - [5.3. 比较数字](#53-比较数字)
- [6. 常用语句](#6-常用语句)
- [7. 标注输入输出](#7-标注输入输出)
- [8. sed的常见语法](#8-sed的常见语法)
- [9. xargs/expr/exec](#9-xargsexprexec)
    - [9.1. xargs和exec在使用中的不同](#91-xargs和exec在使用中的不同)
- [10. sort,wc,uniq](#10-sortwcuniq)
- [11. 转义符](#11-转义符)
- [12. 高级bash](#12-高级bash)

<!-- /TOC -->


<a id="markdown-1-特性" name="1-特性"></a>
# 1. 特性
`/bin/bash`时Linux默认的shell,时GNU计划中重要的工具软件之一

shell意思为`命令行界面`,是UNIX操作系统中最为重要的部分之一,Unix的shell有很多中,他们都是基于Bourne shell(/bin/sh)这个贝尔实验室开发的标准shell.Linux使用了一个增强版本的Bourne shell,我们称之为bash或者"Bourne-again" shell,大部分Linux系统的默认shell是bash,可用`chsh`命令来修改默认shell

* history可查看输入历史,`~/.bash_history`
* tab命令补全
* 命令别名设置(alias),例如` alias lm='ls -al'`
* 工作控制,前景背景控制 (job control, foreground, background)
* 程序化脚本(shell script)
* 万用字符: (Wildcard)

<a id="markdown-11-快捷键" name="11-快捷键"></a>
## 1.1. 快捷键

* ctrl+u 向前删除字符串
* ctrl+k 向后删除字符串
* ctrl+a 光标移动到最前面
* ctrl+e 光标移动到最后面
* ctrl+s vim画面锁死  strl+q恢复
* ctrl+c 终止目前的命令
* ctrl+d 输入结束(eof),例如邮件结束的时候
* ctrl+m enter
* ctrl+z 暂停目前的命令

<a id="markdown-2-使用场景" name="2-使用场景"></a>
# 2. 使用场景

请记住shell脚本的强项: 强控简单的文件和命令,当你发现你的脚本写得有点繁琐,特别时涉及复杂的字符串或数学处理时,或许你就该实时Python,Perl或awk之类的脚本语言

* https://stackoverflow.com/questions/209470/can-i-use-python-as-a-bash-replacement (使用python替代shell)
* http://plumbum.readthedocs.io/en/latest/ (库)

<a id="markdown-3-竖杠的含义" name="3-竖杠的含义"></a>
# 3. 竖杠的含义

* http://www.linfo.org/vertical_bar_character.html
* http://www.linfo.org/pipe.html


<a id="markdown-4-各种符号含义" name="4-各种符号含义"></a>
# 4. 各种符号含义

符号|含义
-|-
单引号|保证shell不做任何转换
双引号|同上,只不过shell会对双引号中的所有变量进行扩展
$+数字|单个参数
$#|参数的数量
$@|代表脚本接收的所有参数
$0|脚本名
$?|退出码

注意
* 引号中的任何东西都会被当成一个参数


字符|名称|用途
-|-|-
*|星号|正则表达式,通用字符
,|句点|当前目录,文件/主机名的分隔符
!|感叹号|逻辑非运算符,命令历史
竖杠符号|管道|命令管道
/|斜线|目录分割符,搜索命令
`\`|反斜线|常量,宏(非目录)
$|美元符号|变量符号,行尾
'|单引号|字符串常量
`|反引号|命令替换
"|双引号|半字符串常量
^|脱字符|逻辑非运算符,行头
~|波浪字符|逻辑非运算符,目录快捷方式
`#`|井号|注释,预处理,替换
[]|方括号|范围
{}|大括号|声明块,范围
_|下划线|空格的简易替代


<a id="markdown-5-运算符号" name="5-运算符号"></a>
# 5. 运算符号

<a id="markdown-51-文件类型运算符" name="51-文件类型运算符"></a>
## 5.1. 文件类型运算符

运算符|用于测试
-|-
-f|普通文件
-d|目录
-h|符号链接
-b|块设备
-c|字符设备
-p|命名管道
-S|套接字


<a id="markdown-52-文件权限运算符" name="52-文件权限运算符"></a>
## 5.2. 文件权限运算符

运算符|用于测试
-|-
-r|可读
-w|可写
-x|可执行
-u|Setuid
-g|Setgid
-k|Sticky

<a id="markdown-53-比较数字" name="53-比较数字"></a>
## 5.3. 比较数字

运算符|当参数一与参数二相比,....时,返回true
-|-
-eq|相等
-ne|不等
-lt|更小
-gt|更大
-le|更小或相等
-ge|更大或相等
 
<a id="markdown-6-常用语句" name="6-常用语句"></a>
# 6. 常用语句

```bash
# 条件判断
if [ $1 = hi ]; then
    echo 'The first argument was "hi"'
else
    echo -n 'The first argument was not "hi" -- '
    echo it was '"'$1'"'
fi

# elif
if [ "$1" = "hi" ]; then
   echo 'The first argument was "hi"'
elif [ "$2" = "bye" ]; then
   echo 'The second argument was "bye"'
else
   echo -n 'The first argument was not "hi" and the second was not "bye"-- '
   echo They were '"'$1'"' and '"'$2'"'
fi

# -f表示普通文件
for filename in *; do
    if [ -f $filename ]; then
        ls -l $filename
        file $filename
    else
        echo $filename is not a regular file.
    fi
done

# case进行字符串匹配
case $1 in
    bye)
        echo Fine, bye.
        ;;
    hi|hello)
        echo Nice to see you.
        ;;
    what*)
        echo Whatever.
        ;;
    *)
       echo 'Huh?'
       ;;
esac

# for循环
for str in one two three four; do
    echo $str
done

# while循环
#!/bin/sh
FILE=/tmp/whiletest.$$;
echo firstline > $FILE
while tail -10 $FILE | grep -q firstline; do
    # add lines to $FILE until tail -10 $FILE no longer prints "firstline"
    echo -n Number of lines in $FILE:' '
    wc -l $FILE | awk '{print $1}'
    echo newline >> $FILE
done

rm -f $FILE
```


<a id="markdown-7-标注输入输出" name="7-标注输入输出"></a>
# 7. 标注输入输出

按`ctrl-d`终止当前终端的标准输入并终止命令.`ctrl-c`终止当前进程的运行.

标准输入和标注输出通常简写为`stdin`和`stdout`,标准错误输出`stderr`

重定向
```bash

# 如果文件不存在,会创建文件,如果文件已经存在,shell会清空文件内容
command > file

# 不想文件内容被清空
command >> file

# 流ID 1是标准输出,2是标准错误输出
# 重定向标准错误输出至标准输出
ls /ffffffff > f 2>&1

# 标准输入重定向
head < /proc/cpuinfo
```

<a id="markdown-8-sed的常见语法" name="8-sed的常见语法"></a>
# 8. sed的常见语法

```bash

# 根据一个正则表达式进行内容替换
sed 's/exp/test/'

# 将/etc/passwd的第一个冒号替换成%
sed 's/:/%/' /etc/passwd

# 将/etc/passwd的所有冒号都换成%,在末尾加上g
sed 's/:/%/g' /etc/passwd

# 读取/etc/passwd,并把三到六行去掉,打印到标准输出
sed 3,6d /etc/passwd
```

<a id="markdown-9-xargsexprexec" name="9-xargsexprexec"></a>
# 9. xargs/expr/exec
当把海量的文件当作一个命令的参数时,该命令或者shell可能会告诉你缓冲不足以容纳这些参数,解决这个问题,可用`xargs`,它能对自身输入流的每个文件名逐个地执行命令

<a id="markdown-91-xargs和exec在使用中的不同" name="91-xargs和exec在使用中的不同"></a>
## 9.1. xargs和exec在使用中的不同

* https://en.wikipedia.org/wiki/Xargs
* https://www.endpoint.com/blog/2010/07/28/efficiency-of-find-exec-vs-find-xargs

```bash

# 下面两句在文件多时会出错Argument list too long
rm /path/*
rm $(find /path -type f)

# xargs本质上就是管道, 一个输出作为另一个命令的输入, 参数全部传
# xargs用时一定要注意加print0和xargs -0,防止文件名有空格
find . -name '*.cpp' -type f -print0 | xargs -0 file

# 或者直接使用-exec,参数是一个一个传
# $0是脚本名 {}是find出的单个文件名
find . -name '*.h' -type f -exec bash -c 'expand -t 4 "$0" > /tmp/e && mv /tmp/e "$0"' {} \;
```

```bash
# 验证.gif是否是真的gif
find . -name '*.gif' -print0 | xargs -0 file

# 或者可以这样写
find . -name '*.gif' -exec file {} \;
```

exec命令时shell内置的,他会用其后的程序的进程来取代你当前的shell进程,当在shell窗口中运行exec cat时,按下ctrl-d或ctrl-c时,shell窗口就会小时,因为没有任何子进程了

<a id="markdown-10-sortwcuniq" name="10-sortwcuniq"></a>
# 10. sort,wc,uniq

```bash
# 个人账号进行排序
cat /etc/passwd | sort

# 第三栏排序
cat /etc/passwd | sort -t ':' -k 3

# 利用last,将输出的数据仅取账号,并加以排序
last | cut -d ' ' -f1 | sort

# 使用last将账号列出,仅取出账号栏,进行排序后仅取出一位
last | cut -d ' ' -f1 | sort | uniq

# 知道每个人的登录总次数
last | cut -d ' ' -f1 | sort | uniq -c

# /etc/man_db.conf 里面到底有多少相关字,行,字符数
cat /etc/man_db.conf | wc
```


<a id="markdown-11-转义符" name="11-转义符"></a>
# 11. 转义符

我差点天真地以为http协议或者是memcached协议的\r\n是4个字节的了  
其实是转义符啦  

* telnet按回车是CRLF
* netcat按回车是LF
* netcat 这样配置是CRLF nc -C localhost 11211
* echo 可以这样搭配(不过马上就退出)echo -ne 'set x 0 900 1 x\r\nget x\r\n' | nc localhost 11211

输入方法:
* http://ascii-table.com/control-chars.php (输入转义符号的表)
* http://www.asciitable.com/ (ascii表)

实在不行的话用tcpdump搞清楚


<a id="markdown-12-高级bash" name="12-高级bash"></a>
# 12. 高级bash

* https://www.zhihu.com/question/21418449 (zsh韦易笑)
* https://www.zhihu.com/question/29977255 (zsh)
* https://github.com/zsh-users/antigen (插件管理)
* https://www.howtoforge.com/tutorial/how-to-setup-zsh-and-oh-my-zsh-on-linux/ (如何安装oh-my-zsh)
* https://github.com/arialdomartini/oh-my-git/issues/10 (putty zsh符号显示不全解决方法)
* https://github.com/gabrielelana/awesome-terminal-fonts/tree/patching-strategy/fonts (putty 字体 windows可用的吧)
* https://github.com/powerline/fonts (powerline 字体)
* https://github.com/robbyrussell/oh-my-zsh/wiki/Themes (所有主题)

```bash
# 安装fish
yum install fish -y
chsh -s /usr/bin/fish
```

```bash
# 安装zsh
yum install zsh -y
chsh -s /bin/zsh

# 插件管理
mkdir -p $HOME/.local/bin
curl -L git.io/antigen > $HOME/.local/bin/antigen.zsh

# 直接用韦易笑的脚本
curl -L https://raw.githubusercontent.com/yqsy/vim/master/etc/zshrc.zsh > ~/.zshrc
```

oh-my-zsh
```bash
# oh-my-zsh
echo $SHELL
wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O - | zsh
cp ~/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc
source ~/.zshrc
```
