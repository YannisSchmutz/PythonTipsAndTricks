"""
Similar to compute1.Compute()

"""

from time import sleep


def compute():
    """
    Returns a generator class
    :return:
    """
    for i in range(10):
        sleep(.5)
        yield i
       
print(type(compute()))
for val in compute():
    print(val)
