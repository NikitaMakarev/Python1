# 1.Вводится список целых чисел в одну строчку через пробел. 
# Необходимо оставить в нем только двузначные числа. 
# Реализовать программу с использованием функции filter. 
# Результат отобразить на экране в виде последовательности оставшихся чисел в одну строчку через пробел.
# пример - 8 11 0 -23 140 1 => 11 -23

lst = [1, 3, 20, 44, 5, 16, 89]
print(list(filter(lambda x: 9 < abs(x) < 100, lst)))

# abs - модуль числа.