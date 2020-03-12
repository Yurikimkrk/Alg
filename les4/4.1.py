# Определить, какое число в массиве встречается чаще всего.
import random
from collections import Counter
from timeit import timeit
from cProfile import run

# Констранты ниже - разные размеры сгенерированных массивов для оценки скорости работы функций
SIZE1 = 20
SIZE2 = 200
SIZE3 = 2000
MIN_ITEM = 0
MAX_ITEM = 20
gen_array1 = [random.randint(MIN_ITEM, MAX_ITEM) for i in range(SIZE1)]
gen_array2 = [random.randint(MIN_ITEM, MAX_ITEM) for j in range(SIZE2)]
gen_array3 = [random.randint(MIN_ITEM, MAX_ITEM) for k in range(SIZE3)]


# Далее 3 функции для нахождения (вторая позаимствована с урока)
# При этом 1 и 3 находят самое частое число (если их 2 и более), которое первое по индексу встречается,
# а второе решение дает самое частое число, которое раньше встречается в последний раз).

def first(array):
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
    return top_num, top_count


print(timeit('first(gen_array1)', number=100, globals=globals()))  # 0.0020811999999999983
print(timeit('first(gen_array2)', number=100, globals=globals()))  # 0.1579112
print(timeit('first(gen_array3)', number=100, globals=globals()))  # 15.8811979
run('first(gen_array1)')
run('first(gen_array2)')
run('first(gen_array3)')

def second(array):
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
    if top_num is not None:
        return top_num, top_count


print(timeit('second(gen_array1)', number=100, globals=globals()))  # 0.0005515000000002601
print(timeit('second(gen_array2)', number=100, globals=globals()))  # 0.005754599999999499
print(timeit('second(gen_array3)', number=100, globals=globals()))  # 0.04404650000000032
run('second(gen_array1)')
run('second(gen_array2)')
run('second(gen_array3)')

def third(array):
    count = Counter(array)
    top_num = 0
    top_count = 0
    for i in count:
        if count[i] > top_count:
            top_num, top_count = i, count[i]
    return top_num, top_count


print(timeit('third(gen_array1)', number=100, globals=globals()))  # 0.0009009999999989304
print(timeit('third(gen_array2)', number=100, globals=globals()))  # 0.0022385000000006983
print(timeit('third(gen_array3)', number=100, globals=globals()))  # 0.01591139999999669
run('third(gen_array1)')
run('third(gen_array2)')
run('third(gen_array3)')

# Первая реализация с квадратичной зависимостью, остальные с линейной, при этом последний вариант
# самый быстрый при больших объемах информации, так как, несмотря на затраты времени на работу Counter,
# поиск ответа (самое часто встречающееся число) занимает уже гораздо меньше времени.