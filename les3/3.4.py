# 4.	Определить, какое число в массиве встречается чаще всего.

import random

SIZE = 50
MIN_ITEM = 0
MAX_ITEM = 20
array = [random.randint(MIN_ITEM, MAX_ITEM) for i in range(SIZE)]
print(array)
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
print(f"Top number - {top_num}, {top_count} times in array")
