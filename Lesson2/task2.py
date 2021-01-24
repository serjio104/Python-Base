"""
2. Для списка реализовать обмен значений соседних элементов,
т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""



list_text = []
for i in  range(1,6):
    if i == 1:
        try:
            list_text.append( int(input( 'Введите значение целого числа : ' )) )
        except:
            print('Введите целое число верно !')
    elif i == 2:
        list_text.append( input( 'Введите значение строки: ' ) )
    elif i == 3:
        list_text.append( list(input( 'Введите значение элементов списка: ' )) )
    elif i == 4:
        list_text.append( tuple(input( 'Введите значение элементов кортежа: ' )) )
    elif i == 5:
        list_text.append( set(input( 'Введите значение элементов множества: ' )) )

s = -1
print( f' начальное состояние списка {list_text}')
for el in list_text:
    s = s + 1
    if not not s % 2:
        stor_Ind_Value = list_text[s]
        list_text[s] = list_text[s - 1]
        list_text[s - 1] = stor_Ind_Value
print( f' конечное состояние списка {list_text}')
