
#  Задача 24


# a = list(map(int, input('Ввидите количество урожая через пробел').split()))

# maxsum = 0
# for i in range(3):
# 	cursum = sum(a[i:i+3])
# 	if cursum > maxsum:
# 		maxsum = cursum
# if a[0] + a[-1] + a[-2] > maxsum:
# 	maxsum = a[0] + a[-1] + a[-2]
# if a[0] + a[1] + a[-1] > maxsum:
# 	maxsum = a[0] + a[1] + a[-1]
# print(maxsum)

# задача 24

# n = int(input("Ввидите количество первого множества"))
# m = int(input("Ввидите количество второго множества"))
# new_list = list(range(1, n+1))
# New_list2= list(range(1, m+1))
# arr = [i for i in new_list if i % 2 == 0]
# arr1 = [i for i in New_list2 if i % 2 == 0]

# print(arr1, arr)
