
# Int = [сумма по всем i (f(a+i*h+h/2))] * h,

    # h - длина кусочка по иксам, =(b-a)/n:
    # a - нижняя граница отрезка интегрирования:
    # i - номер кусочка (от 0 до (n-1) включительно).


def integral(f, start, end, n):
    h = (end - start) / n
    result = sum(f(start + i * h + h / 2) for i in range(n)) * h
    return result

def example_function(x):
    return x ** 2  # функция x^2

def main():

    start = 0
    end = 1
    n = 10

    print(f"Приближенное значение интеграла: ~ {integral(example_function, start, end, n)}")

main()
