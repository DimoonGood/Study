#В исходном текстовом файле (hotline.txt) после фразы «Горячая линия» добавить 
#фразу «Министерства образования Ростовской области», посчитать количество 
#произведённых добавлений. Сколько номеров телефонов заканчивается на «03», 
#«50». Вывести номера телефонов горячих линий, связанных с ЕГЭ/ГИА. 

import re


with open('hotline.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()


new_lines = []
add_count = 0
for line in lines:
    if "Горячая линия" in line:
        line = re.sub(r'(Горячая линия)', r'\1 Министерства образования Ростовской области', line, count=1)
        add_count += 1
    new_lines.append(line)


with open('hotline_modified.txt', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)


full_text = ''.join(lines)
phone_numbers = re.findall(r'\+?\d[\d\s\-()]{5,}\d', full_text)


ends_with_03 = [num for num in phone_numbers if re.search(r'03\b', num)]
ends_with_50 = [num for num in phone_numbers if re.search(r'50\b', num)]


ege_gia_numbers = []
for line in lines:
    if re.search(r'ЕГЭ|ГИА', line, re.IGNORECASE):
        found_numbers = re.findall(r'\+?\d[\d\s\-()]{5,}\d', line)
        ege_gia_numbers.extend(found_numbers)


print(f'Количество вставок "Министерства образования Ростовской области": {add_count}')
print(f'Номеров телефонов, оканчивающихся на 03: {len(ends_with_03)}')
print(f'Номеров телефонов, оканчивающихся на 50: {len(ends_with_50)}')
print('\nНомера телефонов горячих линий, связанных с ЕГЭ/ГИА:')
for number in ege_gia_numbers:
    print(number)
