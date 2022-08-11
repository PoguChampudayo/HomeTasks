# Я работаю секретарем и мне постоянно приходят различные документы. Я должен быть очень внимателен чтобы не потерять ни один документ. Каталог документов хранится в следующем виде:

#       documents = [
#         {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
#         {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
#         {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
#       ]
# Перечень полок, на которых находятся документы хранится в следующем виде:

#       directories = {
#         '1': ['2207 876234', '11-2', '5455 028765'],
#         '2': ['10006'],
#         '3': []
#       }
# Задача №1
# Необходимо реализовать пользовательские команды, которые будут выполнять следующие функции:

# p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
# s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
# Правильно обработайте ситуации, когда пользователь будет вводить несуществующий документ.
# l– list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
# a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться. Корректно обработайте ситуацию, когда пользователь будет пытаться добавить документ на несуществующую полку.
# Внимание: p, s, l, a - это пользовательские команды, а не названия функций. Функции должны иметь выразительное название, передающие её действие.

# Задача №2. Дополнительная (не обязательная)
# d – delete – команда, которая спросит номер документа и удалит полностью документ из каталога и его номер из перечня полок. Предусмотрите сценарий, когда пользователь вводит несуществующий документ;
# m – move – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую. Корректно обработайте кейсы, когда пользователь пытается переместить несуществующий документ или переместить документ на несуществующую полку;
# as – add shelf – команда, которая спросит номер новой полки и добавит ее в перечень. Предусмотрите случай, когда пользователь добавляет полку, которая уже существует.;

from pprint import pprint

class Documents:
    documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
    ]
    directories = {
            '1': ['2207 876234', '11-2', '5455 028765'],
            '2': ['10006'],
            '3': []
    }

    def get_person_name(self, doc):
        #doc_number = input('Введите номер документа: ')
        for elem in self.documents:
            return elem["name"] if elem["number"] == doc else False
            break



# print(Documents.__dict__)
doc_number = "2207 876234" #input('Введите номер документа: ')
print(Documents.get_person_name(doc_number))

    # def __init__ (self, type, number, name):
    #     self.type = type
    #     self.number = number
    #     self.name = name
       # self.shelf = shelf
    

# class Shelf:

#     def __init__ (self, number, documents):
#         self.number = number
#         self.documents = documents

# gupkin_passport = Document("passport", "2207 876234", "Василий Гупкин")
# pokemonov_invoice = Document("invoice", "11-2", "Геннадий Покемонов")
# pavlov_insurance = Document("insurance", "10006", "Аристарх Павлов")
# shelf1 = Shelf(1, ['2207 876234', '11-2', '5455 028765'])
# shelf2 = Shelf(2, ['10006'])
# shelf3 = Shelf(3, [] )



# documents = [
#         {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
#         {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
#         {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
# ]
# directories = {
#         '1': ['2207 876234', '11-2', '5455 028765'],
#         '2': ['10006'],
#         '3': []
# }

# def get_person_name():
#   doc_number = input('Введите номер документа: ')
#   for i in range(len(documents)):
#     if doc_number in documents[i].values():
#       print("Имя: ", documents[i]["name"])
#       doc_exist = True
#       break
#     else:
#       doc_exist = False
#       #continue
#   if doc_exist == False:
#     print("Введен номер несуществующего документа")
# # get_person_name()  

# def get_shelf():
#   doc_number = input('Введите номер документа: ')
#   for key, value in directories.items():
#     if doc_number in value:
#       print("Номер полки: ", key)
#       doc_exist = True
#       break
#     else:
#       doc_exist = False
#   if doc_exist == False:
#     print("Введен номер несуществующего документа")

# #get_shelf()

# def get_docs_list():
#   for i, doc in enumerate(documents):
#     print(f" {doc['type']} \"{doc['number']}\" \"{doc['name']}\";")
   
# #get_docs_list()

# def add_new_doc():
#   new_doc_type = input('Введите тип документа: ')
#   new_doc_number = input('Введите номер документа: ')
#   new_doc_name = input('Введите имя: ')
#   new_doc_shelf = input('Введите номер полки: ')
#   shelves_list = ", ".join(directories.keys())
#   while new_doc_shelf not in directories.keys():
#     new_doc_shelf = input(f'Введен несуществующий номер полки (допустимые номера - {shelves_list}), \nПопробуйте еще раз: ')
#   new_record = {'type': new_doc_type, 'number': new_doc_number, 'name': new_doc_name}
#   documents.append(new_record)
#   directories[new_doc_shelf].append(new_doc_number)
#   pprint(documents)
#   pprint(directories)   

# def del_doc():
#   doc_number = input('Введите номер документа: ')
#   for i in range(len(documents)):
#     if doc_number in documents[i].values():
#       documents.pop(i)
#       for docs_list in directories.values():
#         if doc_number in  docs_list:
#           docs_list.remove(doc_number)
#           break
#       doc_exist = True
#       break
#     else:
#       doc_exist = False
#   if doc_exist == False:
#     print("Введен номер несуществующего документа")
#   pprint(documents)
#   pprint(directories) 

# def move_doc():
#   docs_list = [documents[i]['number'] for i, j in enumerate(documents)]
#   shelves_list = ", ".join(directories.keys())
#   doc_number = input('Введите номер документа: ')
#   # shelves_list = [*directories.keys()]
#   while doc_number not in docs_list:
#     doc_number = input('Введен несуществующий документ, еще раз: ')
#   doc_shelf = input('Введите номер полки, на которую перемещаем: ')
#   while doc_shelf not in directories.keys():
#     doc_shelf = input(f'Введен несуществующий номер полки (допустимые номера - {shelves_list}), \nПопробуйте еще раз: ')
#   for i in directories.values():
#     try:
#       i.remove(doc_number)
#     except:
#       pass
#   directories[doc_shelf].append(doc_number)
#   pprint(directories)   
