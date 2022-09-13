
# a = 'opopoopppooopppoopppppp'
# max = 0
# for i in range(len(a)):
#     count = 0
#     if a[i] == 'p':
#         count += 1
#         if count > max:
#             max = count
# print(max)

s = input()
t = 0
while "p"*(t + 1) in s:
    t += 1
if t!= 0:
    print(t)
else:
    print(0)
