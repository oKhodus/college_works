# t=v1​d1​​+v2​d2​​
# formule

# t - total time
#  d1 d2 = distance in first area and second
# v1 v2 speed of light in first and secnd area

# v1​≈3×108 м/с speed of light


# abc = path
# d1 = ac
# d2 = cb

# mirror = mn

# a = b is true


# L = total distnace in x


import math


def calc_time(x, a, b, L, v):
    AC = math.sqrt(a**2 + x**2)
    
    CB_squared = b**2 - (L - x)**2
    if CB_squared < 0:
        return float('inf')

    CB = math.sqrt(CB_squared)
    return (AC + CB) / v

def findMin_on_line(a, b, L, v, step= "1.0"):
    min_time = float("inf")
    x = 0
    optimal_x = 0
    while x <= L:
        current_time = calc_time(x, a, b, L, v)
        if current_time < min_time:
            min_time = current_time
            optimal_x = x
        x += step

    return optimal_x, min_time




def main():
    v = 3 * math.pow(10, 8)

    a = float(input("Enter a height a of point A: "))
    b = float(input("Enter a height b of point B: "))
    L = float(input("Enter distance L btw A and B: "))

    optimal_x, min_time = findMin_on_line(a, b, L, v, step=0.01)
    print(f"Min point of mirror C: x = {optimal_x}")
    print(f"Min time: t = {min_time} sec")


if __name__ == "__main__":
    main()