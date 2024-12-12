# Задание 1: Сумма элементов списка, исключая диапазон
# Дан список размера N и целые числа К и L (1 < K < L < N). Найти сумму всех элементов списка, кроме элементов с номерами от К до L включительно.

try:
    N = int(input("Введите размер списка: "))   # Ввод данных от пользователя
    K = int(input(f"Введите начало диапазона исключения (1 < X < {N}): "))
    L = int(input(f"Введите конец диапазона исключения ({K} < X < {N}): "))

    if not (1 < K < L < N):
        raise ValueError("Ошибка в проверке условия: (1 < K < L < N)")

    my_list = []
    for i in range(N):
        while True:
            try:
                element = int(input(f"Введите элемент {i+1}: "))
                my_list.append(element)
                break
            except ValueError:
                print("Некорректный ввод. Попробуйте снова.")

    # Вычисление суммы, исключая элементы из диапазона [K-1:L] (индексы начинаются с 0)
    sum_of_elements = sum(my_list[:K-1] + my_list[L:])
    print("Сумма элементов вне диапазона:", sum_of_elements)

except ValueError as e:
    print("Ошибка:", e)
except Exception as e:
    print("Произошла непредвиденная ошибка:", e)