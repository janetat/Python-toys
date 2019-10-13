# Navigation
- [Navigation](#navigation)
- [Introduction](#introduction)
- [Solution 1 reversed()](#solution-1-reversed)
- [Solution 2 range(len(a)-1, -1, -1)](#solution-2-rangelena-1--1--1)
- [Solution 3 range(len(a)) + ~操作符](#solution-3-rangelena--%e6%93%8d%e4%bd%9c%e7%ac%a6)
- [Solution 4 slice](#solution-4-slice)
- [Solution 5 length - i - 1](#solution-5-length---i---1)


# Introduction
implement reversed()
实现反向遍历序列


# Solution 1 reversed()
```python
a = [1, 2, 3, 4]
for i in reversed(a):
    print(i)
```

# Solution 2 range(len(a)-1, -1, -1)
```python
a = [1, 2, 3, 4]
for i in range(len(a)-1, -1, -1):
    print(a[i])
```

# Solution 3 range(len(a)) + ~操作符
> ~按位取反运算符：对数据的每个二进制位取反,即把1变为0,把0变为1 。~x 类似于 -x-1
```python
a = [1, 2, 3, 4]
for i in range(len(a)):
    print(a[~i])
```

# Solution 4 slice
```python
a = [1, 2, 3, 4]
for i in a[::-1]:
    print(i)
```

# Solution 5 length - i - 1
```python
a = [1, 2, 3, 4]

seq_length = len(a)
for i in range(seq_length):
    print(a[seq_length-i-1])
```