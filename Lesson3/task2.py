"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""


def describe_data(name, surname, year_Birth, city_residence, email, phone):
    print(
        f'Имя:{name} Фамилия:{surname} Год рождения:{year_Birth} Город проживания:{city_residence} email:{email} телефон:{phone}')


describe_data(name=input('Имя : '), surname=input('Фамилия : '),
              year_Birth=input('Год рождения : '), city_residence=input('Город проживания : '),
              email=input('Email : '), phone=input('Телефон : ')
              )
