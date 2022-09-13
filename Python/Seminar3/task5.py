# Задайте список. Напишите программу, которая определит, 
# присутствует ли в заданном списке строк некое число

strings = ["1", "another string", "string 3", "hello world", "123"]
x = input('Введите число: ')
if x in strings:
    print('Есть')
else:
    print('Нет')

