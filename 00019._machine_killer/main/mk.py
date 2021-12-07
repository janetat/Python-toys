import itertools
import os

from multiprocessing import Pool, Process


def attack():
    naturals = itertools.count(1)
    # _lis = []
    for n in naturals:
        # Dangerous! CPU killer!
        print(n, os.getpid())
        # Dangerous! Memory killer!
        # _lis.append(n)


def attack_pools():
    p = Pool(10)
    for _ in range(10):
        p.apply_async(attack)

    p.close()
    p.join()


def attck_multiproces():
    for num in range(7):
        Process(target=attack).start()
