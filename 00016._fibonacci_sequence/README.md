# 斐波那契数列
https://en.wikipedia.org/wiki/Fibonacci_number
https://zh.wikipedia.org/wiki/%E6%96%90%E6%B3%A2%E9%82%A3%E5%A5%91%E6%95%B0%E5%88%97

# Navigation:
[version 1 递归版本](./main/v1.py)
[version 2 生成器版本](./main/v2.py)
[version 3 递归版本，LRU缓存优化](./main/v3.py)

# ScreenShot
![version 1 递归版本](./screenshot/v1.png)
递归版本会比较慢，因为每个数都重新计算。
![version 2 生成器版本](./screenshot/v2.png)
生成器版本比较快，因为当前一个数基于前两个数计算出来。
![version 3 递归版本，LRU缓存优化](./screenshot/v3.png)