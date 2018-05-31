import functools
 
 
def calltracker(func):
    @functools.wraps(func)
    def wrapper(*args):
        wrapper.called = True
        return func(*args)
    wrapper.called = False
    return wrapper
 
@calltracker
def doubler(number):
    return number * 2
 
if __name__ == '__main__':
    if not doubler.called:
        print("You haven't called this function yet")
        doubler(2)
 
    if doubler.called:
        print('doubler has been called!')
