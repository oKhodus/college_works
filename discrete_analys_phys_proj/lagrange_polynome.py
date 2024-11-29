def lagrange_calc(points, t):
    
    res = 0 
    for point_i in range(len(points)):
        xi, yi = points[point_i]

        li =  1
        for point_j in range(len(points)):
            if point_i != point_j:
                xj, _ = points[point_j]
                li *= (t - xj) / (xi - xj)
                # по формуле
        res += yi * li

    return res

if __name__ == "__main__":
    points = [(1, 1), (2, 4), (3, 9)]  # Набор точек
    t = 2.5
    result = lagrange_calc(points, t)
    print(f"Значение полинома в точке t (t = {t}): {result}")
# points - (x, y)
# t - число (float или int) или значение полинома
