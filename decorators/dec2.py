"""
Parameter check

"""


class Paramcheck(object):
    def __init__(self, *args):
        self._args = [x for x in args]
        # print(self._args)
        
    def __call__(self, func):
        def f(*args):
            _args = [x for x in args]
            # print(args)
            for i in range(0, func.__code__.co_nlocals):
                if isinstance(_args[i], self._args[i]):
                    continue
                else:
                    raise AssertionError("{} is not type {}".format(_args[i], self._args[i]))
            
            ret = func(*args)
            return ret
        # print(func)
        # print(func.__code__.co_name)
        # print(func.__code__.co_varnames)
        return f
        

@Paramcheck(int, int)
def add_just_ints(x, y):
    return x + y


if __name__ == '__main__':
    print("add_just_ints(10, 20)", add_just_ints(10, 20))
    print("add_just_ints('a', 'b')", add_just_ints('a', 'b'))
