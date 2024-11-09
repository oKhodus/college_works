# Int = ( [сумма по всем i f(a+h*i)] + f(a)/2 +f(b)/2 ) * h,

def integral(f, start, end, n):
    h = (end - start) / n
    integral = 0.5 * (f(start) + f(end)) 
    # формула

    for i in range(1, n):
        x_i = start + i * h
        integral += f(x_i)

    integral *= h
    return integral

def example_function(x):
    return x ** 2  # функция x^2

def main():

    start = 0
    end = 1
    n = 10

    print(f"Приближенное значение интеграла: ~ {integral(example_function, start, end, n):.2f}")

main()