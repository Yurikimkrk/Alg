# 3). Массив размером 2m + 1, где m — натуральное число, заполнен случайным
# образом. Найдите в массиве медиану. Медианой называется элемент ряда,
# делящий его на две равные части: в одной находятся элементы,
# которые не меньше медианы, в другой — не больше медианы.

from random import randint

a = int(input("Input positive integer: "))

size = 2 * a + 1
MIN_ITEM = 0
MAX_ITEM = 20
array = [randint(MIN_ITEM, MAX_ITEM) for i in range(size)]
print(f"random array - {array}")

eq = 0
more = 0
less = 0
answer = 0
for i in range(len(array)):
    for j in range(len(array)):
        if i != j:
            if array[i] == array[j]:
                eq += 1
            elif array[i] > array[j]:
                less += 1
            else:
                more += 1
    if more == eq + less or less == eq + more:
        answer = array[i]
    else:
        eq = 0
        more = 0
        less = 0

print(f"median = {answer}")
