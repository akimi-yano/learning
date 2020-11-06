# total = 0
# for num in range(101):
#     # print(num, 100-num)
#     total += num
# print(total)
'''
you cannot add 50 + 50 middle
so its ...49+51 + 50
so itas 5000 + 50 because its even without 0
'''
total = 0
for num in range(1, 5):
    # print(num, 100-num)
    total += num
# 1, 2, 3, 4
# N = 4
# 1+4 = 5
# 2+3 = 5
# (n+1) * n/2
print(total)

total = 0
for num in range(1, 6):
    # print(num, 100-num)
    total += num
# 1, 2, 3, 4, 5
# N = 5
# 1+5 = 6
# 2+4 = 6
# 3 
# (n+1) * (n-1)/2 + (n+1)/2
# (n+1) * n/2
print(total)

# you need to pip install and import before using pyperclip 
# pyperclip.copy()
# pyperclip.paste()

# print('Hello', end = '')
# print('World')