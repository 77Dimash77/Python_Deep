# Напишите функцию в шахматный модуль. Используйте генератор
# случайных чисел для случайной расстановки ферзей в задаче выше.
# Проверяйте различный случайные варианты и выведите 4 успешных расстановки.

import random

def queens_attack(queens):
    for i in range(len(queens)):
        for j in range(i + 1, len(queens)):
            if (queens[i][0] == queens[j][0] or
                queens[i][1] == queens[j][1] or
                abs(queens[i][0] - queens[j][0]) == abs(queens[i][1] - queens[j][1])):
                return False
    return True

def random_queens():
    queens = []
    rows = random.sample(range(1, 9), 8)
    for i in range(8):
        queens.append((rows[i], random.randint(1, 8)))
    return queens

if __name__ == "__main__":
    successful_arrangements = 0
    attempts = 0
    while successful_arrangements < 4:
        attempts += 1
        queens = random_queens()
        if queens_attack(queens):
            print(f"Успешная расстановка ферзей: {queens}")
            successful_arrangements += 1
    print(f"Попыток: {attempts}")
