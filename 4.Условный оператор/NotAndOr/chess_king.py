'''
Ход короля 🌶️
Даны две различные клетки шахматной доски. 
Напишите программу,  которая определяет, может ли король попасть с первой клетки на вторую одним ходом. 
Программа получает на вход четыре числа от 1 до 8 каждое, задающие номер столбца и номер строки сначала для первой клетки, 
потом для второй клетки. Программа должна вывести «YES», если из первой клетки ходом короля можно попасть во вторую, 
или «NO» в противном случае.
#
Формат входных данных
На вход программе подаётся четыре числа от 1 до 8.
#
Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.
#
Примечание. Шахматный король ходит по горизонтали, вертикали и диагонали, но только на 1 клетку.
'''
'''
x1 = int(input())
x2 = int(input())
y1 = int(input())
y2 = int(input())

if (x1 >= x2 -1 and x1 <= x2 +1) and (y1 >= y2 -1 and y1 <= y2 +1):
    print('YES')
else:
    print('NO')
'''

x1 = int(input()) # первая точка
y1 = int(input()) # первая точка
x2 = int(input()) # вторая точка
y2 = int(input()) # вторая точка

if -1 <= x1-x2 <= 1 and -1 <= y1 - y2 <= 1: 
    print('YES')
else:
    print('NO')

# if (x1 and y1 >= x2 - 1) or (x1 and y1 <= x2 + 1) or (x1 and y1 >= y2 -1) or (x1 and y1 <= y2 +1) or (x1 and y1 >= (x2 + 1 and y2 + 1)) or (x1 and y1 <= (x2 - 1 and y2 - 1)) or (x1 or y1 >= (x2 -1 and y2 + 1)) or (x1 or y1 <= (x2 + 1 and y2 - 1)):
# Решил как(___or____or____)and(___or____or____)

'''
# едрить решение подсмотрел +_+:

a = int(input())
b = int(input())
a1 = int(input())
b1 = int(input())
if 1 <= a <= 8 and 1 <= b <= 8:
    if a == b == 1:
        if a1 == 2 and b1 == 1 or a1 == 2 and b1 == 2 or a1 == 1 and b1 == 2:
            print('YES')
        else: print('NO')
    elif a == 8 and b == 1:
        if a1 == 7 and b1 == 1 or a1 == 7 and b1 == 2 or a1 == 8 and b1 == 2:
            print('YES')
        else: print('NO')
    elif a == 1 and b == 8:
        if a1 == 1 and b1 == 7 or a1 == 2 and b1 == 8 or a1 == 2 and b1 == 7:
            print('YES')
        else: print('NO')            
    elif a == b == 8:
        if a1 == 7 and b1 == 8 or a1 == 8 and b1 == 7 or a1 == b1 == 7:
            print('YES')
        else: print('NO')
    elif 2 <= a <= 7 and b == 1:
        if a1 == a - 1 and b1 == b or a1 == a + 1 and b1 == b or a1 == a - 1 and b1 == b + 1 or a1 == a and b1 == b + 1 or a1 == a + 1 and b1 == b + 1:
            print('YES')
        else: print('NO')
    elif a == 1 and 2 <= b <= 7:
        if a1 == a and b1 == b - 1 or a1 == a and b1 == b + 1 or a1 == a + 1 and b1 == b - 1 or a1 == a + 1 and b1 == b or a1 == a + 1 and b1 == b + 1:
            print('YES')
        else: print('NO')
    elif 2 <= a <= 7 and b == 8:
        if a1 == a - 1 and b1 == b or a1 == a + 1 and b1 == b or a1 == a - 1 and b1 == b - 1 or a1 == a and b1 == b - 1 or a1 == a + 1 and b1 == b - 1:
            print('YES')
        else: print('NO')
    elif a == 8 and 2 <= b <= 7:
        if a1 == a and b1 == b - 1 or a1 == a and b1 == b + 1 or a1 == a - 1 and b1 == b - 1 or a1 == a - 1 and b1 == b or a1 == a - 1 and b1 == b + 1:
            print('YES')
        else: print('NO')    
    elif 2 <= a <= 7 and 2 <= b <= 7:
        if a - 1 <= a1 <= a + 1 and b - 1 <= b1 <= b + 1:
            print('YES')
        else: print('NO')                
else:
    print('NO')
'''