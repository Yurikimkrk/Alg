# 1.	Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
# https://drive.google.com/file/d/1wiNKsoVBb2FYTBpgQd_0xQ2AYbA8XlS7/view?usp=sharing
a = int(input('Введите число от 100 до 999   '))
s = a//100 + (a//10)%10 + a%10
p = (a//100)*((a//10)%10)*(a%10)
print(f'сумма равна {s}, произведение равно {p}')