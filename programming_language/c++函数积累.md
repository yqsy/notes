---
title: c++函数积累
date: 2017-11-08 22:58:21
categories: [编程语言]
---

<!-- TOC -->

- [1. 其他](#1-其他)
- [2. split](#2-split)
    - [2.1. 字符分割(c++11)](#21-字符分割c11)
    - [2.2. 字符分割(c++98)](#22-字符分割c98)
    - [2.3. 字符串分割(c++11)](#23-字符串分割c11)
- [3. 指定位置寻找有分割符号的字符串](#3-指定位置寻找有分割符号的字符串)
- [4. Trim(中文有问题把?)](#4-trim中文有问题把)
- [5. 替换一个字符串](#5-替换一个字符串)
- [6. 替换所有字符串](#6-替换所有字符串)
- [7. 判断double是否相等](#7-判断double是否相等)

<!-- /TOC -->


<a id="markdown-1-其他" name="1-其他"></a>
# 1. 其他 

* http://www.gingerbill.org/article/defer-in-cpp.html (defer)

<a id="markdown-2-split" name="2-split"></a>
# 2. split

<a id="markdown-21-字符分割c11" name="21-字符分割c11"></a>
## 2.1. 字符分割(c++11)
```c++
std::vector<std::string> split(const std::string &str, char c) {
  std::vector<std::string> vec;
  std::string buffer("");
  for (const auto &i : str)
    if (i != c) {
      buffer += i;
    } else {
      vec.push_back(std::move(buffer));
      buffer = "";
    }
  if (buffer != "") {
    vec.push_back(std::move(buffer));
  }
  return vec;
}
```

<a id="markdown-22-字符分割c98" name="22-字符分割c98"></a>
## 2.2. 字符分割(c++98)
```c++
const std::vector<std::string> split(const std::string &str, char c) {
  std::vector<std::string> vec;
  std::string buf("");
  for (size_t i = 0; i < str.length(); ++i) {
    if (str[i] != c) {
      buf += str[i];
    } else {
      vec.push_back(buf);
      buf = "";
    }
  }
  if (buf != "") {
      vec.push_back(buf);
  }
  return vec;
}
```

<a id="markdown-23-字符串分割c11" name="23-字符串分割c11"></a>
## 2.3. 字符串分割(c++11)

```c++
std::vector<std::string> split(const std::string &str,
                               const std::string &separate) {

  std::vector<std::string> vec;

  const size_t len = separate.length();
  std::string::size_type begin = 0;
  std::string::size_type pos = 0;

  do {
    pos = str.find(separate, begin);
    if (pos != std::string::npos) {
      vec.push_back(str.substr(begin, pos - begin));
      begin = pos + len;
    }
  } while (pos != std::string::npos);

  std::string endstr = str.substr(begin);
  if (endstr != "")
    vec.push_back(std::move(endstr));

  return vec;
}
```

<a id="markdown-3-指定位置寻找有分割符号的字符串" name="3-指定位置寻找有分割符号的字符串"></a>
# 3. 指定位置寻找有分割符号的字符串
```c++
bool GetSplitStringPosition(const std::string &str, const std::string &separate,
                            int position, std::string *out) {
  if (out == NULL || position <= 0)
    return false;

  *out = "";

  const size_t len = separate.length();

  std::string::size_type begin = 0;
  std::string::size_type pos = 0;

  int current_position = 0;

  do {
    pos = str.find(separate, begin);
    if (pos != std::string::npos) {
      std::string sub_rtn = str.substr(begin, pos - begin);
      begin = pos + len;
      current_position++;

      if (current_position == position) {
        *out = sub_rtn;
        return true;
      }
    }
  } while (pos != std::string::npos);

  std::string endstr = str.substr(begin);
  if (endstr != "") {
    current_position++;

    if (current_position == position) {
      *out = endstr;
      return true;
    }
  }

  return false;
}
```

<a id="markdown-4-trim中文有问题把" name="4-trim中文有问题把"></a>
# 4. Trim(中文有问题把?)
* http://www.cplusplus.com/reference/cctype/isspace/
```c++
std::string trim(const std::string &str) {
  const char *white_space = " \t\n\v\f\r";
  size_t first = str.find_first_not_of(white_space);
  if (std::string::npos == first)
    return str;
  size_t last = str.find_last_not_of(white_space);
  return str.substr(first, (last - first + 1));
}
```

<a id="markdown-5-替换一个字符串" name="5-替换一个字符串"></a>
# 5. 替换一个字符串

```c++
bool replace(std::string *str, const std::string &from, const std::string &to) {
  size_t start_pos = str->find(from);
  if (start_pos == std::string::npos)
    return false;
  str->replace(start_pos, from.length(), to);
  return true;
}
```

<a id="markdown-6-替换所有字符串" name="6-替换所有字符串"></a>
# 6. 替换所有字符串

```c++
std::string ReplaceAll(std::string str, const std::string &from,
                       const std::string &to) {
  size_t start_pos = 0;
  while ((start_pos = str.find(from, start_pos)) != std::string::npos) {
    str.replace(start_pos, from.length(), to);
    start_pos += to.length();
  }
  return str;
}
```

<a id="markdown-7-判断double是否相等" name="7-判断double是否相等"></a>
# 7. 判断double是否相等

```c++
bool DoubleEquals(double a, double b, double epsilon /*= 0.000001*/) {
  return std::abs(a - b) < epsilon;
}
```
