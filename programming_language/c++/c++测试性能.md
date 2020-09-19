<!-- TOC -->

- [1. 说明](#1-说明)

<!-- /TOC -->



# 1. 说明


```bash
# 纳秒
auto start = std::chrono::high_resolution_clock::now();

auto finish = std::chrono::high_resolution_clock::now();

std::cout << (finish - start).count() << std::endl;
```
