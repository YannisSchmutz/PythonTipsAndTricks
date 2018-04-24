from time import sleep

class Api(object):
    """
    Needs to be called sequentially! Breaks otherwise
    
    Problem:
    User could always do something like Api().second() at first. -> Breaks
    """
    def first(self):
        # Needs to always run first, breaks otherwise
        print('first')
        
    def second(self):
        # Needs to always run second, breaks otherwise
        print('second')
        
    def last(self):
        # Needs to always run last, breaks otherwise
        print('last')


# SOLUTION
def api():
    print('first')
    yield
    print('second')
    yield
    print('last')


print('Going to call the api-method...')
for test in api():
    print('Getting back the control, process something...')
    sleep(3)
    print('Going to the next api-method...')
