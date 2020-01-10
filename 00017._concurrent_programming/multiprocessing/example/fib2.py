"""
    OOP多进程计算fib。
"""

from multiprocessing.pool import Pool


class CalculateFib:
    
    @classmethod
    def fib(cls, n):
        if n <= 2:
            return 1
        return cls.fib(n-1) + cls.fib(n-2)

    def map_run(self):
        pool = Pool(2)
        print(pool.map(self.fib, [35] * 2))


cl = CalculateFib()
cl.map_run()
