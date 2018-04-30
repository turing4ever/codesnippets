# place super_test.py code here


# place keyword_test.py code here
def force(*, mass, acceleration):
    return mass*acceleration


def quad(*, a, b, c):
    sqrt = (b**2 - 4*a*c)**0.5
    x1 = (-b + sqrt)/(2*a)
    x2 = (-b - sqrt)/(2*a)
    return x1, x2
