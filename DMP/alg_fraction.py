def main(a, b):
    res = []

    while b != 0:
        res.append(a // b)
        a, b = b, a % b
    return f"Компоненты цепной дроби: {res}"

print(main(int(input("Введите число (a): ")),
           int(input("Введите число (b): "))))