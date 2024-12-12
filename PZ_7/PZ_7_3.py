# Задание 3: Нахождение ближайшей точки
# Дано множество А из N точек на плоскости и точка В (точки заданы своими координатами х, у).
# Найти точку из множества А, наиболее близкую к точке В. Расстояние R между точками с координатами (х1, у1) и (x2, У2) вычисляется по формуле:
# R = √(x2 - x1)²+ (y2 - y1)².

# Ввод данных от пользователя
import math

try:
    N = int(input("Введите количество точек (N): "))
    points = []
    for i in range(N):
        while True:
            try:
                x = float(input(f"Введите координату x для точки {i+1}: "))
                y = float(input(f"Введите координату y для точки {i+1}: "))
                points.append((x, y))
                break
            except ValueError:
                print("Некорректный ввод. Попробуйте снова.")

    Bx = float(input("Введите координату x для точки B: "))
    By = float(input("Введите координату y для точки B: "))

    # Находим ближайшую точку
    min_distance = float('inf')  # Инициализируем минимальное расстояние бесконечностью
    closest_point = None
    for x, y in points:
        distance = math.sqrt((Bx - x)**2 + (By - y)**2)
        if distance < min_distance:
            min_distance = distance
            closest_point = (x, y)

    print(f"Ближайшая точка к B({Bx}, {By}): {closest_point}")

except ValueError as e:
    print("Ошибка:", e)
except Exception as e:
    print("Произошла непредвиденная ошибка:", e)