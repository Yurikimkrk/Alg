# 5.	Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят,
# и сколько между ними находится букв.
a = input('Введите первую букву  ')
b = input('Введите вторую букву  ')
first = ord(a) - 96
second = ord(b) - 96
between = abs(first - second) - 1
print(f'Номер первой буквы - {first}, номер второй буквы - {second}, букв между ними - {between}')
