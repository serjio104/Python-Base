"""
4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
Если в слово длинное, выводить только первые 10 букв в слове.
"""
my_string = input('Введите строку из нескольких слов, разделённых пробелами : ').strip()
rez = my_string.split(' ')
count_letters = 10
if my_string:
    for i, word in enumerate(rez):
        if len(word) > count_letters:
            print(str(i + 1), word[:count_letters])
        else:
            print(str(i + 1), word)
