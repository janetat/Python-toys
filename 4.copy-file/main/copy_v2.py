"""
    Description :
    1. 部分拷贝文件内容，利用缓冲区
"""

with open('temp1', 'rb') as fsrc:
    with open('temp2', 'wb') as fdst:
            buf = fsrc.read(11)
            fdst.write(buf)#copyfile#
