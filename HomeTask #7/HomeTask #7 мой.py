def split_recipes_to_files():   
    with open('support_files/recipes.txt', 'r', encoding = 'utf-8') as file:
        recipe = []
        for line in file:
            if line != "\n":
                recipe.append(line)
            else:
                dish_name = recipe[0].strip("\n")
                new_recipe = f'support_files/recipes/{dish_name}.txt'
                with open(new_recipe, 'w', encoding = 'utf-8') as new_file:
                    new_file.writelines(recipe)
                recipe = []
        dish_name = recipe[0].strip("\n")
        new_recipe = f'support_files/recipes/{dish_name}.txt'
        with open(new_recipe, 'w', encoding = 'utf-8') as new_file:
            new_file.writelines(recipe)

# split_recipes_to_files()

def get_recipe_from_file(filename):
    filepath = f'support_files/recipes/{filename}.txt'
    with open(filepath, 'rt', encoding = 'utf-8') as file:
        recipe = []
        for line in file:
            if "|" in line:
                line = line.strip("\n")
                data = line.split(" | ")
                recipe.append({'ingredient_name': data[0],
                        'quantity': int(data[1]),
                        'measure': data[2]})
    return recipe

class Dish:

    def __init__(self, name, recipe) -> None:
        self.name = name
        self.recipe = recipe

    # def get_recipe_from_file(self):
    #     filepath = f'support_files/recipes/{self.name}.txt'
    #     with open(filepath, 'rt', encoding = 'utf-8') as file:
    #         for line in file:
    #             if "|" in line:
    #                 line = line.strip("\n")
    #                 data = line.split(" | ")
    #                 self.recipe.append({'ingredient_name': data[0],
    #                         'quantity': int(data[1]),
    #                         'measure': data[2]})
       

omelet = Dish("Омлет", get_recipe_from_file("Омлет"))
# omelet.get_recipe_from_file()
# china_duck = Dish("Утка по-пекински")
# china_duck.get_recipe_from_file()
print(omelet.recipe)

# Список рецептов должен храниться в отдельном файле в следующем формате:

# Название блюда
# Количество ингредиентов в блюде
# Название ингредиента | Количество | Единица измерения
# Название ингредиента | Количество | Единица измерения
# ...
# Пример(файл в папке files):

# Омлет
# 3
# Яйцо | 2 | шт
# Молоко | 100 | мл
# Помидор | 2 | шт

# Утка по-пекински
# 4
# Утка | 1 | шт
# Вода | 2 | л
# Мед | 3 | ст.л
# Соевый соус | 60 | мл

# Запеченный картофель
# 3
# Картофель | 1 | кг
# Чеснок | 3 | зубч
# Сыр гауда | 100 | г

# Фахитос
# 5
# Говядина | 500 | г
# Перец сладкий | 1 | шт
# Лаваш | 2 | шт
# Винный уксус | 1 | ст.л
# Помидор | 2 | шт

# В одном файле может быть произвольное количество блюд.
# Читать список рецептов из этого файла.
# Соблюдайте кодстайл, разбивайте новую логику на функции и не используйте глобальных переменных.

# Задача №1
# Должен получится следующий словарь

# cook_book = {
#   'Омлет': [
#     {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
#     {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
#     {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
#     ],
#   'Утка по-пекински': [
#     {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
#     {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
#     {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
#     {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
#     ],
#   'Запеченный картофель': [
#     {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
#     {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
#     {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
#     ]
#   }

# Задача №2
# Нужно написать функцию, которая на вход принимает список блюд из cook_book и количество персон для кого мы будем готовить

# get_shop_list_by_dishes(dishes, person_count)
# На выходе мы должны получить словарь с названием ингредиентов и его количества для блюда. Например, для такого вызова

# get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
# Должен быть следующий результат:

# {
#   'Картофель': {'measure': 'кг', 'quantity': 2},
#   'Молоко': {'measure': 'мл', 'quantity': 200},
#   'Помидор': {'measure': 'шт', 'quantity': 4},
#   'Сыр гауда': {'measure': 'г', 'quantity': 200},
#   'Яйцо': {'measure': 'шт', 'quantity': 4},
#   'Чеснок': {'measure': 'зубч', 'quantity': 6}
# }
# Обратите внимание, что ингредиенты могут повторяться