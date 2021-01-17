"""
1.  Поработайте с переменными, создайте несколько, выведите на экран,
    запросите у пользователя несколько чисел и строк и сохраните в переменные,
    выведите на экран.
"""
age = 50
name_Team = 'Моя любимая команда :'
str_Number = 'Моя любимое чмсло :'

team = input("Введите название Вашей любимой команды : ")
number = int(input("Введите Ваше любимое число : "))
print(f'Переменная age равна {age}')
print('Переменная age равна {}'.format(age))
if team:
    print(f'{name_Team} {team}')
    print('{} {}'.format(name_Team, team))
if str_Number:
    print(f'{str_Number} {number}')
    print('{} {}'.format(str_Number, number))
