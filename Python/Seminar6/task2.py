# Дан список, вывести отдельно буквы и цифры.
# a = ( "a", 'b', '2', '3' ,'c')
# b = ( 'a' , 'b' , 'c')
# c = ( '1', '2', '3')

from curses.ascii import isalpha, isdigit


lst =["a", 'b', '2', '3' ,'c']
number = list(filter(lambda x: x.isdigit(), lst))
word =  list(filter(lambda x: x.isalpha(), lst))
print(number, word)

# isdigit - поиск числа.
# isalpha - поиск буквы.