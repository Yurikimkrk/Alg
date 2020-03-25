# 1). Отсортируйте по убыванию методом пузырька одномерный целочисленный
# массив, заданный случайными числами на промежутке [-100; 100).
# Выведите на экран исходный и отсортированный массивы.

from random import randint

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 99
array = [randint(MIN_ITEM, MAX_ITEM) for i in range(SIZE)]
print(f"random array - {array}")


def bubble(arr):
    n = 1
    while n < len(arr):
        for i in range(len(arr) - n):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        n += 1
    array.reverse()
    return array


print(f"sorted array - {bubble(array)}")
