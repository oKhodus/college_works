import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

m = 1.0 
# масса кг
k = 10.0
# жесткость пружины, Н/м
r = 0.5
# вязкость Н * с/м

x0 = 1.0
# начальное смещение м
v0 = 0.0
# начальная скорость м/с

def calc(t, y):
    x, vx = y
    ax = -k/m * x - r/m * vx
    return [vx, ax]

# интервал времени от 0 до 10
t_span = (0, 10)
t_eval = np.linspace(t_span[0], t_span[1], 1000)

out = solve_ivp(calc, t_span, [x0, v0], t_eval = t_eval)

x = out.y[0]
vx = out.y[1]

plt.figure(figsize=(8, 6))
plt.plot(x, vx, label="Фазовая кривая")
plt.title("Фазовая кривая пружинного маятника")
plt.xlabel("x (м)")
plt.ylabel("v (м/с)")
plt.grid(True)
plt.legend()
plt.show()

