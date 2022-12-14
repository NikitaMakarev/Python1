# Напишите программу для обработки текста.
# На вход вашей программы подается многострочный текст, причем число строк заранее известно.
# Ваша задача пронумеровать слова в нем, начиная с нуля, а затем вывести только те слова, которые начинаются с большой буквы.
# Перед словом необходимо вывести номер первого вхождения этого слова в текст.
# Слова необходимо отсортировать в лексикографическом порядке. ( В решение задачи поможет функция enumerate())
# Входные данные
# Выходные данные
# Ехал Грека через реку.
# Видит Грека в реке рак.
# Рак за руку Греку цап.
# 4 - Видит
# 1- Грека
# 17 - Греку
# 0 - Ехал
# 14 - Рак
# 9 - Сунул 

a = []
for i in range(4):
    a.extend(input().replace('.', '').split())
b = list(enumerate(a))
sp = []
b.sort(key = lambda x: x[1])
for i in b:
    if i[1][0].isupper() and i[1] not in sp:
        print(*(i[0], '-', i[1]))
        sp.append(i[1])
        