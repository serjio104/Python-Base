"""
5. Создать (программно) текстовый файл,
записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
from functools import reduce
import numbers


def product_numbers(product,el):
    return float(product) + float(el)


def test_string(param):
    result = True
    for num in param:
        try:
            num = float(num)
        except ValueError:
            print('Вы ввели не число.')
            exit(1)


with open('task5.txt','w',encoding='utf-8') as f:
    string = input('Ведите числа, разделенные пробелами : ')
    test_string(string.split())
    f.write(string)
with open('task5.txt','r',encoding='utf-8') as f:
    my_list = f.read().split()
    sum_all1 = reduce(lambda el1,el2: float(el1) + float(el2),my_list)  # ???????????????????
    print(f'1 вариант: сумма чисел в файле = {sum_all1}')

    sum_all2 = reduce(product_numbers,my_list)  # ???????????????????
    print(f'2 вариант: сумма чисел в файле = {sum_all2}')

    sum_all3 = 0
    for number in my_list:
        sum_all3 += float(number)
    print(f'3 вариант: сумма чисел в файле = {sum_all3}')

    # И самый оптимальный вариант - приходит опосля
    # Функция map() в Python, обработка последовательности без цикла.
    print(f'4 вариант САМЫЙ КРУТОЙ: сумма чисел в файле = {sum(map(float,my_list))}')
