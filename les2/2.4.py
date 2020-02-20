# 4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.

x = int(input("Enter the positive integer: "))
numb = 1
sum = 1
while x > 1:
    numb /= -2
    sum += numb
    x -= 1
print(sum)
