"""
    Description:
    1. 基于shutil高级文件处理模块
    2. shutil其中两个函数的源码看本目录
"""

import shutil

with open('temp1', 'rb') as fsrc:
    with open('temp2', 'wb') as fdst:
        shutil.copyfileobj(fsrc, fdst)
