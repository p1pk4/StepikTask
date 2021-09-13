'''
Only even numbers 🌶️
Напишите программу, которая считывает последовательность из 10 целых чисел и определяет является ли каждое из них четным или нет.
#
Формат входных данных
На вход программе подаются 10 целых чисел, каждое на отдельной строке.
#
Формат выходных данных
Программа должна вывести строку «YES», если все числа четные и «NO» в ином случае.
'''


my_even_list = []
my_odd_list = []
for i in range(1, 11):
    num = int(input())
    if num % 2 != 0:
        my_odd_list.append(num)
    else:
        my_even_list.append(num)
if len(my_even_list) == 10:
    print('YES')
elif len(my_odd_list) >= 1:
    print('NO')