import math

def check_snell_law(n1, n2, theta1, theta2):
    theta1_rad = math.radians(theta1)
    theta2_rad = math.radians(theta2)
    
    # Проверка - выполняется ли закон преломления
    # Формула: n1​⋅sin(θ1​)=n2​⋅sin(θ2​)
    left_side = n1 * math.sin(theta1_rad)
    right_side = n2 * math.sin(theta2_rad)
    l_round = round(left_side, 2)
    r_round = round(right_side, 2)
    
    if l_round == r_round:
        return True
    else:
        return False

# T=v1​d1​​+v2​d2​​
def calc_time(A, B, C, c, n1, n2):
    d1 = math.sqrt((B[0] - A[0])**2 + (B[1] - A[1])**2)
    d2 = math.sqrt((C[0] - B[0])**2 + (C[1] - B[1])**2)
    v1 = c / n1
    v2 = c / n2
    
    t = (d1 / v1) + (d2 / v2)
    return d1, d2, t



# пусть
n1 = 1.0
n2 = 1.5
theta1 = 30
theta2 = 19.47
c = 3 * 10**8
A = (0, 10)
B = (10, -10)
C = (5, 0)

result = check_snell_law(n1, n2, theta1, theta2)
dist = calc_time(A, B, C, c, n1, n2)

print(f"Закон преломления выполняется: {result}")
print(f"Кратчайший по времени маршрут: {dist[2]:.10f} секунд")