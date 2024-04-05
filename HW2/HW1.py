# Напишите программу, которая получает целое число и возвращает
# его шестнадцатеричное строковое представление. Функцию hex
# используйте для проверки своего результата.

decimal_number = int(input("Введите число в десятичной системе: "))
hexadecimal_number = format(decimal_number, 'X')
print("Число в шестнадцатеричной системе:", hexadecimal_number)
strdem = ("0x" + str(hexadecimal_number)).lower()
# Проверка
h = hex(decimal_number)
if strdem == h:
    print(True)
else:
    print(False)
print(strdem)
