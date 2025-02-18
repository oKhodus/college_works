import math as m
import time as t

# вычисление экспоненты

def taylor_exp(x, precision=1e-8):
    term = 1  # Первое слагаемое (x^0 / 0!)
    res = term
    n = 1
    while abs(term) >= precision:
        term *= x / n
        res += term
        n += 1
    return res

step = m.pi / 100
x_values = [i * step for i in range(101)]

taylor_res_exp = []
math_res_exp = []

start_taylor = t.perf_counter()
for x in x_values:
    taylor_res_exp.append(taylor_exp(x))
end_taylor = t.perf_counter()
taylor_time_exp = end_taylor - start_taylor

start_math_exp = t.perf_counter()
for x in x_values:
    math_res_exp.append(m.exp(x))
end_math_exp = t.perf_counter()
math_time_exp = end_math_exp - start_math_exp

table_exp = [
    (x, taylor_exp_value, builtin_value)
    for x, taylor_exp_value, builtin_value in zip(x_values, taylor_res_exp, math_res_exp)
]

taylor_time_exp, math_time_exp, table_exp[:5]

print(f"\nВремя выполнения Тейлорова ряда: {taylor_time_exp:.8f} секунд")
print(f"Время выполнения встроенной функции math.exp: {math_time_exp:.8f} секунд")

print("\nТаблица результатов (x, Тейлорова экспонента, Встроенная экспонента):")
for x, taylor_exp_value, builtin_value in table_exp[:5]:
    print(f"x = {x:.2f}, Тейлор: {taylor_exp_value:.8f}, math.exp: {builtin_value:.8f}")

