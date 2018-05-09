import contextlib
import os
import sys

@contextlib.contextmanager
def shut_stdout():
    sys.stdout = open(os.devnull, 'w')
    yield
    sys.stdout = sys.__stdout__

with shut_stdout():
    # do something 
    pass
