# 2.	Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого — цифры
# числа. Например, пользователь ввёл A2 и C4F. Нужно сохранить их как
# [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
# произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
from collections import deque

NUMB_LEN = 16
summ = deque()
numb = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
first = list(input("input first number: ").upper())
second = list(input("input second number: ").upper())
plus_one = 0
for i in range(max(len(first), len(second))):
    try:
        a = numb.index(first[-(i + 1)]) + numb.index(second[-(i + 1)]) + plus_one
        if a > NUMB_LEN - 1:
            plus_one = 1
            summ.append(numb[a - NUMB_LEN])
        else:
            plus_one = 0
            summ.append(numb[a])
    except IndexError:
        try:
            a = numb.index(first[-(i + 1)]) + plus_one
            if a > NUMB_LEN - 1:
                plus_one = 1
                summ.append(numb[a - NUMB_LEN])
            else:
                plus_one = 0
                summ.append(numb[a])
        except IndexError:
            a = numb.index(second[-(i + 1)]) + plus_one
            if a > NUMB_LEN - 1:
                plus_one = 1
                summ.append(numb[a - NUMB_LEN])
            else:
                plus_one = 0
                summ.append(numb[a])
if plus_one:
    summ.append("1")
summ.reverse()
print("".join(summ))

# Кажется немного перемудрил с кодом, да еще и много задвоенного, но уже нет времени править
# (завтра не будет времени на учебу, а хотел успеть сдать ПЗ)
# жду критики кода :)