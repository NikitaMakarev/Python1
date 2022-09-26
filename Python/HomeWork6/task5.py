# Задайте список из n чисел последовательности и выведите на экран их сумму.

def seq(n: int) -> float:
    li = [i for i in range(1, n +1)]
    sum_sq = sum((map(lambda x: (1 + 1/x)**x, li)))
    return sum_sq

print(round(seq(6), 2))