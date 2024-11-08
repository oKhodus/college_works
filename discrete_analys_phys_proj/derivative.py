# formules:

# для внутренней точки 
# 1. y′(x0​) = y(0​+1)−y(0​−1)​ / 2 / h

# для начальной точки (x0 = 0)
# 3. y′(x0​) = (-y(0​+2) + 4y(0 + 1) - 3y(0​)) / 2 / h​

# для конечной точки (x0 = N-1)
# 3. y′(x0​) = (y(0​-2) - 4y(0 - 1) + 3y(0​)) / 2 / h​

def derivative(y, step):
    n = len(y)
    result = []
    
    for i in range(n):
        if i == 0:
            # для начальной точки (x0 = 0)
            value = (-y[i+2] + 4 * y[i+1] - 3 * y[i]) / (2 * step)
        elif i == n - 1:
            # для конечной точки (x0 = N-1)
            value = (y[i-2] - 4 * y[i-1] + 3 * y[i]) / (2 * step)
        else:
            # для внутренней точки 
            value = (y[i+1] - y[i-1]) / (2 * step)
        
        result.append(value)
    
    return result

def main():
    x = [0, 1, 2, 3, 4, 5]
    first = derivative(x, step=1)
    print(f" Первая производная: {first}\
          \n Вторая производная: {derivative(first, step=1)}")


main()