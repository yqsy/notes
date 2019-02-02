---
title: Windows开发Linux程序积累
date: 2017-11-12 15:20:00
categories: [coding]
---

<!-- TOC -->

- [1. 基础要点](#1-基础要点)
- [2. Windows写LinuxC /C++代码](#2-windows写linuxc-c代码)
- [3. Windows类Linux操作环境](#3-windows类linux操作环境)
    - [3.1. Cygwin](#31-cygwin)
    - [3.2. MinGW](#32-mingw)
    - [3.3. MSYS](#33-msys)
    - [3.4. MinGW-w64](#34-mingw-w64)
    - [3.5. MYSYS2](#35-mysys2)
- [4. windows g++ 编译器选择](#4-windows-g-编译器选择)
- [5. 调试](#5-调试)
- [6. 代码同步](#6-代码同步)
    - [6.1. beyond compare](#61-beyond-compare)
    - [6.2. rsync+inotifywait](#62-rsyncinotifywait)
- [7. samba-终极方案](#7-samba-终极方案)

<!-- /TOC -->


<a id="markdown-1-基础要点" name="1-基础要点"></a>
# 1. 基础要点

平常开发的主要是Linux后台程序,开发平台为windows

因为有些语言或库对对于跨平台不理想,所以还是需要`windows编辑`+`Linux运行/调试`那么有几个问题需要注意,整理一下:

* Windows如何写Linux C/C++代码 (code auto complete/头文件)
* Windows类Linux操作环境
* 如何将代码从Windows sync 到Linux之上
* 源代码文件从`CRLF`转换成`LF`(git + ide搭配控制好)
* 某些语言,tab转换成空格(ide自动做到)
* 某些语言,注意编码(只有`c/c++`需要注意,不要写中文把)

<a id="markdown-2-windows写linuxc-c代码" name="2-windows写linuxc-c代码"></a>
# 2. Windows写LinuxC /C++代码

使用工具
* https://www.jetbrains.com/clion/ (太重量级了)
* https://code.visualstudio.com/insiders/ (轻巧些)
* understand (看代码用)

参考
* https://code.visualstudio.com/docs/languages/cpp
* https://stackoverflow.com/questions/17939930/finding-out-what-the-gcc-include-path-is (得知头文件路径)

`Ctrl+Shift+P`将头文件目录设置成linux的头文件

```
"name": "Win32",
"includePath": [
    "${workspaceRoot}",
    "C:/work/source/refer/usr/include/c++/4.8.5",
    "C:/work/source/refer/usr/include/c++/4.8.5/x86_64-redhat-linux",
    "C:/work/source/refer/usr/include/c++/4.8.5/backward",
    "C:/work/source/refer/usr/lib/gcc/x86_64-redhat-linux/4.8.5/include",
    "C:/work/source/refer/usr/include",
    "C:/work/source/refer/usr/local/include",
    "C:/work/source/refer/muduo"
],
```

```bash
# 得知头文件搜索路径
`gcc -print-prog-name=cc1` -v
`gcc -print-prog-name=cc1plus` -v

# c
/usr/local/include
/usr/include
/usr/lib/gcc/x86_64-redhat-linux/4.8.5/include


# c++
/usr/local/include
/usr/include
/usr/include/c++/4.8.5
/usr/include/c++/4.8.5/x86_64-redhat-linux
/usr/include/c++/4.8.5/backward
/usr/lib/gcc/x86_64-redhat-linux/4.8.5/include

# linux
# 拷贝头文件
tar -cvzf /tmp/include.tgz /usr/include
tar -cvzf /tmp/lib_gcc_include.tgz /usr/lib/gcc/x86_64-redhat-linux/4.8.5/include
tar -cvzf /tmp/usr_local_include.tgz /usr/local/include

# windows

dstpath=/c/work/source/refer

scp root@vm1:/tmp/include.tgz $dstpath
tar -xvzf include.tgz

scp root@vm1:/tmp/lib_gcc_include.tgz $dstpath
tar -xvzf lib_gcc_include.tgz

scp root@vm1:/tmp/usr_local_include.tgz $dstpath
tar -xvzf usr_local_include.tgz
```

```bash
# rsync同步
# 记住: 如果源头是文件夹那么就会拷贝文件夹

dstpath=/c/work/source/refer

rsync -azvh --force root@vm1:/usr/include $dstpath/usr

mkdir -p $dstpath/usr/lib/gcc/x86_64-redhat-linux/4.8.5
rsync -avzh --force root@vm1:/usr/lib/gcc/x86_64-redhat-linux/4.8.5/include $dstpath/usr/lib/gcc/x86_64-redhat-linux/4.8.5

mkdir -p $dstpath/usr/local
rsync -azvh --force root@vm1:/usr/local/include $dstpath/usr/local

# -a, --archive               archive mode;
# -v, --verbose               increase verbosity
# -h, --human-readable        output numbers in a human-readable format
# -z, --compress              compress file data during the transfer
```

<a id="markdown-3-windows类linux操作环境" name="3-windows类linux操作环境"></a>
# 3. Windows类Linux操作环境

* https://www.zhihu.com/question/22137175
* https://www.zhihu.com/question/39952667 (怎么选择mingw mingw-w64 tdm-gcc)

<a id="markdown-31-cygwin" name="31-cygwin"></a>
## 3.1. Cygwin
提供了运行于Windows平台的类Unix环境,提供了一套抽象层dll,用于将部分Posix调用转换成Windows的调用API (基本就是传说中的GNU/NT系统 对照GNU/Linux,GNU/BSD,GNU/HURD)

<a id="markdown-32-mingw" name="32-mingw"></a>
## 3.2. MinGW
Minimalist GNU for Windows,用于进行Windows应用开发的GNU工具链(开发环境)

<a id="markdown-33-msys" name="33-msys"></a>
## 3.3. MSYS
辅助Windows版MinGW进行命令行开发的配套软件包,提供了部分Unix工具以使得MinGW的工具使用起来更方便一些.如果不喜欢庞大的Cygwin,而且使用不多,可以试试.不过喜欢完整体验,不在乎磁盘占用等等,还是推荐Cygwin而不是MSYS

<a id="markdown-34-mingw-w64" name="34-mingw-w64"></a>
## 3.4. MinGW-w64

新一代的MinGW,支持更多的API,支持64位应用开发

<a id="markdown-35-mysys2" name="35-mysys2"></a>
## 3.5. MYSYS2

fork了Cygwin,对于不喜欢庞大的Cygwin的用户而言,推荐试试mysys2

<a id="markdown-4-windows-g-编译器选择" name="4-windows-g-编译器选择"></a>
# 4. windows g++ 编译器选择
* https://www.zhihu.com/question/39952667


<a id="markdown-5-调试" name="5-调试"></a>
# 5. 调试

* https://zhuanlan.zhihu.com/p/32843449?group_id=934863168711348224 (韦易笑的)
* http://blog.csdn.net/shyanyang/article/details/37349135 (emacs gdb多窗口布局)
* https://gdbgui.com/downloads.html (游览器调试)
* https://sourceware.org/gdb/wiki/GDB%20Front%20Ends (全部工具)



```bash
# 安装gdb gui
yum install epel-release -y
yum install python-pip -y
pip install gdbgui -i https://pypi.tuna.tsinghua.edu.cn/simple --upgrade
gdbgui --host 0.0.0.0 xxx
```

<a id="markdown-6-代码同步" name="6-代码同步"></a>
# 6. 代码同步

<a id="markdown-61-beyond-compare" name="61-beyond-compare"></a>
## 6.1. beyond compare
文件夹同步-镜像功能,使用sftp协议,缺点是需要手动点击同步,比较繁琐

```bash
# 目的文件夹格式
sftp://root@vm1://root/reference/linux_socket_test
```

<a id="markdown-62-rsyncinotifywait" name="62-rsyncinotifywait"></a>
## 6.2. rsync+inotifywait

inotifywait
* https://github.com/thekid/inotify-win (c# .net 4.0编译)
* https://github.com/yqsy/inotify-win/files/1609484/inotifywait.zip

```bash
# 编译
csc.exe /t:exe /out:inotifywait.exe src\*.cs
```

rsync
* https://blog.tiger-workshop.com/add-rsync-to-git-bash-for-windows/
* https://www.computerhope.com/unix/rsync.htm (用法)

可以`排除.gitignore`中的文件以及`.git`文件夹,还有`删除多余的文件`
```bash
rsync -av ./ --filter=':- .gitignore' --cvs-exclude --delete root@192.168.198.130:/root/reference/linux_socket_test
```

inotifywait
```bash

inotifywait -mrq . | while read file ; do
    echo '111'
done

# inotifywait -mrq . --exclude '.git|.idea|.vscode|cmake-build-debug' | while read file ; do
#     rsync -avh . --filter=':- .gitignore' --cvs-exclude --delete-excluded --force root@vm1:/root/reference/linux_socket_test
#     echo {$file}
# done

# 建议用这种写法
while inotifywait -r . --exclude '.git|.idea|.vscode|cmake-build-debug'; do
    rsync -avh . --filter=':- .gitignore' --cvs-exclude  --force root@vm1:/root/reference/linux_socket_test
done
# --delete-excluded 看情况加不加,会清除中间文件

```

<a id="markdown-7-samba-终极方案" name="7-samba-终极方案"></a>
# 7. samba-终极方案

适用于本地虚拟机开发,目的是为了提高开发效率,使用visual studio 2017开发吧

映射成z:,everything也可以扫描

```
                "z:/opt/muduo/build/release-install-cpp11/include",
                "z:/usr/lib/gcc/x86_64-redhat-linux/4.8.2/include",
                "z:/usr/local/include",
                "z:/usr/include",
                "z:/usr/include/c++/4.8.5",
                "z:/usr/include/c++/4.8.5/x86_64-redhat-linux",
                "z:/usr/include/c++/4.8.5/backward"
```
