# Программа загадывает число от 0 до 1000. Необходимо угадать число
# за 10 попыток. Программа должна подсказывать “больше” или “меньше” после
# каждой попытки. Для генерации случайного числа используйте код:
# from random import randintnum = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint
randnum = randint(0, 1000)
count = 1
while count <= 11:
    a = int (input("введите ваше число"))
    if a == randnum:
        print(f"Вы победили c {count} попытки")
        break
    else:
        if a > randnum:
            print("Меньше")
            count += 1
        if a < randnum:
            print("Больше")
            count += 1
        if count == 11 and a!= randnum:
            print("Вы проиграли!")
            break