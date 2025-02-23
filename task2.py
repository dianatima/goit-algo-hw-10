import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi

# Визначення функції та межі інтегрування
def f(x):
    return x ** 2

a = 0  # Нижня межа
b = 2  # Верхня межа

# Створення діапазону значень для x
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()


# Метод Монте-Карло
def monte_carlo_method(num_points):
    random_x = np.random.uniform(a, b, num_points)
    random_y = np.random.uniform(0, f(b), num_points)

    points_under_curve = sum(random_y <= f(random_x))
    area_ratio = points_under_curve / num_points
    total_area = (b - a) * f(b)
    integral_value = total_area * area_ratio

    return integral_value

# Обчислення інтеграла
result, error = spi.quad(f, a, b)
print("Інтеграл: ", result, error)

# Обчислення інтеграла методом Монте-Карло
number_of_points = [10, 100, 1000, 10000, 100000, 1000000]

for points in number_of_points:
    print(
        f"Кількість точок: {points} , інтеграл: {monte_carlo_method(points)}"
    )