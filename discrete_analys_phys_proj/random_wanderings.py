import numpy as np, matplotlib.pyplot as plt


# N от 10 до 500
N_range = range(10, 501, 10)
# 5000 испытаний
N_trial = 5000

avg_square = []

for n in N_range:
    empty = []
    for _ in range(N_trial):
        steps = np.random.choice([-1, 1], size = n)
        x_n = np.sum(steps)
        empty.append(x_n ** 2)
        # S2 =< (xN )**2 > от N
    avg_square.append(np.mean(empty))
    # .mean - calc avg values 

plt.figure(figsize= (8, 6))
plt.plot(N_range, avg_square, label="S^2(N)", marker= "o")
plt.xlabel("Val of steps (N)")
plt.ylabel("Avg square s^2")
plt.title("Зависимость среднего квадрата смещения от числа шагов")
plt.grid()
plt.legend()
plt.show()

