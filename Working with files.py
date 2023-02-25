# задача 1

# def read_last(lines, file):
#     if lines > 0:
#         with open(file, encoding='utf-8') as text:
#             file_lines = text.readlines()[-lines:]
#         for line in file_lines:
#             print(line.strip())
#         else:
#             print('Количество строк может быть только целым положительным')


# read_last(3, 'article.txt')
# read_last(-5, 'article.txt')


# задача 1,1


# def longest_words(file):
#     with open(file, "r") as text:
#         words = text.read().split()
#         max_length = len(max(words, key=len))
#         sought_words = [word for word in words if len(word) == max_length]
#         with open("result.txt", mode="a") as file:
#             file.write(' '.join(sought_words)+"\n")

# longest_words("article.txt")