# place super_test.py code here

class Character:
    def speed(self): return 2
    def jump(self): return 2
    def power(self): return 2

class Mario(Character):
    def speed(self): return super().speed() + 2
    def jump(self): return super().jump() + 2
    def power(self): return super().power() + 2

class Luigi(Character):
    def speed(self): return super().speed() + 1 
    def jump(self): return super().jump() + 3 
    def power(self): return super().power() + 1 

class Toad(Character):
    def speed(self): return super().speed() + 3 
    def jump(self): return super().jump()
    def power(self): return super().power() + 3 

# place keyword_test.py code here
def force(*, mass, acceleration):
    return mass*acceleration


def quad(*, a, b, c):
    import cmath
    sqrt = cmath.sqrt(b**2 - 4*a*c)
    x1 = (-b + sqrt)/(2*a)
    x2 = (-b - sqrt)/(2*a)
    return x1, x2
