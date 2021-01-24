"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
 Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def delete_numbers(num1, num2):
    try:
        result = num1 / num2
    except ZeroDivisionError as e:
        print(e, ' Деление на 0')
    else:
        return result


number1, number2 = (int(input('Первое число :')), int(input('Второе число :')))
print(f'{number1}/{number2} = {delete_numbers(number1, number2)}')
