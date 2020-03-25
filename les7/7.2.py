# 2). Отсортируйте по возрастанию методом слияния одномерный вещественный
# массив, заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.

from random import random

SIZE = 10
array = [random() * 50 for i in range(SIZE)]
print(f"random array - {array}")


def merge(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_list = arr[:mid]
    right_list = arr[mid:]

    left_list = merge(left_list)
    right_list = merge(right_list)
    return list(half(left_list, right_list))


def half(left, right):
    lst = []
    while len(left) != 0 and len(right) != 0:
        if left[0] < right[0]:
            lst.append(left[0])
            left.remove(left[0])
        else:
            lst.append(right[0])
            right.remove(right[0])
    if len(left) == 0:
        lst = lst + right
    else:
        lst = lst + left
    return lst


print(f"sorted array - {merge(array)}")
