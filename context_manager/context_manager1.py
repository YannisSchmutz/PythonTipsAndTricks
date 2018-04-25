
class Context(object):
    def __init__(self, name):
        self.name = name
        print("__init__", self.name)
        pass
    
    def __enter__(self):
        print("__enter__", self.name)
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("__exit__", self.name)

c1 = Context("C1")  # does just __init__

with Context("C2") as c2:  # does __init__
    # does __enter__
    pass
# does __exit__
