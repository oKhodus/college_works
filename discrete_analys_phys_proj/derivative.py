# formules:

# для внутренней точки 
# 1. y′(x0​) = y(0​+1)−y(0​−1)​ / 2 / h

# для начальной точки (x0 = 0)
# 3. y′(x0​) = (-y(0​+2) + 4y(0 + 1) - 3y(0​)) / 2 / h​

# для конечной точки (x0 = N-1)
# 3. y′(x0​) = (y(0​-2) - 4y(0 - 1) + 3y(0​)) / 2 / h​

def calc_derevative(y, step):
    n = len(y)
    derivatives = []
    # step это h в формуле

    # начальная точка
    derivatives.append((-y[2] + 4 * y[1] - 3 * y[0]) / (2 / step))

    # Для любой внутренней точки (x0, y0)
    # (x0 = N-1)
    for point in range(1, n - 1):
        derivatives.append((y[point + 1] - y[point - 1]) / (2 / step))
    
    # Для конечной точки (x0 = N-1)
    derivatives.append((y[-2] - 4 * y[-1] + 3 * y[-3]) / (2 / step))
    
    return derivatives

def calc_derevative2(first, step):
    n = len(first)
    sec_derev = []

    for point in range(1, n - 1):
        sec_derev.append(first[point + 1] - first[point - 1] / (2 / step))

    return sec_derev


def main():
    y = [1, 2, 3, 4, 5, 6]
    step = 1
    
    first = calc_derevative(y, step)
    second = calc_derevative2(first, step)

    print(f"Первая производная: {first}")
    print(f"Вторая производная: {second}")

main()

