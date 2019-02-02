---
title: Code Format
date: 2017-11-19 15:20:00
categories: [coding]
---

<!-- TOC -->

- [1. C/C++/Java/JavaScript/Objective-C/Protobuf](#1-ccjavajavascriptobjective-cprotobuf)
- [2. python](#2-python)

<!-- /TOC -->

<a id="markdown-1-ccjavajavascriptobjective-cprotobuf" name="1-ccjavajavascriptobjective-cprotobuf"></a>
# 1. C/C++/Java/JavaScript/Objective-C/Protobuf

* https://clang.llvm.org/docs/ClangFormat.html
* https://stackoverflow.com/questions/28896909/how-to-call-clang-format-over-a-cpp-project-folder

```bash

# 创建模板
clang-format -style=llvm -dump-config > .clang-format

# 左大括号换行
BreakBeforeBraces: Allman

# 是否排序include
SortIncludes:    false

# 格式化并替换
find . -name '*.h' -type f -print0 | xargs -0 clang-format -i

```


<a id="markdown-2-python" name="2-python"></a>
# 2. python

暂时使用的是pycharm的自带的Code Format工具 + pylint 
