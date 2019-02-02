---
title: 从git迁移至svn
date: 2018-01-01 15:10:36
categories: [版本管理]
---

<!-- TOC -->

- [1. 资料](#1-资料)
- [2. 实践](#2-实践)
- [3. 创建git历史](#3-创建git历史)
- [4. 创建一个svn仓库以及checkout](#4-创建一个svn仓库以及checkout)
- [5. 将git的历史回归到svn](#5-将git的历史回归到svn)

<!-- /TOC -->

<a id="markdown-1-资料" name="1-资料"></a>
# 1. 资料

* https://zxtechart.com/2017/07/16/use-two-remote-repos-of-svn-and-git-at-the-same-time-for-the-same-project/ 
* https://superuser.com/questions/486683/setting-up-local-repository-with-tortoisesvn-in-windows


<a id="markdown-2-实践" name="2-实践"></a>
# 2. 实践
由于公司比较保守,不愿意使用分布式版本管理工具,而我一直使用git来管理版本,所以离职时要将git的提交历史回归到svn上

<a id="markdown-3-创建git历史" name="3-创建git历史"></a>
# 3. 创建git历史
```
mkdir local-git-repos
cd local-git-repos/
git init
touch test.txt
git add test.txt
git commit -am "Added test.txt."
echo aaaa >> test.txt
git commit -am "Added aaaa."
echo bbbb >> test.txt
git commit -am "Added bbbb."
```

<a id="markdown-4-创建一个svn仓库以及checkout" name="4-创建一个svn仓库以及checkout"></a>
# 4. 创建一个svn仓库以及checkout
```
cd C:\work\testrepo
svnadmin create svn-repos
svn co file:///C:/work/testrepo/svn-repos svn-client
cd svn-client/
mkdir trunk branches tags
svn add *
svn ci -m "Added trunk, branches and tags."
```

<a id="markdown-5-将git的历史回归到svn" name="5-将git的历史回归到svn"></a>
# 5. 将git的历史回归到svn

我还是觉得git svn是将svn的历史转到git,而不是git的历史转到svn,(或者可以,但是我这边尝试下来各种报错,这种很傻的事情没必要投入大量的精力尝试)
所以我得改变思路
```bash
cd C:\work\testrepo\local-git-repos

# --stdlayout 没加,加了报错
git svn init C:/work/testrepo/svn-repos/ --prefix=svn/

# 这个指令应该是svn -> git的
git rebase --onto remotes/svn/trunk --root master
```

* http://blog.ploeh.dk/2013/10/07/verifying-every-single-commit-in-a-git-branch/ (参考这个)


仅作参考吧,因为这种脚本可能在我程序员生涯里只会跑一次同是也是最后一次
```bash
shopt -s extglob

SRC=./cache
DEST=C:/back/other/svn/3源代码区/107Cache服务器/from-git

git --git-dir=cache/.git --work-tree=cache checkout master

COMMITS=$(git --git-dir=cache/.git --work-tree=cache log --oneline  --reverse | cut -d " " -f 1)

git --git-dir=cache/.git --work-tree=cache reset --hard
git --git-dir=cache/.git --work-tree=cache clean -fxd

for COMMIT in $COMMITS
do
    git --git-dir=cache/.git --work-tree=cache checkout $COMMIT

    MSG=$(git --git-dir=cache/.git --work-tree=cache log --format=%B -n 1 ${COMMIT})

    echo rm -rf $DEST/!(.svn|.|..)
    rm -rf $DEST/!(.svn|.|..)

    tar --exclude .git --ignore-failed-read -C $SRC -cf - . | tar --ignore-failed-read -C $DEST -xf -

    pushd .
    cd $DEST
    svn st > /tmp/1 && iconv -f GBK -t UTF-8 /tmp/1 > /tmp/2 && cat /tmp/2 | grep -a '^!' | awk '{print $2}' | sed 's/\\/\//g' | xargs svn delete --force
    svn add . --force
    svn commit . -m "${MSG}"
    popd

done

git --git-dir=cache/.git --work-tree=cache checkout master
```