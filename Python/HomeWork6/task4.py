# Напиите программу, которая принимает на 
# вход вещественное число и показывает сумму его цифр.
#6782 -> 23
# 0,56 -> 11

def sum_num(num: str) -> int:
    return sum(map(int, filter(lambda i: i.isdigit(), str(num))))

print(sum_num(6782))
print(sum_num(0,56))