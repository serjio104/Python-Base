"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве
делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class DivisionByNull:
    def __init__(self,numerator,denominator):
        self.numerator = numerator
        self.denominator = denominator

    @staticmethod
    def divide_by_null(numerator, denominator):
        try:
            return numerator / denominator
        except ZeroDivisionError:
            return f'Делить на 0 - нельзя'


division = DivisionByNull(1,1)
print(DivisionByNull.divide_by_null(0,0))
print(DivisionByNull.divide_by_null(1,0.25))
print(division.divide_by_null(1.45,0))
