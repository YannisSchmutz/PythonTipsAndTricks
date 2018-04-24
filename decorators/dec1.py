#!/usr/bin/python3

from pprint import pprint as pp
from time import time


def delta_time(func):
    """
    Wraps delta-time around a function
    :param func:
    :return:
    """
    def f(x, y):
        before = time()
        ret = func(x, y)
        after = time()
        print("Delta-time: ", after - before)
        return ret
    return f


@delta_time
def add(x, y):
    return x + y
# add = delta_time(add) --> Does the same as the decorator


# @delta_time
def sub(x, y):
    return x - y
# sub = delta_time(sub) --> Does the same as the decorator

if __name__ == '__main__':
    
    print('add(10, 20)', add(10, 20))
    print('add(10, 20)', add('a', 'b'))
    print('add(10, 20)', sub(10, 20))

