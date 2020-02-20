# 2. Посчитать четные и нечетные цифры введенного натурального числа. Например,
# если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

a = int(input("Positive integer: "))
even = 0
odd = 0
while a > 0:
    if a % 2 == 0:
        even += 1
    else:
        odd += 1
    a //= 10
print (f'{even} even and {odd} odd digits in the current number')

