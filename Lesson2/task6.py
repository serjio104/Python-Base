"""
6. * Реализовать структуру данных «Товары».
Она должна представлять собой список кортежей. Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
Пример готовой структуры:
[
(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]
Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
например название, а значение — список значений-характеристик, например список названий товаров.
Пример:
{
“название”: [“компьютер”, “принтер”, “сканер”],
“цена”: [20000, 6000, 2000],
“количество”: [5, 2, 7],
“ед”: [“шт.”]
}
"""

"""
список кортежей. Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения).
запрашивать все данные у пользователя.
если ПРОКАТЫВАЕТ такое:
a,b,c =input('1111 :'),input('2222 :'),input('3333 :')
print(a,b,c)
"""
my_tuple_list = []
while True:
    my_tuple_list.append(
        (input('Введите номер товара: '),
         dict({
             'название': input('Название товара : '),
             'цена': float(input('Цена товара : ')),
             'количество': int(input('Количество товара : ')),
             'eд': input('Единица измерения : '),
         }
         )
         )
    )
    if input('Ввести новый товар? (нет = 1 ): ') == '1':
        break
my_dic_list = {}
for product in my_tuple_list:
    product_chars = product[1]
    for key, value in product_chars.items():
        if key in my_dic_list:
            # проверяю есть ли такое значение по ключю
            # если нет  - добавляю данные
            # my_dic_list.get( key ) - это List
            if value not in my_dic_list.get(key):
                record = my_dic_list.get(key)
                record.append(value)
        else:
            # Добавляю 1 запись в my_dic_list
            my_dic_list.update({key: [value]})

"""
словарь, в котором каждый ключ — характеристика товара,
"""
print(type(my_dic_list))
for key, value in my_dic_list.items():
    print("=", key, value)
