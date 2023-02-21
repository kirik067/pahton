# задача 34

# c = "пара-ра-рам рам-пам-папам па-ра-па-да"
# st = c.lower().split()
# f = lambda x: sum(1 for i in x if i in 'аеёиоуыэюя')
# t = f(st[0])
# if all([f(i) == t for i in st]):
#     print('Парам пам-пам')
# else:
#     print('Пам парам')




# задача 36


# def print_operation_table(operation, num_rows=6, num_columns=6):
#     for i in range(1, num_rows + 1):
#         answer = []
#         for j in range(1, num_columns + 1):
#             answer.append(str(operation(i, j)))
#         print(" ".join(answer))


# print_operation_table(lambda x, y: x * y)