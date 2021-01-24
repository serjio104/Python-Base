"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента
 и возвращает сумму наибольших двух аргументов.
"""

# 1 решение
def calc_sum_2larg_numbers(num1, num2, num3):
    sum12 = num1 + num2
    sum13 = num1 + num3
    sum23 = num2 + num3
    return max(sum12, sum13, sum23)

# 2 решение
def calc_sum2(num1,num2,num3):
    my_list = [num1,num2,num3]
    my_list.remove(min(num1,num2,num3))
    return sum(my_list)

try:
    number1, number2, number3 = (float(input('Первый аргумент: ')),
                                 float(input('Второй аргумент: ')),
                                 float(input('Третий аргумент: '))
                                 )
except ValueError:
    print(f'вы ввели не число.')
else:
    print(f'решение 1 сумма наибольших двух аргументов = {calc_sum_2larg_numbers(number1, number2, number3)}')
    print(f'решение 2 сумма наибольших двух аргументов = {calc_sum2(number1, number2, number3)}')
