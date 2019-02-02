---
title: Windows常用积累
date: 2017-11-06 15:20:00
categories: [coding]
---

<!-- TOC -->

- [1. 常用](#1-常用)
- [2. 穿墙应用或国内源](#2-穿墙应用或国内源)
- [3. Freecommander技巧](#3-freecommander技巧)
    - [3.1. git](#31-git)
    - [3.2. 比较](#32-比较)
    - [3.3. everything](#33-everything)
- [4. visual code 积累](#4-visual-code-积累)
- [5. putty配置](#5-putty配置)

<!-- /TOC -->


<a id="markdown-1-常用" name="1-常用"></a>
# 1. 常用

```bash
# telnet安装
pkgmgr /iu:"TelnetClient"

# 刷新dns
ipconfig /flushdns

# 注册/卸载DLL
Regsvr32 /S VA_X.dll
Regsvr32 /S /U VA_X.dll

# 查看静态库
dumpbin.exe -headers glog.lib > export.txt

# 新装网卡驱动时,注意安装官方原版
realtek

# dig
https://www.isc.org/downloads/

# 远程连接
mstsc

# 查看屏幕尺寸
dxdiag

# mstsc full screen on second monitor
http://www.fixedbyvonnie.com/2013/12/how-to-open-full-screen-remote-desktop-session-secondary-monitor-in-windows/#.WUi7XeuGOHs

# git bahs 在conenum以管理员启动
"%ConEmuDrive%\Program Files (x86)\Git\bin\sh.exe" --login -i -new_console:a
```

<a id="markdown-2-穿墙应用或国内源" name="2-穿墙应用或国内源"></a>
# 2. 穿墙应用或国内源

```bash
# git(只能代理https,ssh的无效)
git config --global http.proxy 'socks5://127.0.0.1:1080' 
git config --global https.proxy 'socks5://127.0.0.1:1080'

# pip
vim C:\Users\Gong.guochun\pip\pip.ini

[global]
proxy = 127.0.0.1:1080

# atom
apm config set proxy "http://127.0.0.1:1080"
apm config set https_proxy "http://127.0.0.1:1080"

# go get
env `https_proxy` http://127.0.0.1:1080

# nodejs npm (使用cnpm替换npm)
npm install cnpm -g --registry=https://registry.npm.taobao.org

```

<a id="markdown-3-freecommander技巧" name="3-freecommander技巧"></a>
# 3. Freecommander技巧

<a id="markdown-31-git" name="31-git"></a>
## 3.1. git
定义快捷键:
* Ctrl + Alt + P -> git push
* Ctrl + Alt + U -> git pull
* Ctrl + Alt + L -> git log
* Ctrl + Alt + D -> git diff
* Ctrl + Alt + C -> git commit

设置:
* 程序或文件夹: C:\Program Files\TortoiseGit\bin\TortoiseGitProc.exe
* 安装文件夹: C:\Program Files\TortoiseGit\bin
* 参数: /command:push /path:%ActivSel%


<a id="markdown-32-比较" name="32-比较"></a>
## 3.2. 比较

设置:
* 程序或文件夹: C:\Program Files\Beyond Compare 4\BCompare.exe
* 安装文件夹: C:\Program Files\Beyond Compare 4
* 参数: %LeftSel% %RightSel%

<a id="markdown-33-everything" name="33-everything"></a>
## 3.3. everything
定义快捷键:
* Ctrl + Alt + F -> 搜索active 目录

设置:
* 程序或文件夹: C:\Program Files\Everything\Everything.exe
* 安装文件夹: C:\Program Files\Everything
* 参数: -filename %ActivDir%

<a id="markdown-4-visual-code-积累" name="4-visual-code-积累"></a>
# 4. visual code 积累

* https://code.visualstudio.com/insiders (多个目录)

插件:
* c/c++
* Clang-Format (win需要安装llvm http://releases.llvm.org/)
* c/c++ Clang Command Adapter
* Python
* Markdown TOC
* Material Icon Theme
* Markdown PDF

折叠技巧:
* https://stackoverflow.com/questions/30067767/how-do-i-collapse-sections-of-code-in-visual-studio-code-for-windows
* ctrl+k,ctrl+0 
* ctrl+k,ctrl+j

修改的设置:

* https://code.visualstudio.com/docs/languages/cpp (c++ auto complete)
* "editor.formatOnSave": true,

数学公式:
* https://marketplace.visualstudio.com/items?itemName=goessner.mdmath

<a id="markdown-5-putty配置" name="5-putty配置"></a>
# 5. putty配置
0.70版本

* window-appearance-font (默认字体难看)
* Terminal-Features-Disable remote-controlled window title changing (不修改标题)
* Connection-Data-Terminal-type string linux (home end 键)
