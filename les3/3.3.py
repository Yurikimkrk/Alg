# 3.	В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

SIZE = 20
MIN_ITEM = 0
MAX_ITEM = 50
array = [random.randint(MIN_ITEM, MAX_ITEM) for i in range(SIZE)]
min_el = MAX_ITEM
max_el = MIN_ITEM
min_index = 0
max_index = 0
for i in range(len(array)):
    if array[i] < min_el:
        min_el, min_index = array[i], i
    if array[i] > max_el:
        max_el, max_index = array[i], i
print(array)
array[min_index], array[max_index] = array[max_index], array[min_index]
print(array)
