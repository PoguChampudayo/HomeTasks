class Square:

    def __init__(self, side):
        self.side = side
    
    def calculate_area(self, side):
        return side ** 2

    def calculate_perimeter(self, side):
        return side * 4

class Rectangle:
    
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self, length, width):
        return length * width

    def calculate_perimeter(self):
        return (length + width) * 2      

side = 3
length = 3
width = 4

my_sqare = Square(side)
my_rectangle = Rectangle(length, width)

print(my_sqare.calculate_perimeter(side))
print(my_sqare.calculate_area(side))
print(my_rectangle.calculate_perimeter(length, width))
print(my_rectangle.calculate_area(length, width))


# Задача №1

# Квадрат и прямоугольник.

# Пользователь вводит длину и ширину фигуры.
# Программа выводит их периметр и площадь.

# Пример:

# Введите длину стороны квадрата: 3

# Вывод:
# Периметр: 12
# Площадь: 9

# Введите длину прямоугольника: 3
# Введите ширину прямоугольника: 4

# Вывод:
# Периметр: 14
# Площадь: 12

# Программа запрашивает у пользователя длину стороны квадрата и выводит его периметр и площадь. Сразу после этого пользователю предлагается ввести длину и ширину прямоугольника, для которого рассчитывается периметр и площадь. Обратите внимание, что программа должна работать корректно при любых введённых значениях длины и ширины фигуры.