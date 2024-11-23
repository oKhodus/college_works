import numpy as np

n = 1000 # кол-во точек для случайной выборки

apprs = np.zeros(n)  # approximations

def f(x, y, z):
    return 1


# Функция создает рандомные точки для радиуса, угла альфа и бета
def random_points(a_x, b_x, a_y, b_y, a_z, b_z):
    r = np.random.uniform(a_x, b_x)
    angle_theta = np.random.uniform(a_y, b_y)
    angle_phi = np.random.uniform(a_z, b_z)
    return r, angle_theta, angle_phi


# Связь с декартовыми координатами:
# x = r * sin⁡θ * cos⁡ϕ, 
# y = r * sin⁡θ * sin⁡ϕ,
# z = r * cos⁡θ.

def spheric_points(r, angle_theta, angle_phi):
    x = r * np.sin(angle_theta) * np.cos(angle_phi)
    y = r * np.sin(angle_theta) * np.sin(angle_phi)
    z = r * np.cos(angle_theta)
    return x, y, z

for point in range(n):
    r, angle_theta, angle_phi = random_points(0, 5, 0, np.pi, 0, 2*np.pi)
    x, y, z = spheric_points(r, angle_theta, angle_phi)
    dV = r ** 2 * np.sin(angle_theta)
    apprs[point] = f(x, y, z) * dV

Monte_Carlo_Approximation=(np.sum(apprs)/n)*(5-0)*(np.pi-0)*(2*np.pi-0) 
print ("Объём сферы подсчитанный с помощью метода Монте-Карло =", Monte_Carlo_Approximation)






