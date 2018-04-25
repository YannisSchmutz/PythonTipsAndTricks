

class Temptable(object):
    def __init__(self, name):
        self.name = name
        print("__init__", self.name)
        pass
    
    def __enter__(self):
        print("__enter__", self.name)
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("__exit__", self.name)
        
t1 = Temptable("T1")

with Temptable("T2") as t2:
    pass
