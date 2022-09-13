# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

# Пример:

# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

c = int(input('Введите число n: '))
result_list3 = list((1+1/i) **i for i in range(1, c + 1))
print(f'sum for = {round(sum(result_list3), 3)}')