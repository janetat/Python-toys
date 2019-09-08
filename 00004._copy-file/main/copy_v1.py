"""
    Description :
    1. 拷贝文件内容，利用缓冲区
"""

with open('temp1', 'rb') as fsrc:
    with open('temp2', 'wb') as fdst:
            while True:
                buf = fscr.read(1024)
                if not buf:
                    break
                fdst.write(buf)
