# ПЗ 2
#Вариант 21. Дано трехзначное число. Вывести число, полученное при
#перестановке цифр десятков и единиц исходного числа (например, 123 перейдет в 132).
print("This program shuffles the number") # эта программа меняет цифры


def mixxing():
    have_letters = False # если букв нет в "числе" - переходит к циклу
    try:
        meaning = input("Please enter a three-digit number ")
        for char in meaning:
            if char.isalpha(): # если в "числе" есть буква - выполняет код
                have_letters = True
            else:
                have_letters = False

        if have_letters == True: # если есть буква в "числе":
            print("Only numbers! Please try again...")
            mixxing()
        else:
            if int(meaning) >= 100 and int(meaning) <= 999: # проверка на 3-х значное число по условию
                hundreds = (int(meaning)) // 100 # разбиение числа на отдельные переменные
                tens = ((int(meaning)) % 100) // 10
                units = (int(meaning)) % 10
                print("Original:", meaning)
                print("Mixing: " + str(hundreds) + str(units) + str(tens))
                print("(Thanks for using the program!)")
                mixxing()
            else:
                print("This number is not a three-digit number!")
                print("Please try again...")
                mixxing()
    except:
        print("Недопустимое значение!")
        mixxing()


mixxing()