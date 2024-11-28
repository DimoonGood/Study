#2.	Дано целое число N (>0). Если оно является степенью числа 3, то вывести TRUE, если не является — вывести FALSE.
try:
    def koren(n):
        if n <= 0:
            return False
        while n % 3 == 0:
            n //= 3
        return n == 1

    number = int(input("Введите положительное целое число: "))
    if koren(number):
        print("TRUE")
    else:
        print("FALSE")
except:
    print("Ошибка!")