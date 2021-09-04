'''
Три города
Даны названия трех городов. Напишите программу, которая определяет самое короткое и самое длинное название города.
#
Формат входных данных
На вход программе подаётся названия трех городов, каждое на отдельной строке.
#
Формат выходных данных
Программа должна вывести самое короткое и длинное название города, каждое на отдельной строке.
#
Примечание. Гарантируется, что длины названий всех трех городов различны.
'''
city1 = input()
city2 = input()
city3 = input()

# a = len(city1), len(city2), len(city3)
# print(min(a))
# print(max(a))

if len(city1) < len(city2) and len(city1) < len(city3):
    print(city1)
elif len(city2) < len(city1) and len(city2) < len(city3):
    print(city2)
elif len(city3) < len(city1) and len(city3) < len(city2):
    print(city3)

if len(city1) > len(city2) and len(city1) > len(city3):
    print(city1)
elif len(city2) > len(city1) and len(city2) > len(city3):
    print(city2)
elif len(city3) > len(city1) and len(city3) > len(city2):
    print(city3)