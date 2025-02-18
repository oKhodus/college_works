def find_primes(lim):
    nums = list(range(2, lim + 1))
    for i in nums:
        # минус числа - которые делятся на i (кроме самого i)
        for x in nums:
            if x != i and x % i == 0:
                nums.remove(x)  # минус число - если оно делится на i
    return nums

upper_lim = int(input("Введите верхнюю границу диапазона: "))
prime_nums = find_primes(upper_lim)
print(f"Простые числа до {upper_lim}: {prime_nums}")