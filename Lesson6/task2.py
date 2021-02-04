"""
2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.

Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу:
длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см * число см толщины полотна.

Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т
"""


# про метод расчета массы асфальта написано очень витьевато 

# 1 вариант
class Road:
    mas = 0
    thickness = 0

    def __init__(self,_length,_width):
        self._length = _length
        self._width = _width

    def calculate_mass(self):
        return self._width * self._length * self.mas * self.thickness / 1000


obj = Road(20,5000)
obj.mas = 25
obj.thickness = 5
print(obj.calculate_mass())


# 2 вариант
class Road:
    def __init__(self,_length,_width):
        self._length = _length
        self._width = _width

    def calculate_mass(self):
        return self._width * self._length


# 2 вариант
class MassCount(Road):
    def __init__(self,_length,_width,_mas,_thickness):
        super().__init__(_length,_width)
        self._mas = _mas
        self._thickness = _thickness


obj = MassCount(20,5000,25,5)
print(obj.calculate_mass() * obj._mas * obj._thickness / 1000)
