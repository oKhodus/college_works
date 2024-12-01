import math as m

def ferma_meth(n):
    
    a = m.ceil(m.sqrt(n))
    
    while (b2 := a * a - n) != int(m.sqrt(b2)) ** 2:
        a += 1
    b = int(m.sqrt(b2))
    return a - b, a + b
    
n = int(input("Введите число: "))
factors = ferma_meth(n)
print(f"Множители числа {n}: {factors}")

