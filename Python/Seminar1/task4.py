# Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа
# Пример:
# -6,78 -> 7
# - 5 -> нет
# -0,34 -> 3

num = float(input('Введите число:'))
number = num * 10
if int(number % 10) == 0:
    print('Нет')
else:
    print(int(number % 10))

