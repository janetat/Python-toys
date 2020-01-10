"""
    1. 使用 Manager 和 Queue 就可以实现简单的分布式的不同服务器的不同进程间的通信（C/S 模式）。
    2. https://docs.python.org/3.8/library/multiprocessing.html#managers
"""
from multiprocessing.managers import BaseManager


host = '127.0.0.1'
port = 9030
authkey = 'secret'


class RemoteManager(BaseManager):
    pass


def main():
    RemoteManager.register('get_list')
    mgr = RemoteManager(address=(host, port), authkey=authkey.encode('utf-8'))
    mgr.connect()

    l = mgr.get_list()
    print(l)
    l.append(1)
    print(mgr.get_list())

main()