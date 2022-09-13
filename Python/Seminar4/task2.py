# Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число. 
# В качестве символа - разделителя используйте пробел.

n = ' 3 5 7 9 2 5'
min = int(n[0])
max = int(n[0])
for i in n.split(sep = ' '):
    if int(i) < min:
        min = int(i)
    if int(i) > max:
        max = int(i)
print(min, max)

# Второе решение

# str = '12 40 0 15'
# lst = [int(i) for i in str.split()]
# print(min(lst))
# print(max(lst))