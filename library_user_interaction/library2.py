


class BaseMeta(type):
  def __new__(cls, name, bases, body):
    print(cls, name, bases, body)
    if not 'bar' in body:
      raise TypeError("bad user class")
    return super().__new__(cls, name, bases, body)   


class Base(metaclass=BaseMeta):
  def foo(self):
    return self.bar() 


