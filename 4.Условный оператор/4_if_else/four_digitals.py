'''
Напишите программу, которая определяет наименьшее из четырёх чисел.

Формат входных данных
На вход программе подаётся четыре целых числа.

Формат выходных данных
Программа должна вывести наименьшее из четырёх чисел.
'''
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a < b:
    low = a
else:
    low = b
# print(low)
if c < d:
    lower = c
else:
    lower = d
# print(lower)
if low < lower:
    print(low)
else:
    print(lower)
