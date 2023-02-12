# задача 26

# def power (A, B):
#     if B == 0:
#         return 1
#     if B % 2 == 0:
#         return power(A, B//2)*power(A, B//2)

#     else:
#         return power (A, B-1)*A

# A = int(input("Введите число"))
# B = int (input("Введите степень числа"))
# print(power (A, B))



 # задача 28

# def sum(a, b):
#     if b == 0:
#         return
#     else:
#         if b > 0:
#             return sum(a + 1, b - 1)
#         else:
#             return sum(a - 1, b + 1)
# print(sum(a=int(input()), b=int(input())))