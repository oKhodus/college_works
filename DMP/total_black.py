import numpy as np
import matplotlib.pyplot as plt

f = np.arange(100, 20001, 100)  # частоты от 100 до 20000 с шагом 100
T_values = [500, 1000, 1500, 2000, 2500]  # температуры

# 1) Функция зависимости спектральной светимости
def planck_law(f, T):
    return f**3 / (np.exp(f / T) - 1)

plt.figure(figsize=(10, 6))

for T in T_values:
    r_values = planck_law(f, T)
    plt.plot(f, r_values, label=f'T = {T} K')

plt.xlabel('Частота (Hz)')
plt.ylabel('Спектральная светимость r(f, T)')
plt.title('Зависимость спектральной светимости от частоты при различных температурах')
plt.legend()
plt.grid(True)
plt.show()

# 2) Найти частоты fmax, при которых достигается максимальная светимость
def find_fmax(T):
    r_values = planck_law(f, T)
    f_max_index = np.argmax(r_values)  # индекс максимума
    return f[f_max_index]  # частота f_max

fmax_values = [find_fmax(T) for T in T_values]
for T, fmax in zip(T_values, fmax_values):
    print(f"f_max при T = {T} K: {fmax} Hz")

# закон смещения Вина
win_law = T_values[0] / fmax_values[0]  # Для первой температуры
for T, fmax in zip(T_values, fmax_values):
    print(f"Для T = {T} K, f_max = {fmax} Hz, \
           T / f_max = {T / fmax:.2f}, \
           ожидаемое значение {win_law:.2f}")
    
# 3) Проверить справедливость закона Стефана – Больцмана

def total_r(T):
    r_values = planck_law(f, T)
    return np.sum(r_values)

# суммарная энергия для каждой температуры
total_r_values = [total_r(T) for T in T_values]

# sum(energy) of T^4
T_fourth = np.array(T_values) ** 4
plt.figure(figsize=(8, 6))
plt.plot(T_fourth, total_r_values, 'o-', label="Суммарная энергия")
plt.xlabel('T^4')
plt.ylabel('Суммарная светимость')
plt.title('Зависимость суммарной светимости от T^4')
plt.grid(True)
plt.legend()
plt.show()
