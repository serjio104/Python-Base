"""
3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
"""
number_User = input("Введите число : ")
def func_1(number,count):
    numberOld = number
    summa = 0
    for i in range(1,count):
       try:
           summa += int(number)
       except ValueError:
           print(f'{number_User} - это не положительное число')
           break
       else:
           number += numberOld
    return summa

result = func_1(number_User, 4)
if result and result > 0:
    print(f'Ответ - {result}')
