#Из заданной строки отобразить только цифры. Использовать библиотеку string.
import string

текст = "TheGreatPyramidofKhufuatGizawasbuiltabout 2700 BC, 755 feet (230metres) longand 481 feet (147 metres) high."


цифры = ""

for символ in текст:
    if символ in string.digits:
        цифры += символ

print("Цифры из строки:", цифры)