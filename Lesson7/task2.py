"""
2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3).
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта,
проверить на практике работу декоратора @property.
"""

# Чтобы объявить абстрактный класс, нам сначала нужно импортировать модуль abc .

from abc import ABC,abstractmethod


class Clothes(ABC):

    def __init__(self,param):
        self.param = param

    @property
    def consumption(self):
        return f'Общий расход ткани : {self.param / 6.5 + 0.5 + 2 * self.param + 0.3 :.2f}'

    @abstractmethod
    def abstract(self):
        return 'vary abstract Clothes'


class Coat(Clothes):
    def consumption(self):
        return f'Расход ткани для пошива пальто : {self.param / 6.5 + 0.5 :.2f}'

    def abstract(self):
        return 'vary abstract Coat'


class Costume(Clothes):
    def consumption(self):
        return f'Расход ткани для пошива костюма : {2 * self.param + 0.3 :.2f}'

    def abstract(self):
        return 'vary abstract Costume'


coat_obj = Coat(100)
costume_obj = Costume(100)

print(coat_obj.consumption())
print(costume_obj.consumption())
print(coat_obj.abstract())
print(costume_obj.abstract())
