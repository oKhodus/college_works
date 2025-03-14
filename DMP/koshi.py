from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
# import numpy as np

# правая часть уровнения
# y' = f(x, y)
def f(x, y):
    return x + y
# y' = x + y

# Решение задачи Коши модифицированным методом Эйлера.
def eiler_meth(func, x0, y0, h, n):
    x_vls = [x0]
    y_vls = [y0]

    for _ in range(n):
        x_prev, y_prev = x_vls[-1], y_vls[-1]
        y1_next = y_prev + h * func(x_prev, y_prev)

        x_next = x_prev + h
        y_next = y_prev + 0.5 * h * (func(x_prev, y_prev) + func(x_next, y1_next))

        x_vls.append(x_next)
        y_vls.append(y_next)

    return x_vls, y_vls

# нач. условия

x0 = 0
y0 = 1
h = 0.1
n = 10

x, y = eiler_meth(f, x0, y0, h, n)

formatted_data = [(f"{xi:.2f}", f"{yi:.2f}") for xi, yi in zip(x, y)]

fig, ax = plt.subplots(figsize=(10, 6))

ax.axis("tight")
ax.axis("off")

table = ax.table(
    cellText=formatted_data,
    colLabels=["x", "y"],
    cellLoc="center",
    loc="center",
    colColours=["lightblue", "lightgreen"],
)

table.auto_set_font_size(False)
table.set_fontsize(14)
table.auto_set_column_width(col=list(range(len(["x", "y"]))))

# Показ таблицы
plt.show()