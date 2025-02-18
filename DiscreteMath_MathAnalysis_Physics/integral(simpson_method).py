# ∫ab ​f(x)dx≈3h​(f(a)+4i=1,3,…∑n−1​f(xi​)+2i=2,4,…∑n−2​f(xi​)+f(b))

def simpsons_rule(func, start, end, n):
    if n % 2 != 0:
        raise ValueError("Количество разбиений (n) должно быть четным.")

    h = (end - start) / n

    # по формуле Симпсона
    integral = func(start) + func(end)

    for i in range(1, n):
        x = start + i * h
        if i % 2 == 0:
            integral += 2 * func(x)
        else:
            integral += 4 * func(x)

    integral *= h / 3
    return integral

def example_function(x):
    return x**2

def main():

    start = 0
    end = 1
    n = 10

    result = simpsons_rule(example_function, start, end, n)
    print(f"Приближенное значение интеграла: ~ {result:.2f}")

main()
