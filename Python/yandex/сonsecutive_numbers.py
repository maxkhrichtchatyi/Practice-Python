"""
B. Последовательно идущие единицы

Ограничение времени: 1 секунда
Ограничение памяти: 64Mb
Ввод: стандартный ввод или input.txt
Вывод: стандартный вывод или output.txt

# Описание
Требуется найти в бинарном векторе самую длинную последовательность единиц и вывести её длину.

Желательно получить решение, работающее за линейное время и при этом проходящее по входному массиву
только один раз.

# Формат ввода
Первая строка входного файла содержит одно число n, n ≤ 10000. Каждая из следующих n строк содержит
ровно одно число — очередной элемент массива.

# Формат вывода
Выходной файл должен содержать единственное число — длину самой длинной последовательности единиц
во входном массиве.

# Пример
Ввод:
5
1
0
1
0
1

Вывод:
1
"""

import sys

max_of_ones, max_of_ones_tmp = 0, 0
tuple_of_numbers = ()

number_of_numbers = int(sys.stdin.readline().strip())

if number_of_numbers <= 10000:
    for _ in range(0, number_of_numbers):
        number = int(sys.stdin.readline().strip())
        if number <= 10000:
            tuple_of_numbers += (number,)

for number in tuple_of_numbers:
    if number == 1:
        max_of_ones_tmp += 1
    else:
        if max_of_ones_tmp > max_of_ones:
            max_of_ones = max_of_ones_tmp

        max_of_ones_tmp = 0
else:
    if max_of_ones_tmp > max_of_ones:
        max_of_ones = max_of_ones_tmp

print(max_of_ones)
