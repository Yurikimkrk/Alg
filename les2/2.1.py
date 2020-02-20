# # https://drive.google.com/file/d/1xm-VHEQfWt9csqacq6HPm3QLOxXXuiG3/view?usp=sharing
# 1. Написать программу, которая будет складывать, вычитать, умножать или делить
# два числа. Числа и знак операции вводятся пользователем. После выполнения вычисления
# программа не завершается, а запрашивает новые данные для вычислений.
# Завершение программы должно выполняться при вводе символа '0' в качестве
# знака операции. Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'),
# программа должна сообщать об ошибке и снова запрашивать знак операции.
# Также она должна сообщать пользователю о невозможности деления на ноль,
# если он ввел его в качестве делителя.

sign = '+'
while sign != '0':
    num1 = float(input("input any number (1): "))
    num2 = float(input("input any number (2): "))
    sign = input("input the operation sign (0 - end of the program): ")
    if sign == '+':
        answer = num1 + num2
        print(f'{num1} + {num2} = {answer}')
    elif sign == '-':
        answer = num1 - num2
        print(f'{num1} - {num2} = {answer}')
    elif sign == '*':
        answer = num1 * num2
        print(f'{num1} * {num2} = {answer}')
    elif sign == '/':
        if num2 == 0:
            print("you can't divide by zero")
        else:
            answer = num1 / num2
            print(f'{num1} / {num2} = {answer}')
    else:
        if sign != "0":
            print("wrong sign")
        else:
            print("end of program")