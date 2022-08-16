# # # f = open('data.txt', encoding = 'utf-8')
# # # print(type(f))

# # # # content = f.read()
# # # # print(type(content))
# # # # print(content)

# # # # line1 = f.readline()
# # # # line2 = f.readline()
# # # # line3 = f.readline()
# # # # print(line1)
# # # # print(line3)

# # # # content = f.readlines()
# # # # print(type(content))
# # # # print(content)

# # content = f.read()
# # f.seek(0)
# # content2 = f.read()
# # print(content2)


# # # f.close()

# # with open('data.txt', encoding = 'utf-8') as f:
# #     content = f.readlines()
# #     print(content[-1])

# # with open('data.txt', 'rt', encoding = 'utf-8') as f:
# #     # content = f.readlines()
# #     # for line in content:
# #     for line in f:
# #         data = line.split(" | ")
# #         print(data)

# считываем данные в словарь
# with open('data.txt', 'rt', encoding = 'utf-8') as f:
#     result = []
#     for line in f:
#         data = line.split(" | ")
#         result.append({'name': data[0],
#                     'stock': data[1],
#                     'price': data[2]})
# print(result)

# запись в файл
# w (write) - перезапись
# a (append) - дозапись
# х (exclusive) - запись в новый файл

# with open('test.txt', 'w', encoding = 'utf-8') as file:
#     # file.write('World\n')
#     # file.write('Привет')
#     file.writelines(['String1\n', 'String2\n'])

# with open('test.txt', 'a', encoding = 'utf-8') as file:
#     # file.write('World\n')
#     # file.write('Привет')
#     file.writelines(['String3\n', 'String4\n'])


# with open('test2.txt', 'x', encoding = 'utf-8') as file:
#     # file.write('World\n')
#     # file.write('Привет')
#     file.writelines(['String3\n', 'String4\n'])

# чтение и запись (добавляем +):
# with open('test.txt', 'a+', encoding = 'utf-8') as file:
#     file.seek(0) # перетаскиваем указатель в начало
#     content = file.read()
#     print(content)
#     file.write('String5\n')

# with open('test.txt', 'a+', encoding = 'utf-8') as file:
#     file.seek(0) # перетаскиваем указатель в начало
#     content = file.read()
#     print(content)
#     file.write('String5\n')

# with open('test2.txt', 'w+', encoding = 'utf-8') as file:
#     file.write('Hello world')
#     file.seek(0)
#     content = file.read()
#     print(content)

# with open('test2.txt', 'a', encoding = 'utf-8') as file:
#     print(file.readable())
#     print(file.writable())

# относительный путь
# with open('folder1/file1.txt', 'r', encoding = 'utf-8') as file:
#     content = file.read()
#     print(content)

# абсолютный путь для Windows (r подавляет символы переноса строк и т.д. (знаки экранирования, сырые строки (row strings))
# with open(r'C:\Users\YGordeyeva\OneDrive - Emerson\Documents\Python Projects\HomeTasks\folder1\file1.txt', 'r', encoding = 'utf-8') as file:
#     content = file.read()
#     print(content)

# # сбор пути программным спсосбом

# import os

# BASE_DIR = os.getcwd()
# FOLDER_NAME = 'folder1'
# FILE_NAME = 'file1.txt'

# full_path = f'{BASE_DIR}/{FOLDER_NAME}/{FILE_NAME}'
# full_path1 = os.path.join(BASE_DIR, FOLDER_NAME, FILE_NAME)

# print(full_path)
# print(full_path1)

# with open(full_path, 'r') as file:
#     content = file.read()
#     print(content)

# with open(full_path1, 'r') as file:
#     content = file.read()
#     print(content)