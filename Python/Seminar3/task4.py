# Напишите функцию to_dict(list), которая принимает аргумент в виде списка

def to_dict(list):
    return {element: element for element in list}

# Тесты 
print(to_dict([1, 2, 3, 4]))
print(to_dict(['grey', (2, 17), 3.11, -4]))
