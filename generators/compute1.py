"""

Just the fundamental principe.

"""

from time import sleep


# Bad example
def compute():
    """
    We would have to wait for the whole list, even though we might just need the first few element of it.
    - takes a lot of time (for the first element being returned)
    - needs much more memory than using an iterable class
    :return:
    """
    ret = []
    for i in range(0, 10):
        ret.append(i)
        sleep(.5)  # simulate some computing process, which takes its time
    return ret


# Goode example
class Compute(object):
    def __iter__(self):
        self.last = 0
        return self
    
    def __next__(self):
        ret = self.last
        self.last += 1
        if self.last > 10:
            raise StopIteration()
        sleep(.5)  # simulate some computing process, which takes its time
        return ret

if __name__ == '__main__':
    for val in Compute():
        print(val)
        # You are able to do something right now with your value