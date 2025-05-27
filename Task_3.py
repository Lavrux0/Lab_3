import numpy as np

# Створюємо масив 25x25 з випадковими значеннями
arr_25x25 = np.random.rand(25, 25)

# Знаходимо мінімальне та максимальне значення
min_val = np.min(arr_25x25)
max_val = np.max(arr_25x25)

print(f"Мінімальне значення: {min_val:.2f}")
print(f"Максимальне значення: {max_val:.2f}")
# Створюємо матрицю 6x6 з послідовними значеннями під діагоналлю
matrix_6x6 = np.zeros((6, 6))
for i in range(6):
    for j in range(i):
        matrix_6x6[i, j] = i+1
print(matrix_6x6)
# Створюємо матриці для множення
matrix_5x3 = np.random.rand(5, 3)
matrix_3x2 = np.random.rand(3, 2)

# Виконуємо множення матриць
result = np.matmul(matrix_5x3, matrix_3x2)

print(result)
# Створюємо масив із 20 елементів
arr_20 = np.arange(20)

# Змінюємо знак елементів 10-16
arr_20[9:15] *= -1

print(arr_20)
# Створюємо два масиви
x = np.random.rand(10)
y = np.random.rand(10)

# Обчислюємо матрицю Коші
C = 1 / (x[:, None] - y[None, :])

# Обчислюємо визначник матриці
det_C = np.linalg.det(C)

print(f"Визначник матриці Коші: {det_C:.2f}")
def find_extrema(f, x_min, x_max, dx):
    x = np.arange(x_min, x_max, dx)
    y = f(x)
    max_idx = np.argmax(y)
    min_idx = np.argmin(y)
    return x[max_idx], x[min_idx]

# Приклад використання
def f(x):
    return x**3 - 2*x**2 + x

max_x, min_x = find_extrema(f, -2, 2, 0.01)
print(f"Максимум: {max_x:.2f}, Мінімум: {min_x:.2f}")
