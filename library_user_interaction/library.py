
class Base(object):
  def foo(self):
    return "foo"


import builtins
obc = __build_class__

#def my_bc(*a, **kw):
def my_bc(fun, name, base=None, **kw):
  print("my buildclass->", fun, name, base, kw)
  if base is Base:
    print('check if bar method is defined')
  #return obc(*a, **kw)
  if base is not None:
    return obc(fun, name, base, **kw)
  return obc(fun, name, **kw)

builtins.__build_class__ = my_bc
