from math import pow, sqrt

def solve_quadratic(a, b, c):

    discriminant = pow(b, 2) - 4*a*c

    if discriminant > 0:

        x1 = (-b + sqrt(discriminant)) / (2*a)
        x2 = (-b - sqrt(discriminant)) / (2*a)

        return x1, x2

    elif discriminant == 0:
        return -b / (2*a)
    else:   
        return None
