import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def forced_oscillator(t, y, m, k, r, F, w):
    x, vx = y  # x - положение, vx - скорость
    dxdt = vx
    dvxdt = (-k * x - r * vx + F * np.cos(w * t)) / m
    return [dxdt, dvxdt]

m = 1.0  # масса (кг)
k = 10.0  # жесткость пружины (Н/м)
r = 0.5  # коэффициент демпфирования (кг/с)
F = 1.0  # амплитуда вынуждающей силы (Н)
w = 2.0  # частота вынуждающей силы (рад/с)
x0 = 1.0  # начальное положение (м)
v0 = 0.0  # начальная скорость (м/с)

t_start = 0
t_end = 50
t_points = 1000
t_eval = np.linspace(t_start, t_end, t_points)

sol = solve_ivp(
    forced_oscillator,
    [t_start, t_end],
    [x0, v0],
    args=(m, k, r, F, w),
    t_eval=t_eval
)

x = sol.y[0]  # положение
vx = sol.y[1]  # скорость

plt.figure(figsize=(10, 6))
plt.plot(x, vx, label="Фазовая кривая (x, v)")
plt.title("Фазовая кривая вынужденных колебаний")
plt.xlabel("x (положение, м)")
plt.ylabel("vx (скорость, м/с)")
plt.grid()
plt.legend()
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(t_eval, x, label="x(t)")
plt.title("График положения x(t)")
plt.xlabel("t (время, с)")
plt.ylabel("x (положение, м)")
plt.grid()
plt.legend()
plt.show()

# import math as m
# import matplotlib.pyplot as plt

# def main():
#     mass = 0.2  # Масса тела
#     k = 10      # жксткость пружины
#     r = 0.2     # (Damping) коэффициент затухания
#     w = 5       # угловая частота внешней силы
#     dt = 0.005  # шаг времени
#     t = 0       # нач. время
#     x = 0       # нач. позиция
#     speed = 0   # нач. скорость

#     time = []
#     acceleration = [] # ускорение
#     speed_list = []
#     position = []

#     while t < 20:
#         t += dt
#         # по второму закону ньютона
#         f = 2 * m.sin(w * t)  # внешняя сила - как син. функция
#         a = (f - k * x - r * speed) / mass
#         speed += a * dt
#         x += speed * dt

#         time.append(t)
#         acceleration.append(a)
#         speed_list.append(speed)
#         position.append(x)

#     plt.figure(figsize=(12, 8))

#     plt.subplot(3, 1, 1)
#     plt.plot(time, acceleration, label="Acceleration (a)", color="blue")
#     plt.ylabel("Acceleration (m/s²)")
#     plt.grid()
#     plt.legend()

#     plt.subplot(3, 1, 2)
#     plt.plot(time, speed_list, label="Speed (s)", color="green")
#     plt.ylabel("Velocity (m/s)")
#     plt.grid()
#     plt.legend()

#     plt.subplot(3, 1, 3)
#     plt.plot(time, position, label="Position (x)", color="red")
#     plt.xlabel("Time (s)")
#     plt.ylabel("Position (m)")
#     plt.grid()
#     plt.legend()

#     plt.tight_layout()
#     plt.show()

# main()
