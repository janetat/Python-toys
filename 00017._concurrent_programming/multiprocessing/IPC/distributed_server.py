"""
    1. 使用 Manager 和 Queue 就可以实现简单的分布式的不同服务器的不同进程间的通信（C/S 模式）。
    2. https://docs.python.org/3.8/library/multiprocessing.html#managers
"""
from multiprocessing.managers import BaseManager


host = '127.0.0.1'
port = 9030
authkey = 'secret'

shared_list = ['a', 'b', 'c']


class RemoteManager(BaseManager):
    pass


def get_list():
    return shared_list


def main():
    RemoteManager.register('get_list', callable=get_list)
    mgr = RemoteManager(address=(host, port), authkey=authkey.encode('utf-8'))
    server = mgr.get_server()
    server.serve_forever()


main()
