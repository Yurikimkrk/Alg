# 5.	В массиве найти максимальный отрицательный элемент. Вывести на экран его значение
# и позицию в массиве. Примечание к задаче: пожалуйста не путайте
# «минимальный» и «максимальный отрицательный». Это два абсолютно разных значения.

import random

SIZE = 20
MIN_ITEM = -20
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for i in range(SIZE)]
print(array)
top_negative = "No negative numbers in the array"
top_index = "None"
for i in range(len(array)):
    if array[i] < 0:
        if top_negative == "No negative numbers in the array" or array[i] > top_negative:
            top_negative, top_index = array[i], i

print(f"Top negative number - {top_negative}. Index of number - {top_index}")



