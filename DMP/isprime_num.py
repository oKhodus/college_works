import math as m

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    lim = int(m.sqrt(n)) + 1
    # лимит до корня из n

    for i in range(3, lim, 2):
        if n % i == 0:
            return False
    return True

print(is_prime(int(input("Введите число: "))))

