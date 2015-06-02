__author__ = 'estma_000'

import random


def fermat(n):
    for i in range(1, 6):
        a = random.randint(1, n-1)
        temp1 = a**(n-1) % n
        temp2 = 1 % n
        if temp1 != temp2:
            return False
    return True




