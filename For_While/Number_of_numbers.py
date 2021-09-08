'''
Количество чисел
На вход программе подаются два целых числа a и b(a≤b). 
Напишите программу, которая подсчитывает количество чисел в диапазоне от a до b включительно, куб которых оканчивается на 4 или 9.
#
Формат входных данных
На вход программе подаются два целых числа a и b(a≤b).
#
Формат выходных данных
Программа должна вывести одно целое число в соответствии с условием программы.
#
Примечание. Куб числа a – это его третья степень a^3.
'''
print('Input 2 numbers. Number "a" must be <= number "b":')
a = int(input())
b = int(input())

while a > b:
    print(f'Wrong numbers! You input {a} and {b}.\nPls fix it and input numbers again:')
    a = int(input())
    b = int(input())
    if a <= b:
        print('Nice numbers. Let\'s rock!')
        break

counter = 0
for i in range(a, b + 1):
    if i ** 3 % 10 == 4 or i ** 3 % 10 == 9:
        counter += 1
print(counter)