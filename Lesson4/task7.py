"""
7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
При вызове функции должен создаваться объект-генератор.
Функция должна вызываться следующим образом: for el in fact(n).
Функция отвечает за получение факториала числа,
а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
Подсказка: факториал числа n — произведение чисел от 1 до n.
Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
Конструкция yield
Это итерируемый объект, который можно использовать один раз, 
так как при использовании генератора значения не хранятся в памяти.
Они формируются в процессе обращения к ним, по мере запроса.
Оператор yield по назначению похож с оператором return, но возвращает генератор вместо значения.
"""

from itertools import count
from math import factorial




def calc_fact(n):
    res = 1
    for i in range(1, n + 1):
        res = res * i
    return res


# 1 вариант
def fact():
    for el1 in count(0):
        print(el1)
        yield calc_fact(el1)





print('\n')
print(f'1 вариант:{fact()}')
s = 0
for el in fact():
    if s > 10:
        break
    else:
        print(f"Факториал {s} = {el} ")
        s += 1


# 2 вариант
def fact():
    for el2 in count(0):
        yield factorial(el2)

print('\n')
print(f'2 вариант:{fact()}')
s = 0
for el in fact():
    if s > 10:
        break
    else:
        print(f"Факториал {s} = {el} ")
        s += 1
print('\n')
print(f'3 вариант:{fact()}')
def fact1():
    fac = 1
    #yield fac
    for el1 in count(1):
        yield  fac
        fac *= el1



s = 0
for el in fact1():
    if s > 10:
        break
    else:
        print(f"Факториал {s} = {el} ")
        s += 1



1