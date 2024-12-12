# Задание 2: Проверка на перестановку
# 2. Дан целочисленный список размера N. Если он является перестановкой, то есть содержит все числа от 1 до N, то вывести 0;
# в противном случае вывести номер первого недопустимого элемента.

# Ввод данных от пользователя
try:
    N = int(input("Введите размер (количество элементов) в списке: "))
    my_list = []
    for i in range(N):
        while True:
            try:
                element = int(input(f"Введите число {i+1}: "))
                my_list.append(element)
                break
            except ValueError:
                print("Некорректный ввод. Попробуйте снова.")

    # Проверка на перестановку
    seen = set()
    for i, num in enumerate(my_list):
        if not 1 <= num <= N or num in seen:
            print(f"Список не является перестановкой. Недопустимый элемент: {num} (номер {i+1})")
            break
        seen.add(num)
    else: # Выполняется, если цикл завершился без break
        print("Список является перестановкой. Вывод: 0")

except ValueError as e:
    print("Ошибка:", e)
except Exception as e:
    print("Произошла непредвиденная ошибка:", e)