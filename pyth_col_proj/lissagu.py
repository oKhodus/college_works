from matplotlib import pyplot as plt
import math

def calc_lissajous(A1, A2, n):
    t_num_points = 1000
    step = (100 * math.pi) / t_num_points

    x_values = []
    y_values = []

    t = 0

    for _ in range(t_num_points):
        x_values.append(A1 * math.cos(t))  # Используем cos для оси X
        y_values.append(A2 * math.sin(n * t))  # Используем sin для оси Y
        t += step

    plt.figure(figsize=(6, 6))
    plt.plot(x_values, y_values, color='green')
    plt.title(f"Lissajous Figure: A1 = {A1}, A2 = {A2}, n = {n}")
    plt.ylabel("Ось Y")
    plt.xlabel("Ось X")
    plt.grid(True)
    plt.show()

calc_lissajous(10, 10, 4/9)
