# Вариант 21 Задача 1: Дано целое положительное число. Вывести символы, изображающие цифры этого числа (в порядке справа налево).

def print_digits_reverse():
    while True:
        number = int(input("Введите целое положительное число: "))
        if number > 0:
            break  # Выходим из цикла, если ввод корректен
        else:
            print("Число должно быть положительным. Пожалуйста, повторите ввод.")

    number_str = str(number)  # Преобразуем число в строку
    for i in reversed(number_str):
        print(i, end=" ")
    print() # Переход на новую строку в конце

print_digits_reverse()