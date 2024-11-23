def math_funct(x, n):
    if abs(x) >= 1 or n <= 0:
        return "Ошибка: |x| должно быть меньше 1, а n должно быть положительным."
    result = 0
    for i in range(1, n + 1):
        result += ((-1)**(i - 1)) * (x**i) / i
    return result

# Получение входных данных от пользователя
x = float(input("Введите значение x (|x| < 1): "))
n = int(input("Введите значение n (n > 0): "))

# Проверка условия |x| < 1
if abs(x) >= 1:
    print("Ошибка: |x| должно быть меньше 1.")
else:
    # Вычисление приближенного значения ln(1 + x)
    result = math_funct(x, n)
    print(f"Приближенное значение ln(1 + {x}): {result}")