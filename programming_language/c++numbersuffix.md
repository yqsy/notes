---
title: c++numbersuffix
date: 2018-10-15 01:58:21
categories: [编程语言]
---

<!-- TOC -->

- [1. 说明](#1-说明)

<!-- /TOC -->



<a id="markdown-1-说明" name="1-说明"></a>
# 1. 说明

* http://www.cplusplus.com/forum/general/48920/

--- 

* 1.0 => double (8)
* 1.0f => float (4)
* 1 => int (4)
* 1U => unsigned int  (4)
* 1L => long (8)
* 1UL => unsigned long (8)
* 1ULL => unsigned long long (8)
* 1LL -> long long (8)


```c++
#include <iostream>

int main() {
        std::cout << "double" << sizeof(double) << std::endl;
		std::cout << "float" << sizeof(float) << std::endl;
		std::cout << "int" << sizeof(int) << std::endl;
		std::cout << "unsigned int" << sizeof(unsigned int) << std::endl;
		std::cout << "long" << sizeof(long) << std::endl;
		std::cout << "unsigned long" << sizeof(unsigned long) << std::endl;
		std::cout << "unsigned long long" << sizeof(unsigned long long) << std::endl;
		std::cout << "long long" << sizeof(long long) << std::endl;
        
        return 0;
}       


```