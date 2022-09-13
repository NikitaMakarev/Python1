# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.


numbers = [1, 1, 2, 3, 3, 4, 8, 9]

def unique_numbers(numbers):
    unique = []

    for number in numbers:
        if number in unique:
            continue
        else:
            unique.append(number)
    return unique

print(unique_numbers(numbers))

# Второй способ

# numbers = [1, 2, 2, 3, 3, 4, 5]
# unique_numbers = list(set(numbers))
# print(unique_numbers)

# set - включает только уникальные элементы.