"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
 «день-месяц-год».
В рамках класса реализовать два метода.
Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать
их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года
например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""


# class Data:
#
#     # def __init__(self,data):
#     #     self.data = data
#
#     @classmethod
#     def my_method(cls,param):  # Метод класса
#         print(cls,param)
#
# Data.my_method('07-08-1961')  # Вызов метода через название класса
# mc = Data().
# mc.my_method(07-08-1961)  # Вызов метода класса через экземпляр

class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract_number(cls, day_month_year):
        my_date = []
        for value in day_month_year.split('-'):
            my_date.append(value)
            # я понял так 
        return int(my_date[0]) + int(my_date[1]) + int(my_date[2])
        #return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid_numbers(day, month, year):
        """По хорошему надо анализировать по високосному году по числу дней в месяце
           Но нет вреиени Поэтому напишу просто """
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if year >= 0:
                    return f'Дата введена правильно'
                else:
                    return f'В дате неверно введен год'
            else:
                return f'В дате неверно введен месяц'
        else:
            return f'В дате неверно введен день'

    def __str__(self):
        return f'Сегодня : {Data.extract_number(self.day_month_year)}'


today = Data('13-02-2021')
print(today)
print(type(today.extract_number('13-02-2021')))
print(Data.extract_number('13-02-2021'))
print(today.extract_number('13-02-2021'))

print(Data.valid_numbers(13, 12, 2021), '(13, 12, 2021)')
print(today.valid_numbers(32, 11, 2021),'(32, 12, 2021)')
print(today.valid_numbers(13, 13, 2021),'(13, 13, 2021)')
print(today.valid_numbers(13, 12, -10),'(13, 12, -10)')