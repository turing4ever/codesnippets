import random
from tenacity import retry
from tenacity import stop

@retry(stop=stop.stop_after_attempt(7))
def do_something_unreliable():
    r = random.randint(1, 100)
    if  r > 1:
        raise IOError("Broken sauce, everything is hosed!!!111one")
    else:
        return "Awesome sauce!"

print(do_something_unreliable())
