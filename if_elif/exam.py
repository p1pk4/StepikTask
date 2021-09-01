
# Task 1
'''
Напишите программу, которая определяет, оканчивается ли год с данным номером на два нуля. 
Если год оканчивается, то выведите «YES», иначе выведите «NO».
#
Формат входных данных
На вход программе подаётся натуральное число.
#
Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.
#
num = int(input())
if num % 100 == 0:
    print('YES')
else:
    print('NO')
'''

# Task 2
# https://ucarecdn.com/552441a7-7c02-47b4-9338-c9264f6c1b14/ - доска
'''
Заданы две клетки шахматной доски. Напишите программу, которая определяет имеют ли указанные клетки один цвет или нет. 
Если они покрашены в один цвет, то выведите слово «YES», а если в разные цвета — то «NO».
#
Формат входных данных
На вход программе подаётся четыре числа от 1 до 8 каждое, задающие номер столбца и номер строки сначала для первой клетки, 
потом для второй клетки.
#
Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.
#
# Номер столбца и Номер стороки для первой клетки
x1 = int(input())
y1 = int(input())
# Номер столбца и Номер стороки для второй клетки
x2 = int(input())
y2 = int(input())

if (x1 + y1 + x2 + y2) % 2 == 0:
    print('YES')
else:
    print("NO")
'''

# Task 3
'''
Girls only
Футбольная команда набирает девочек от 10 до 15 лет включительно. 
Напишите программу, которая запрашивает возраст и пол претендента, 
используя обозначение пола буквы m (от male – мужчина) и f (от female – женщина) 
и определяет подходит ли претендент для вступления в команду или нет. Если претендент подходит, 
то выведите «YES», иначе выведите «NO».
#
Формат входных данных
На вход программе подаётся натуральное число – возраст претендента и буква обозначающая пол m (мужчина) или f (женщина).
#
Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.
#
age = int(input())
gender = input()

if 10 <= age <= 15:
    if gender == 'f':
        print('YES')
    else:
        print('NO')
else:
    print('NO') 
'''

# Task 4
'''
Римские цифры
Напишите программу, которая считывает целое число и выводит соответствующую ему римскую цифру. 
Если число находится вне диапазона 1-10, то программа должна вывести текст «ошибка».
#
В таблице приведены римские цифры для чисел от 1 до 10.
#
num = int(input())
if num >= 1 and num <= 10:
    if num == 1:
        print('I')
    if num == 2:
        print('II')
    if num == 3:
        print('III')
    if num == 4:
        print('IV')
    if num == 5:
        print('V')
    if num == 6:
        print('VI')
    if num == 7:
        print('VII')
    if num == 8:
        print('VIII')
    if num == 9:
        print('IX')
    if num == 10:
        print('X')
else:
    print('ошибка')
'''

# Task 5
'''
YES or NO вот в чем вопрос
Напишите программу, которая принимает на вход число и в зависимости от условий выводит текст «YES», либо «NO».
#
Условия:

если число нечётное, то вывести «YES»;
если число чётное в диапазоне от 2 до 5 (включительно), то вывести «NO»;
если число чётное в диапазоне от 6 до 20 (включительно), то вывести «YES»;
если число чётное и больше 20, то вывести «NO».
#
Формат входных данных
На вход программе подаётся натуральное число.
#
Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.
#
num = int(input())
if num % 2 == 0:
    if num >= 2 and num <= 5:
        print('NO')
    elif num >= 6 and num <= 20:
        print('YES')
    elif num > 20:
        print('NO')
else:
    print('YES')
'''

# Task 6
'''
Ход слона 🌶️
Даны две различные клетки шахматной доски. Напишите программу, которая определяет, 
может ли слон попасть с первой клетки на вторую одним ходом. 
Программа получает на вход четыре числа от 1 до 8 каждое, задающие номер столбца и номер строки сначала для первой клетки, 
потом для второй клетки. 
Программа должна вывести «YES», если из первой клетки ходом слона можно попасть во вторую или «NO» в противном случае.
#
Формат входных данных
На вход программе подаётся четыре числа от 1 до 8.
#
Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.
#
Примечание. Шахматный слон ходит по диагоналям.

# Номер столбца и Номер стороки для первой клетки
x1 = int(input())
y1 = int(input())
# Номер столбца и Номер стороки для второй клетки
x2 = int(input())
y2 = int(input())

if (x1 - y1 == x2 - y2) or (x1 + y1 == x2 + y2):
    print('YES')
else:
    print('NO')
'''

# Task 7
'''
Ход коня
Даны две различные клетки шахматной доски. 
Напишите программу,  которая определяет, может ли конь попасть с первой клетки на вторую одним ходом. 
Программа получает на вход четыре числа от 1 до 8 каждое, задающие номер столбца и номер строки сначала для первой клетки, 
потом для второй клетки. Программа должна вывести «YES», 
если из первой клетки ходом коня можно попасть во вторую или «NO» в противном случае.
#
Формат входных данных
На вход программе подаётся четыре числа от 1 до 8.
#
Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.
#
Примечание. Шахматный конь ходит буквой «Г».

# Номер столбца и Номер стороки для первой клетки
x1 = int(input())
y1 = int(input())
# Номер столбца и Номер стороки для второй клетки
x2 = int(input())
y2 = int(input())
if (x1 - x2) * (y1 - y2) == 2 or (x1 - x2) * (y1 - y2) == -2:
    print('YES')
else:
    print('NO')
'''

# Task 8
'''
Ход ферзя
Даны две различные клетки шахматной доски. 
Напишите программу,  которая определяет, может ли ферзь попасть с первой клетки на вторую одним ходом. 
Программа получает на вход четыре числа от 1 до 8 каждое, 
задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки. 
Программа должна вывести «YES», если из первой клетки ходом ферзя можно попасть во вторую или «NO» в противном случае.
#
Формат входных данных
На вход программе подаётся четыре числа от 1 до 8.
#
Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.
#
Примечание. Шахматный ферзь ходит по диагонали, горизонтали или вертикали.
'''
# Номер столбца и Номер стороки для первой клетки
x1 = int(input())
y1 = int(input())
# Номер столбца и Номер стороки для второй клетки
x2 = int(input())
y2 = int(input())

if ((x1 - y1 == x2 - y2) or (x1 + y1 == x2 + y2)) or ((x1 != x2 and y1 == y2) or (y1 != y2 and x1 == x2)):
    print('YES')
else:
    print('NO')
