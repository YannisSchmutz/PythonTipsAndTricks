#!/usr/bin/python3

from myLibrary import Base


class Test(Base):
    def bar(self):
        return 'bar'
    

if __name__ == '__main__':
    t = Test()
    print(t.foo())
