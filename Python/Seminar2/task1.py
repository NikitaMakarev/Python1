list = ['222anton456', 'a1n1t1o1n1', '0000a0000n00t00000o000000n', 'gylfole', 'richard', 'ant0n']
print(list)
x = 'антон'
for i in list:
    if 'a' in i:
        if 'n' in i:
            if 't' in i:
                if 'o' in i:
                    if 'n' in i:
                        print(list.index(i) + 1)

# Второй способ
# n = int(input())
# list1 =[]
# for i in range(n):
#     a = input()
#     if 'a' in a:
#         a = a[a.find('a'):]
#         if 'n' in a:
#             a = a[a.find('n'):]
#             if 't' in a:
#                 a = a[a.find('t'):]
#                 if 'o' in a:
#                     a = a[a.find('o'):]
#                     if 'n' in a:
#                         list.append(i + 1)
# print(*list1)