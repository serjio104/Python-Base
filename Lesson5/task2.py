"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк,
количества слов в каждой строке.
"""
# 1 вариант
try:
    f = open('task1.txt','r',encoding='utf-8')
except FileNotFoundError:
    print(f'нет такого файла.1 вариант')
else:
    print(f'1 вариант')
    count = 0
    for line in f:
        count += 1
        print(f'число слов =  {len(line.split())}  Строка : ',line.replace('\n',''))
    print(f'Число строк = {count}\n')
    f.close()

# 2 вариант количество строк
try:
    f = open('task1.txt','r',encoding='utf-8')
except FileNotFoundError:
    print(f'нет такого файла.2 вариант')
else:
    print(f'2 вариант')
    print(f'Число слов = ',[len(line.split()) for line in f])
    f.seek(0)
    print(f'Число строк = {sum(1 for line in f)}\n')

# 3 вариант количества строк
try:
    f = open('task1.txt','r',encoding='utf-8')
except FileNotFoundError:
    print(f'нет такого файла.3 вариант')
else:
    print(f'3 вариант')
    print(f'Число строк = {len(f.readlines())}')
    f.close()
