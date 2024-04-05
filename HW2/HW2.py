# # Напишите программу, которая принимает две строки вида “a/b” - дробь
# с числителем и знаменателем. Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions


from fractions import Fraction
def calculate_sum_and_product(fraction1, fraction2):
    frac1 = Fraction(fraction1)
    frac2 = Fraction(fraction2)

    sum_result = frac1 + frac2
    product_result = frac1 * frac2

    return sum_result, product_result


fraction1_str = input("Введите первую дробь в формате a/b: ")
fraction2_str = input("Введите вторую дробь в формате a/b: ")

sum_result, product_result = calculate_sum_and_product(fraction1_str, fraction2_str)

print("Сумма дробей:", sum_result)
print("Произведение дробей:", product_result)
