'''
Повторяй за мной 1
Дано предложение и количество раз которое его надо повторить. Напишите программу, которая повторяет данное предложение нужное количество раз.

Формат входных данных
В первой строке записано текстовое предложение, во второй — количество повторений.

Формат выходных данных
Программа должна вывести указанное текстовое предложение нужное количество раз. Каждое повторение должно начинаться с новой строки.
'''

# proposal = input()
# repeat = int(input())
# for _ in range(repeat):
#     print(proposal)

# a = int(input())
# b = int(input())

# summ = a + b
# summ /= 3
# print(summ)
# # if summ / 3

# my_str = 'Шла Саша по шоссе'
# my_str = my_str.replace('Шла', 'Гуляла')
# print(my_str)

# my_list = [1, 2, 3, 4, 'a', ',', '213', 123.2, True]

# data_type_int = 0
# data_type_str = 0
# data_type_float = 0
# data_type_bool = 0

# def data_type_print():
#     print(f'В списке "my_list" тип данных "int" встречается:\t{data_type_int} раза.\n')
#     print(f'В списке "my_list" тип данных "str" встречается:\t{data_type_str} раза.\n')
#     print(f'В списке "my_list" тип данных "float" встречается:\t{data_type_float} раз.\n')
#     print(f'В списке "my_list" тип данных "bool" встречается:\t{data_type_bool} раз.\n')
#     return data_type_int, data_type_str, data_type_float, data_type_bool

# for i in my_list:
#     print(type(i))
#     if type(i) == int:
#         data_type_int += 1
#     elif type(i) == str:
#         data_type_str += 1
#     elif type(i) == float:
#         data_type_float += 1
#     elif type(i) == bool:
#         data_type_bool += 1
# data_type_print()

# Именная функция.
def foo(a, b):
    '''Возвращает частное от деления.

    Именованные параметры:
    a - задается пользователем.
    b - задается пользователем.

    '''
    print(int(a / b))
    return(a / b)
    
try:
    foo(a = int(input()), b = int(input()))
except ZeroDivisionError:
    print('На ноль делить нельзя!')

# Анонимная или несвязанная функция.
foo1 = lambda a1, b1: a1 / b1
try:
    print(foo1(a1 = int(input()), b1 = int(input())))
except ZeroDivisionError:
    print('Ноль не может быть делителем!')

# Анонимная или несвязанная функция. Надеюсь на работе так не пишут.
try:
    print((lambda a2, b2: a2 / b2) (a2 = int(input()), b2 = int(input())))
except ZeroDivisionError:
    print('Не дели на 0!')
