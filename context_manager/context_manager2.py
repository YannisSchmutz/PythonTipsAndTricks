
from contextlib import contextmanager
from pprint import pprint as pp

pp(dir(contextmanager))


@contextmanager
def context():
    print(1)
    yield
    print(2)
    

with context() as c:
    print('a')

print('b')
