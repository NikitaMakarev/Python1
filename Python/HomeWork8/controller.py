from import_data import import_data
from export_data import export_data
from print_data import print_data
from search_data import search_data

def greeting():
    print("Здравствуйте!")

def input_data():
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    age = input("Введите возраст: ")
    phone_number = input("Введите телефон: ")
    position = input("Введите должность: ")
    income = input("Введите зарплату: ")
    return[last_name, first_name, age, phone_number, position, income]

def choice_sep():
    sep = input("Введите разделитель: ")
    if sep == "":
        sep = None
    return sep

def choice():
    print( "Что делаем:\n\
    1 - импорт;\n\
    2 - экспорт;\n\
    3 - поиск человека.")
    ch = input("Введите цифру: ")
    if ch == '1':
        sep = choice_sep()
        import_data(input_data(), sep)
    elif ch == '2':
        data = export_data()
        print_data(data)
    else:
        word = input("Введите данные для поиска: ")
        data = export_data()
        item = search_data(word, data)
        if item != None:
            print("Фамилия".center(20), "Имя".center(20), "Возраст".center(2), "Телефон".center(15),"Должность".center(10), "Зарплата".center(10))
            print("-"*107)
            print(item[0].center(20), item[1].center(20), item[2].center(2), item[3].center(15), item[4].center(10), item[5].center(10))
        else:
            print("Данные не обнаружены")
