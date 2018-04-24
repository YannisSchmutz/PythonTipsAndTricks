#!/usr/bin/python3

from pprint import pprint as pp
from inspect import getsource


def add(x, y):
    return x + y


if __name__ == '__main__':
    pp(dir(add.__code__))
    print("Function name: ", add.__code__.co_name)
    print("Variable names: ", add.__code__.co_varnames)
    
    print("Source code of function:")
    print(getsource(add))
