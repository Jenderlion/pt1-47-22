"""
2. Найти самое длинное слово в введенном предложении. Учтите что в предложении есть знаки препинания.
Подсказки:
- my_string.split([chars]) возвращает список строк.
- len(list) - количество элементов в списке
"""


str_1 = (input('Исходная строка: '))
marks = r'!?.,()[]{}\/:;—'
str_2 = ''
best_word = ''
best_word_lenth = 0

for char in str_1:
    if char in marks:
        continue
    else:
        str_2 += char

list_s = str_2.split()
for small_str in list_s:
    if len(small_str) > best_word_lenth:
        best_word = small_str
        best_word_lenth = len(small_str)

print(f'Самое длинное слово - это "{best_word}" с количеством букв, равным {best_word_lenth}')