def koren(n):
    if n <= 0:
        return False
    while n % 3 == 0:
        n //= 3
    return n == 1

number = int(input("Введите положительное целое число: "))
if koren(number):
    print(f"{number} является степенью тройки.")
else:
    print(f"{number} не является степенью тройки.")