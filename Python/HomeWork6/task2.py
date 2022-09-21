# Напишите программу, удаляющую из текста все слова, содержащие "абв".


list = "абв"
string = "Без труда абв не выловишь абв и рыбку из пруда.."
split_str = string.split()
filtered_str = ' '.join((filter(lambda s: s not in list, split_str)))
print("Отфильтрованная строка:", filtered_str)