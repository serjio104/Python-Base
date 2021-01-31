"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

my_dict = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}

out_list = []
with open('task4.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.split(' ', 1)
        out_list.append(my_dict[line[0]] + ' ' + line[1])

with open('task4_1.txt', 'w', encoding='utf-8') as f:
    f.writelines(out_list)
    print(f'{out_list} блок строк записан в текстовый файл task_4.txt')
