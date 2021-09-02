'''
Дано трехзначное число {abc}, в котором все цифры различны. 
Напишите программу, которая выводит шесть чисел, образованных при перестановке цифр заданного числа.

Формат входных данных
На вход программе подаётся положительное трёхзначное целое число, все цифры которого различны.

Формат выходных данных
Программа должна вывести шесть чисел, образованных при перестановке цифр заданного числа
 в следующем порядке: abc, \, acb, \, bac, \, bca, \, cab, \, cba.
'''

num = int(input())
first_digit = num // 100 # первое число
third_digit = num % 10 # третье число
second_digit = (num // 10) % 10 # второе число
print('{}{}{}'.format(first_digit, second_digit, third_digit))
print('{}{}{}'.format(first_digit, third_digit, second_digit))
print('{}{}{}'.format(second_digit, first_digit, third_digit))
print('{}{}{}'.format(second_digit, third_digit, first_digit))
print('{}{}{}'.format(third_digit, first_digit, second_digit))
print('{}{}{}'.format(third_digit, second_digit, first_digit))