# 6. В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться, больше или меньше введенное
# пользователем число, чем то, что загадано. Если за 10 попыток число не отгадано,
# вывести правильный ответ.

import random

x = random.randint(1, 100)

count = 0
while True:
    if count == 10:
        print (f"You are so stupid. You didn't guess in 10 attempts! Answer is {x}")
        break
    else:
        answer = int (input(f"Choose a number (1 - 100). Attempt {count + 1}: "))
        if answer == x:
            print(f"You win - {x} it's right number")
            break
        else:
            if answer > x:
                print ("The hidden number is less")
            else:
                print ("The hidden number is bigger")
            count += 1