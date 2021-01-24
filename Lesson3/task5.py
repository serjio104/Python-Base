"""
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
 Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел
к полученной ранее сумме и после этого завершить программу.
"""

def type_error():
    print('Вы ввели не число.')


spec_symbol = ':'
is_cycle = True
total_Amount = 0

while is_cycle:
    string_numbers = input('Ведите строку чисел, разделенных пробелом : ').split(' ')
    for number in string_numbers:
        if number == spec_symbol:
            is_cycle = False
            break
        else:
            if spec_symbol in number:
                i = 0
                before_Spec = ''
                while i < number.index(spec_symbol):
                    before_Spec += number[i]
                    i += 1
                try:
                    total_Amount += float(before_Spec)
                except ValueError:
                    type_error()
                else:
                    is_cycle = False
                    break
            else:
                if  number:
                    try:
                        total_Amount += float(number)
                    except ValueError:
                        type_error()

    print(f'Общая сумма введенных чисел = {total_Amount}')
