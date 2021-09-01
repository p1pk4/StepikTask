'''
Пересечение отрезков 🌶️🌶️
#
На числовой прямой даны два отрезка: [a_1; b_1] и [a_2; b_2]. Напишите программу, которая находит их пересечение.
#
Пересечением двух отрезков может быть:
отрезок;
точка;
пустое множество.
#
Формат входных данных
На вход программе подаются 4 целых числа a_1, b_1, a_2, b_2, каждое на отдельной строке. 
Гарантируется, что a_1 < b_1 и a_2 < b_2.
#
Формат выходных данных
Программа должна вывести на экран границы отрезка, являющегося пересечением, либо общую точку, либо текст «пустое множество».
'''
'''
a1 = int(input()) # a1 < b1
b1 = int(input())
a2 = int(input()) # a2 < b2
b2 = int(input())

if b1 < a2 or b2 < a1:
    print('пустое множество')
elif b1 == a2:
    print(b1)
elif b2 == a1:
    print(a1)
elif a1 <= a2 < b1 < b2:
    print(a2, b1)
elif a2 <= a1 < b1:
    print(a1, b2)
elif a2 < a1 < b1 <= b2:
    print(a1, b1)
elif a1 < a2 < b2 <= b1:
    print(a2, b2)
elif a1 == a2 and b1 == b2:
    print(a1, b1)

'''
a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())

# если концы разные, и начало одного в середине второго
if b2 > b1 and (a1 < a2 < b1):
        print(a2, b1)
elif (b1 > b2) and (a2 < a1 < b2):
        print(a1, b2)

# если концы равны:
elif b2 == b1 and (a1 < a2 < b1):
    print(a2, b1)
elif b2 == b1 and (a2 < a1 < b2):
    print(a1,b1)
# если начала равны:
elif a1 == a2 and (a1 < b1 < b2):
    print(a1, b1)
elif a1 == a2 and (a1 < b2 < b1):
    print(a1, b2)

# если один отрезок внутри другого:
elif a1 < a2 and (a2<b2<b1):
    print(a2, b2)
elif a2 < a1 and (a1<b1<b2):
    print(a1,b1)

# если отрезки равны:
elif a1==a2 and b2==b1:
    print(a1,b1)

# если пересечений нет
elif (a1>a2 and (b2<a1<b1)) or (a2>a1 and (b1<a2<b2)):
    print('пустое множество')

# если точка пересечения только одна:
elif a1<a2 and b1==a2:
    print(b1)
elif (a2<a1) and b2==a1:
    print(b2)