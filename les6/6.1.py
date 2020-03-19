from sys import getsizeof
from collections import Counter
import random

#  Функция подсчета выделения памяти на переменные ниже.
# Взяты 3 варианта решения ПЗ с 4 урока, извлечены из функции и упрощены
# (считаем только переменные, без затрат памяти на функцию).
# Первое решение (с 2 циклами), несмотря на квадратичную сложность, в памяти занимает меньше места под переменные.
# 2 и 3 реализация схожи по затратам памяти (использоание словаря)

def show(obj):
    global total
    total += getsizeof(obj)
    if hasattr(obj, '__iter__'):
        if hasattr(obj, 'items'):
            for key, value in obj.items():
                show(key)
                show(value)
        elif not isinstance(obj, str):
            for item in obj:
                show(item)


SIZE = 50
MIN_ITEM = 0
MAX_ITEM = 200
array = [random.randint(MIN_ITEM, MAX_ITEM) for i in range(SIZE)]

top_num = 0
top_count = 0
count = 0
for i in array:
    for j in array:
        if i == j:
            count += 1
    if count > top_count:
        top_count = count
        top_num = i
    count = 0
# print(top_num, top_count)

total = 0
variables = [array, top_count, top_num, count, array[-1], array[-1]]  # array[-1] - last value of variable i,j in cycle
for i in variables:
    show(i)

print(f'Allocated memory for variables in the first program = {total} bytes')


counter = {}
top_count = 1
top_num = None
for i in array:
    if i in counter:
        counter[i] += 1
    else:
        counter[i] = 1
    if counter[i] > top_count:
        top_count = counter[i]
        top_num = i
# print(top_num, top_count)

total = 0
variables = [array, counter, top_count, top_num, array[-1]]
for i in variables:
    show(i)

print(f'Allocated memory for variables in the second program = {total} bytes')


count = Counter(array)
top_num = 0
top_count = 0
for i in count:
    if count[i] > top_count:
        top_num, top_count = i, count[i]
# print(top_num, top_count)

total = 0
variables = [array, count, top_count, top_num, count[-1]]
for i in variables:
    show(i)

print(f'Allocated memory for variables in the third program = {total} bytes')