#2.	Описать функцию Power1(A, B) вещественного типа, находящую величину AB по формуле AB = exp(B*ln(A)) (параметры A и B — вещественные). В случае нулевого или отрицательного параметра A функция возвращает 0. С помощью этой функции найти степени AP, BP, CP, если даны числа P, A, B, C.
import math

def Power1(A, B):
    if A <= 0:
        return 0
    return math.exp(B * math.log(A))

try:
    P = float(input("Введите значение P: "))
    A = float(input("Введите значение A: "))
    B = float(input("Введите значение B: "))
    C = float(input("Введите значение C: "))

    AP = Power1(A, P)
    BP = Power1(B, P)
    CP = Power1(C, P)

    print(f"A^P = {AP}")
    print(f"B^P = {BP}")
    print(f"C^P = {CP}")

except ValueError:
    print("Ошибка: Введите корректные вещественные числа.")