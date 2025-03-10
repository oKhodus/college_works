from math_operations import *

A = randint(1, 100)
B = randint(1, 100)

res1 = multiply(A, B)

print(f"First digit: {A}\nSecond digit: {B}\nResult for mult will be: {multiply(A, B)}")

res2 = random_sqrt_sum()

print(f"Result for sqrt will be: {round(random_sqrt_sum())}")

print(f"Total output: {round(add(res1, res2))}")
