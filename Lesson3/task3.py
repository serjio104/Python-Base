"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента
 и возвращает сумму наибольших двух аргументов.
"""


def calc_sum_2larg_numbers(num1, num2, num3):
    sum12 = num1 + num2
    sum13 = num1 + num3
    sum23 = num2 + num3
    return max(sum12, sum13, sum23)


number1, number2, number3 = (float(input('Первый аргумент: ')),
                             float(input('Второй аргумент: ')),
                             float(input('Третий аргумент: '))
                             )

print(f'сумма наибольших двух аргументов = {calc_sum_2larg_numbers(number1, number2, number3)}')
