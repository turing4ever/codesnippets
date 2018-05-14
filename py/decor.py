import time
from functools import wraps

def timeit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        res = func(*args, **kwargs)
        t2 = time.time()
        print(f'{func.__name__} took {t2-t1:.2f} seconds to run')
        return res 
    return wrapper

def show_args(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'{func.__name__} takes in {args}, {kwargs}')
        return func(*args, **kwargs)
    return wrapper

@timeit
@show_args
def generate_report(*months, **parameters):
    time.sleep(2)
    print('(actual function) Done, report links ...')


generate_report('Jan', 'Feb', 'March', a=1, b='color', c={'t':100})
