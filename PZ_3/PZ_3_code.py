# ПЗ 3
#Вариант 21.
#1. Дано трехзначное число. Проверить истинность высказывания: «Все цифры данного
#числа различны».
#2. Даны два числа. Вывести порядковый номер меньшего из них.
import time

def print_slow(text): # функция позволяющая выводить каждый символ в тексте постепенно
    for i in text:
        time.sleep(0.1)
        print(i, end='')


def start():
    print_slow("Приветствую. Автор: Дмитрий\n")
    choise()


def choise():
    print_slow("Выберите часть задания (1,2): \n")
    choise_input = int(input())
    try:
        if choise_input == 1:
            zad_1()
        elif choise_input == 2:
            zad_2()
        else:
            print_slow("Недопустимое значение!")
            choise()
    except ValueError:
        print_slow("Недопустимое значение!\n")
        choise()


def zad_1():
    number_input = input("Введите число!\n")
    number_str = str(number_input)
    try:
        if len(number_str) == 1:
            print("Все цифры данного числа равны!")
            choise()
        else:
            for i in range(1, len(number_str)):
                if number_str[i] == number_str[i-1]: # Сравнение с предыдущей цифрой
                    print("Все цифры данного числа равны!")
                    choise()
        print("Все цифры данного числа различны!")
        choise()
    except:
        print("Недопустимое значение!")
        choise()


def zad_2():
    try:
        number_1 = int(input("Введите первое число: "))
        number_2 = int(input("Введите второе число: "))
        if number_1 < number_2:
            print("Порядковый номер меньшего: 0")
            choise()
        elif number_1 > number_2:
            print("Порядковый номер меньшего: 1")
            choise()
    except:
        print("Недопустимое число!\n")
        choise()



start()