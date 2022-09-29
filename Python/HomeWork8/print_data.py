
def print_data(data):
    if len(data) > 0:
        print("Фамилия".center(20), "Имя".center(20), "Возраст".center(2), "Телефон".center(15),"Должность".center(10), "Зарплата".center(10))
        print("-"*107)
        for item in data:
            print(item[0].center(20), item[1].center(20), item[2].center(2), item[3].center(15), item[4].center(10), item[5].center(10))
    else:
        print("Пустая система!")