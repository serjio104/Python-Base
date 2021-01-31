"""
3. Создать текстовый файл (не программно),
построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""
salary = 20000
try:
    staff_list = [line.split() for line in open('task3.txt','r',encoding='utf-8') if int(line.split()[1]) < salary]
except FileNotFoundError:
    print('нет такого файла.')
else:
    salary_list = []
    for staff in staff_list:
        salary_list.append(staff[1])
        print(f'Сотрудник, имеющий оклад < {salary} : {staff[0]} оклад : {staff[1]}')
    print(f'\nсредний доход сотрудников, имеющих оклад < {salary} = {sum(map(int,salary_list)) / len(salary_list)}')
