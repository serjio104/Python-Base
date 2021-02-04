"""
3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
оклад и премия, например, {"wage": wage, "bonus": bonus}.

Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода
с учетом премии (get_total_income).

Проверить работу примера на реальных данных
(создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""


# на самом деле 2 вариант конечно лучше , но 1 вариант возможен
# КАК ВЫ СЧИТАЕТЕ ?


# 1 вариант
class Worker:
    name = None
    surname = None
    position = None
    _income = {}


class Position(Worker):
    def __init__(self):
        super().__init__()

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return sum(self._income.values())
        # return self._income.get('wage') + self._income.get('bonus')


obj = Position()
obj.name = 'Сергей'
obj.surname = 'Иванов'
obj.position = 'Начальник'
obj._income = {"wage": 10000,"bonus": 5000}
print(obj.get_full_name())
print(obj.get_total_income())


# 2 вариант
class Worker:
    def __init__(self,name,surname,position,wage,bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage,"bonus": bonus}


class Position(Worker):
    def __init__(self,name,surname,position,wage,bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        # return sum(self._income.values())
        return self._income.get('wage') + self._income.get('bonus')


obj = Position('Сергей','Иванов','Начальник',10000,5000)
print(obj.get_full_name())
print(obj.get_total_income())
