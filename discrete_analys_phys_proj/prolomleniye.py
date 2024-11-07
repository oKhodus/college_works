import math

def check_snell_law(n1, n2, theta1, theta2):
    theta1_rad = math.radians(theta1)
    theta2_rad = math.radians(theta2)
    
    # Проверяем, выполняется ли закон преломления
    # Формула: n1​⋅sin(θ1​)=n2​⋅sin(θ2​)
    left_side = n1 * math.sin(theta1_rad)
    right_side = n2 * math.sin(theta2_rad)
    l_round = round(left_side, 2)
    r_round = round(right_side, 2)
    
    if l_round == r_round:
        return True
    else:
        return False

# Пример
n1 = 1.0
n2 = 1.5
theta1 = 30
theta2 = 19.47

result = check_snell_law(n1, n2, theta1, theta2)
print(result)
