# 1.	В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому
# из чисел в диапазоне от 2 до 9.

MIN_ITEM = 2
MAX_ITEM = 99
MIN_NUMB = 2
MAX_NUMB = 9
array = [i for i in range(MIN_ITEM, MAX_ITEM + 1)]
count = 0
for n in range(MIN_NUMB, MAX_NUMB + 1):
    for i in range(len(array)):
        if array[i] % n == 0:
            count += 1
    print(f"{count} numbers are multiples of {n}")
    count = 0
