from random import randint
from .algebra import solve_quadratic

def random_quadratic():
    a = randint(1, 10)
    b = randint(1, 10)
    c = randint(1, 10)
    return solve_quadratic(a, b, c)