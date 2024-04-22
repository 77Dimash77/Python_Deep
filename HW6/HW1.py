# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.

import argparse
from datetime import datetime


def check_date(input_date):
    try:
        date = datetime.strptime(input_date, '%Y-%m-%d')
        print("Введенная дата:", date)
        print("Дата верна!")
    except ValueError:
        print("Неверный формат даты. Используйте формат YYYY-MM-DD.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Проверка корректности введенной даты.")
    parser.add_argument("date", help="Дата для проверки в формате YYYY-MM-DD")
    args = parser.parse_args()

    check_date(args.date)
