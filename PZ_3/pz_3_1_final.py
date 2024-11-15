# ПЗ 3 Вариант 21. 1. Дано трехзначное число. Проверить истинность высказывания: «Все цифры данного числа различны».
try:
    number = int(input("Введите 3-х значное число!\n"))
    if number < 100 or number > 999:
        print("Это не 3-х значное число!")
    else:
        first = number // 100
        second = (number % 100) // 10
        third = number % 10
        if first == second == third:
            print("Все цифры в данном числе равны!")
        else:
            print("Все цифры в данном числе различны!")
except:
    print("Ошибка!")