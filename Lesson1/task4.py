"""
4.  Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
    Для решения используйте цикл while и арифметические операции.
"""

number = input('Введите целое положительное число : ')
i = 0
maxdigit = '0';


if number.isdigit() and int(number) > 0 and number[0] != '0':
    while i < len(number):
        if number[i] > maxdigit:
            maxdigit = number[i]
        i = i + 1
    print(f'Максимальное цифра в числе {number} - это {maxdigit}')
else:
    print(f'Введите правильно число')

