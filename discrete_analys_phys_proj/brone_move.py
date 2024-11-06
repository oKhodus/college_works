import random as r
import matplotlib.pyplot as plt
import numpy as np


x, y = 0, 0
t = 0
dt = 0.05  # интервал времени
trajectory_x = [x]
trajectory_y = [y]

while t < 20:
    t += dt  # увеличивание времени
    angle = r.uniform(0, 2 * np.pi)  # случайный угол от 0 до 2π
    L = r.random()  # случайное смещение

    #  новые координаты
    x += L * np.cos(angle)
    y += L * np.sin(angle)
    
    trajectory_x.append(x)
    trajectory_y.append(y)

plt.plot(trajectory_x, trajectory_y, marker='o', linestyle='-', markersize=3)
plt.title("Броуновское движение частицы")
plt.xlabel("Координата X")
plt.ylabel("Координата Y")
plt.grid(True)
plt.show()
