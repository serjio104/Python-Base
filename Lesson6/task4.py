"""
4. Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать,
что машина поехала, остановилась, повернула (куда).

Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.

Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.

Для классов TownCar и WorkCar переопределите метод show_speed.

При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.

Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
"""


class Car:
    def __init__(self,speed,color,name,is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go_machine(self):
        print(f'{self.name} поехала')

    def stop_machine(self):
        print(f'{self.name} остановилась')

    def veer_machine(self,direction):
        print(f'{self.name} повернула на {direction}')

    def show_speed(self):
        print(f'Текущая скорость автомобиля {self.name} равна {self.speed} км/час')


class TownCar(Car):
    def __init__(self,speed,color,name,is_police):
        super().__init__(speed,color,name,is_police)

    def show_speed(self):
        print(f'Текущая скорость городского  автомобиля  {self.name} равна {self.speed} км/час')
        if self.speed > 60:
            print(f'{self.name} Вы превысили скорость на {self.speed - 60} км/час')


class SportCar(Car):
    def __init__(self,speed,color,name,is_police):
        super().__init__(speed,color,name,is_police)


class WorkCar(Car):
    def __init__(self,speed,color,name,is_police):
        super().__init__(speed,color,name,is_police)

    def show_speed(self):
        print(f'Текущая скорость рабочего автомобиля  {self.name} равна {self.speed} км/час')
        if self.speed > 40:
            print(f'TownCar Вы превысили скорость на {self.speed - 40} км/час')


class PoliceCar(Car):
    def __init__(self,speed,color,name,is_police):
        super().__init__(speed,color,name,is_police)

    def police(self):
        if self.is_police:
            print(f'{self.name} принадлежит полиции')
        else:
            print(f'{self.name} не принадлежит полиции')


directions = ['Север','Восток','Юг','Запад']
objTown = TownCar(65,'Green','Hyundai',False)
objSport = SportCar(300,'Red','Ferrari',False)
objWork = WorkCar(47,'Black','Gazelle',False)
objPolice = PoliceCar(100,'Green','Ford',True)

print(
    f'Городской автомобиль : Марка {objTown.name} Цвет {objTown.color} Скорость {objTown.speed} Полицейская {objTown.is_police}')
objTown.show_speed()
objTown.go_machine()
objTown.stop_machine()
objTown.veer_machine(directions[0])
print('\n')

print(
    f'Спортивный автомобиль : Марка {objSport.name} Цвет {objSport.color} Скорость {objSport.speed} Полицейская {objSport.is_police}')
objSport.show_speed()
objSport.go_machine()
objSport.stop_machine()
objSport.veer_machine(directions[1])

print('\n')
print(
    f'Рабочий автомобиль : Марка {objWork.name} Цвет {objWork.color} Скорость {objWork.speed} Полицейская {objWork.is_police}')
objWork.show_speed()
objWork.go_machine()
objWork.stop_machine()
objWork.veer_machine(directions[2])
try:
    objWork.police()
except AttributeError:
    print(f'метода police() в классе нет')
print('\n')
print(f'Полицейский автомобиль : Марка {objPolice.name} Цвет {objPolice.color} Скорость {objPolice.speed} \
Полицейская {objPolice.is_police}')
objPolice.show_speed()
objPolice.go_machine()
objPolice.stop_machine()
objPolice.veer_machine(directions[3])
objPolice.police()
