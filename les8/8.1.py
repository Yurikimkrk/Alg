# 1) Определение количества различных подстрок с использованием хеш-функции.
# Пусть на вход функции дана строка. Требуется вернуть количество различных
# подстрок в этой строке.
# Примечание: в сумму не включаем пустую строку и строку целиком.
# Пример работы функции:func("papa")6func("sova")9

a = input("input any line: ")
substrings = set()
for i in range(len(a)):
    for j in range(len(a) - 1 if i == 0 else len(a), i, -1):
        substrings.add(hash(a[i:j]))
print(f"number of substrings - {len(substrings)}")
