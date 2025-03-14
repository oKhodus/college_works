def prime_factors(n):
    list_factors = []
    divisor = 2

    # до √n
    while divisor * divisor <= n:
        while n % divisor == 0:
            # делится без остатка
            list_factors.append(divisor)
            n //= divisor
        divisor += 1
    if n > 1:
        list_factors.append(n)
    return list_factors

num = int(input("Введите число: "))
res = prime_factors(num)
print(f"Простые множители числа {num}: {res}")

