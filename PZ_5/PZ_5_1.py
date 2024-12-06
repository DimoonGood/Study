#1.	Составить функцию, которая выполнит суммирования числового ряда.
def sum_range():
    try:
        start = int(input("Введите начало числового ряда: "))
        end = int(input("Введите конец числового ряда: "))
        if end < start:
            print("Числовой ряд считается слева - направо, а не наоборот")
            return
        result = 0
        for i in range(start, end + 1):
            result += i #Суммирование
        print(f"Результат: {result}")

    except ValueError:
        print("Ошибка")

sum_range()