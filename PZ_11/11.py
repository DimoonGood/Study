# Вариант 21: 
# 1) создать два текстовых файла с числами (отрицательные и положительные), обработать, записать в новый файл
# 2) прочитать text18-21.txt, посчитать знаки препинания, сохранить строки в обратном порядке
import string

print('=== ЗАДАНИЕ 1: Обработка чисел ===')


with open('negatives.txt', 'w') as f:
    f.write('-5 -10 -3 -8 -15')


with open('positives.txt', 'w') as f:
    f.write('4 7 12 1 9')


with open('negatives.txt', 'r') as f:
    nums1 = list(map(int, f.read().split()))
negatives = [n for n in nums1 if n < 0]
count_neg = len(negatives)
avg_neg = sum(negatives) / count_neg if count_neg else 0


with open('positives.txt', 'r') as f:
    nums2 = list(map(int, f.read().split()))
positives = [n for n in nums2 if n > 0]
count_pos = len(positives)
sum_pos = sum(positives)


with open('result.txt', 'w', encoding='utf-8') as f:
    f.write(f'Содержимое первого файла:\n{nums1}\n')
    f.write(f'Отрицательные элементы: {negatives}\n')
    f.write(f'Количество отрицательных элементов: {count_neg}\n')
    f.write(f'Среднее арифметическое: {avg_neg:.2f}\n\n')
    f.write(f'Содержимое второго файла:\n{nums2}\n')
    f.write(f'Положительные элементы: {positives}\n')
    f.write(f'Количество положительных элементов: {count_pos}\n')
    f.write(f'Сумма положительных элементов: {sum_pos}\n')

print('Результат записан в result.txt\n')


print('=== ЗАДАНИЕ 2: Работа с текстом ===')


with open('text18-21.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    text = ''.join(lines)
    punctuation_count = sum(1 for c in text if c in string.punctuation)
    print('Содержимое файла text18-21.txt:\n')
    print(text)
    print(f'Количество знаков препинания: {punctuation_count}')


with open('reversed_poem.txt', 'w', encoding='utf-8') as f:
    f.writelines(reversed(lines))

print('Обратный порядок строк сохранён в reversed_poem.txt')
