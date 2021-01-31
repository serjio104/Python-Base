"""
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные
о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.

Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
а также словарь со средней прибылью. Если фирма получила убытки,
также добавить ее в словарь (со значением убытков).

Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""
import json


def have_profits(f):
    temp_list = [line1.split() for line1 in f if float(line1.split()[2]) > float(line1.split()[3])]
    f.seek(0)
    return len(temp_list)


my_list = []
my_dict1 = {}
my_dict2 = {}

with open('task7.txt','r',encoding='utf-8') as f:
    try:
        count = have_profits(f)
    except ValueError:
        print(f'Проверьте формат файла task7.txt')
        exit(1)
    else:
        average_profit = 0.0
        for line in f:
            name,ownership,revenue,costs = line.split()
            revenue = float(revenue)
            costs = float(costs)
            profit = revenue - costs
            print(f'Прибыль компании {name} : {profit}')
            my_dict1[name] = profit
            if profit > 0:
                average_profit += profit
    my_dict2['average_profit'] = average_profit / count
    print(f'Средняя прибыль :{average_profit / count}')
    my_list.append(my_dict1)
    my_list.append(my_dict2)
    print(f'список, содержащий словарь с фирмами и их прибылями : \n{my_list}\n')

with open('task7.json','w',encoding='utf-8') as f:
    json.dump(my_list,f)
#  проверяю из файла в оъект
with open('task7.json','r',encoding='utf-8') as f:
    my_list = json.load(f)
    print(f'Список из файла task7.json для проверки : \n{my_list}')
