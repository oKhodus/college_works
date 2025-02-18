def nod(a, b):
    if b == 0:
        return a
    else:
        return nod(b, a % b)

def nok(a, b):
    return a * b // nod(a, b)

a = int(input("Введите первое число (a) для нахождения НОД и НОК: "))
b = int(input("Введите второе число (b) для нахождения НОД и НОК: "))

print(f"НОД: {nod(a, b)}")
print(f"НОК: {nok(a, b)}")
