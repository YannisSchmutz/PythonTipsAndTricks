#!/usr/bin/python3


class BaseMeta(type):
    def __new__(cls, name, bases, body):
        print("Cls: ", cls)
        print("Name: ", name)
        print("Bases: ", bases)
        print("Body: ", body)
        print("")
        if name != "Base":
            if 'bar' not in body:
                raise TypeError("bad user class")
        return super().__new__(cls, name, bases, body)


class Base(metaclass=BaseMeta):
    def foo(self):
        return self.bar()
