'''
Напишите программу, в которой рассчитывается сумма и 
произведение цифр положительного трёхзначного числа.

Формат входных данных
На вход программе подаётся положительное трёхзначное число.

Формат выходных данных
Программа должна вывести два числа с поясняющим текстом: сумма цифр и произведение цифр.
'''
num = int(input())
first_digit = num // 100
last_digit = num % 10
second_digit = (num // 10) % 10
#print(first_digit, second_digit, last_digit)
summ = first_digit + last_digit + second_digit
proiz = first_digit * second_digit * last_digit
print('Сумма цифр = {}'.format(summ))
print('Произведение цифр = {}'.format(proiz))

