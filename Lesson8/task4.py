"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других
данных, можно использовать любую подходящую структуру, например словарь.
6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например,
для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на
уроках по ООП.

Похоже задачи 4 5 и 6 - это одна задвча , хотя написано непонятно


Написана какая - то хренЬ :
Создайте класс, описывающий склад и потом класс «Оргтехника»,
"""


class Warehouse:
    pass


class Equipments:
    def __init__(self,name,make,year,price,quantity):
        self.name = name
        self.make = make
        self.year = year
        self.price = price
        self.quantity = quantity
        self.my_store_full = []
        self.my_store = []
        self.my_unit = {}

    def __str__(self):
        return f'Модель устройства:{self.name} Сделано в:{self.make} \
         Год производства:{self.year} цена {self.price} количество: {self.quantity}'

    def reception(self):
        try:
            u_name = input(f'Введите наименование: ')
            u_make = input(f'Введите страну производства:')
            u_year = input(f'Год выпуска:')
            u_price = int(input(f'Введите цену за ед :'))
            u_quantity = int(input(f'Введите количество :'))
            unique_device = {'Модель ': u_name,'Страна': u_make,'Год': u_year,'Цена за ед': u_price,
                             'Количество': u_quantity}
            self.my_unit.update(unique_device)
            self.my_store.append(unique_device)
            print(f'Список устройств :-\n {self.my_store}')
        except ValueError:
            return f'Недопустимый тип вводимых данных'

        val = input(f'Продожать - Y , выход - N ')
        if val.lower() == 'n':
            self.my_store_full.append(self.my_store)
            print(f'Состояние всего склада :\n{self.my_store_full}')
            return f'Выход из цикла ввода'
        else:
            return Equipments.reception(self)


class Printer(Equipments):
    def __init__(self,type_printer,name,make,year,price,quantity):
        super().__init__(name,make,year,price,quantity)
        self.type_printer = type_printer

    def to_print(self):
        return f'Принтер  стоит {self.price} рублей'


class Scanner(Equipments):
    def to_print(self):
        return f'Сканер стоит {self.price} рублей'


class Copier(Equipments):
    def to_print(self):
        return f'Ксерокс стоит {self.price} рублей'


printer = Printer('Laser','hp','China',2010,40000,10)
print(printer.reception())
print(printer.to_print())

scanner = Scanner('Canon','Russia',2020,4200,10)
print(scanner.reception())
print(scanner.to_print())

copier = Copier('Xerox','USA',1500,1,15)
print(copier.reception())
print(copier.to_print())
