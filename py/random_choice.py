# secrets.choice() can pick one element from a list(iterable)
import string
import secrets
import random

alphabet = string.ascii_letters + string.digits
print(''.join([secrets.choice(alphabet) for _ in range(10)]))
print(''.join([random.choice(alphabet) for _ in range(10)]))
