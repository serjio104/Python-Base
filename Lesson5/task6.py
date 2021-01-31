"""
6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет
и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.

Сформировать словарь, содержащий название предмета и общее количество занятий по нему.

Вывести словарь на экран.

Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""


def turn_number(string):
    result = ''
    for i in string:
        if i.isdigit():
            result += i
    return int(result) if result.isdigit() else 0


my_dict = {}
with open('task6.txt','r',encoding='utf-8') as f:
    for line in f:
        my_dict[line.split()[0]] = turn_number(line.split()[1]) + turn_number(line.split()[2]) + \
                                   turn_number(line.split()[3])
    print(f'словарь, содержащий название предмета и общее количество занятий по нему. -  {my_dict}')

# можно более красиво
my_dict = {}
with open('task6.txt','r',encoding='utf-8') as f:
    for line in f:
        subject,lecture,practice,lab = line.split()
        my_dict[subject] = turn_number(lecture) + turn_number(practice) + turn_number(lab)
    print(f'словарь, содержащий название предмета и общее количество занятий по нему. -  {my_dict}')
