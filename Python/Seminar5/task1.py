# Объявите анонимную (лямбда) функцию для определения вхождения в переданную ей строку фрагмента "plr".
# То есть, функция должна возвращать True, если такой фрагмент присутствует в строке и False - в противном случае.

# str1 = 'alibaba'
# str2 = 'li'
# print(str2 in str1)
# bl = lambda x: str1 in str2
# print(bl)

countains = lambda s, sample = 'ra' : sample in s
s = input()
print(countains(s))