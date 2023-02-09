# задача 18
 
# numbers = int(input('Ввидите числа от 1 до 10'))
# a = [int(input("Ввисти число")) for i in range(numbers)]
# x = int(input("Заданное число"))

# minraz = (x - a[0])**2

# b = 0
# i = 0
# while i < len(a):
#     if (x-a[i])**2 <= minraz:
#         minraz = (x - a[i])**2
#     b = i
#     i += 1
# print(a)
# print(a[b])
# print(b)





# задача 16

# n = int(input())
# a = map(int, input().split())
# x = int(input())
# print(sum(map(lambda z: int(z ==x), a)))



# задача 20
# import re
# def isCrillic (text):
#     return bool(re.search('[а-яА-Я]', text))
# points_EN = {1:'AEIOULNSTR',
#                 2:'EF',
#                 3:'GH',
#                 4:'LKJH',
#                 5:'OIUY',
#                 8:'MNBV',
#                 10:'VCXZD'}
# points_RU = {1:'ГНЕКЕРИ',
#                 2:'ОГНЕК',
#                 3:'ЬТИМ',
#                 4:'ЯЧСМ',
#                 5:'ГНЕК',
#                 8:'УВАМИ',
#                 10:'ЪХЗЩ'}
# text = input().upper()
# if isCrillic(text):
#     print(sum([k for i in text for k, v in points_RU.items() if i in v]))
# else:
#     print(sum([k for i in text for k, v in points_EN.items() if i in v]))                