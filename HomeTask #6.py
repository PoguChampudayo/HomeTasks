class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturers(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached: 
            if course in lecturer.rate_by_students.keys():
                lecturer.rate_by_students[course] += [grade]
            else:
                lecturer.rate_by_students[course] = [grade]
        else:
            message = f'Товарищ {lecturer.name} {lecturer.surname} не ведет такой предмет либо вы его не изучаете'
            return message

    def __str__(self):
        average_course_rate=[mean(v) for v in self.grades.values()]
        total_average_rate = round(mean(average_course_rate), 2)
        res = (f'\nИмя: {self.name}'
               f'\nФамилия: {self.surname}'
               f'\nСредняя оценка за лекции: {total_average_rate}'
               f'\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}'
               f'\nЗавершенные курсы: {", ".join(self.finished_courses)}')
        return res

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
   
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.rate_by_students = {}

    def __str__(self):
        average_course_rate=[mean(v) for v in self.rate_by_students.values()]
        total_average_rate = round(mean(average_course_rate), 2)
        res = (f'\nИмя: {self.name}'
               f'\nФамилия: {self.surname}'
               f'\nСредняя оценка за лекции: {total_average_rate}')
        return res

class Reviewer(Mentor):
    
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            message = f'Товарищ {student.name} {student.surname} не изучает такой предмет либо вы за ним не закреплены'
            return message
    
    def __str__(self):
        res = (f'\nИмя: {self.name}'
               f'\nФамилия: {self.surname}')
        return res

# для подсчета средней оценки за домашние задания по всем студентам в рамках конкретного курса (в качестве аргументов принимаем список студентов и название курса);
# для подсчета средней оценки за лекции всех лекторов в рамках курса (в качестве аргумента принимаем список лекторов и название курса).

def all_students_average_grade(students, course):
    grade_list = []
    for student in students:
        if course in student.grades.keys():
            grade_list += student.grades[course]
    res = f'\nСредняя оценка среди студентов по предмету {course}: {round(mean(grade_list), 2)}'
    return res

def all_lecturers_average_rate(lecturers, course):
    rate_list = []
    for lecturer in lecturers:
        if course in lecturer.rate_by_students.keys():
            rate_list += lecturer.rate_by_students[course]
    res = f'\nСредняя оценка среди лекторов по предмету {course}: {round(mean(rate_list), 2)}'
    return res


from statistics import mean

chemistry_lecturer = Lecturer("Walter", "White")
chemistry_lecturer.courses_attached += ["Chemistry", "Math"]

math_lecturer = Lecturer("Jonathan", "Bigelow")
math_lecturer.courses_attached += ["Math", "Physics"]

physics_lecturer = Lecturer("Hank", "Shreider")
physics_lecturer.courses_attached += ["Physics", "Chemistry"]

chemistry_reviewer = Reviewer("Karin", "Black")
chemistry_reviewer.courses_attached += ["Chemistry"]

math_reviewer = Reviewer("Anca", "Vass")
math_reviewer.courses_attached += ["Math"]

physics_reviewer = Reviewer("Robert", "Kiss")
physics_reviewer.courses_attached += ["Physics"]

student1 = Student("Robert", "Palmer", "male")
student1.courses_in_progress += ["Physics", "Chemistry", "Math"]
student1.finished_courses += ["Literature", "History"]
student2 = Student("Jessica", "Pao", "female")
student2.courses_in_progress += ["Physics", "Chemistry", "Math"]
student2.finished_courses += ["English"]
student3 = Student("Claudia", "Culda", "female")
student3.courses_in_progress += ["Physics", "Chemistry", "Math"]
student3.finished_courses += ["French", "Nature"]

student1.rate_lecturers(math_lecturer, "Math", 10)
student1.rate_lecturers(math_lecturer, "Physics", 9)
student1.rate_lecturers(chemistry_lecturer, "Chemistry", 10)
student1.rate_lecturers(chemistry_lecturer, "Math", 7)
student1.rate_lecturers(physics_lecturer, "Physics", 10)
student1.rate_lecturers(physics_lecturer, "Chemistry", 4)

student2.rate_lecturers(math_lecturer, "Math", 9)
student2.rate_lecturers(chemistry_lecturer, "Chemistry", 10)
student2.rate_lecturers(physics_lecturer, "Physics", 5)

student3.rate_lecturers(math_lecturer, "Math", 7)
student3.rate_lecturers(chemistry_lecturer, "Chemistry", 10)
student3.rate_lecturers(physics_lecturer, "Physics", 9)

chemistry_reviewer.rate_hw(student1, "Chemistry", 9)
chemistry_reviewer.rate_hw(student2, "Chemistry", 10)
chemistry_reviewer.rate_hw(student3, "Chemistry", 6)

physics_reviewer.rate_hw(student1, "Physics", 5)
physics_reviewer.rate_hw(student2, "Physics", 9)
physics_reviewer.rate_hw(student3, "Physics", 10)

math_reviewer.rate_hw(student1, "Math", 10)
math_reviewer.rate_hw(student2, "Math", 7)
math_reviewer.rate_hw(student3, "Math", 8)


# print(math_lecturer.rate_by_students)
# print(chemistry_lecturer.rate_by_students)
# print(physics_lecturer.rate_by_students)
# print(student1.grades)
# print(student2.grades)
# print(student3.grades)
print(math_reviewer)
print(math_lecturer)
print(student1)
print(student2)
print(student3)
print(all_students_average_grade([student1, student2, student3], "Math"))
print(all_students_average_grade([student1, student2, student3], "Physics"))
print(all_students_average_grade([student1, student2, student3], "Chemistry"))
#all_lecturers_average_rate([math_lecturer, physics_lecturer, chemistry_lecturer], "Math")
print(all_lecturers_average_rate([math_lecturer, physics_lecturer, chemistry_lecturer], "Math"))
print(all_lecturers_average_rate([math_lecturer, physics_lecturer, chemistry_lecturer], "Physics"))
print(all_lecturers_average_rate([math_lecturer, physics_lecturer, chemistry_lecturer], "Chemistry"))

# best_student = Student('Ruoy', 'Eman', 'your_gender')
# best_student.courses_in_progress += ['Python']
 
# cool_mentor = Mentor('Some', 'Buddy')
# cool_mentor.courses_attached += ['Python']
 
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
 
# print(best_student.grades)


# Домашнее задание к лекции «Объекты и классы. Инкапсуляция, наследование и полиморфизм»
# ​Привет! Домашняя работа по данной теме является продолжением квиза к предыдущей лекции. 
# Мы продолжим реализовывать логику функционала учебной группы в парадигме ООП. Удачи!

# Задание № 1. Наследование
# Исходя из квиза к предыдущему занятию, у нас уже есть класс преподавателей и класс студентов
#  (вы можете взять этот код за основу или написать свой). Студентов пока оставим без изменения,
#  а вот преподаватели бывают разные, поэтому теперь класс Mentor должен стать родительским классом,
#  а от него нужно реализовать наследование классов Lecturer (лекторы) и Reviewer (эксперты, 
# проверяющие домашние задания). Очевидно, имя, фамилия и список закрепленных курсов логично 
# реализовать на уровне родительского класса. А чем же будут специфичны дочерние классы? Об этом в следующих заданиях.

# Задание № 2. Атрибуты и взаимодействие классов.
# В квизе к предыдущей лекции мы реализовали возможность выставлять студентам оценки за домашние задания. 
# Теперь это могут делать только Reviewer (реализуйте такой метод)! А что могут делать лекторы? 
# Получать оценки за лекции от студентов :) Реализуйте метод выставления оценок лекторам у класса Student 
# (оценки по 10-балльной шкале, хранятся в атрибуте-словаре у Lecturer, в котором ключи – названия курсов, 
# а значения – списки оценок). Лектор при этом должен быть закреплен за тем курсом, на который записан студент.

# Задание № 3. Полиморфизм и магические методы
# Перегрузите магический метод __str__ у всех классов.

# У проверяющих он должен выводить информацию в следующем виде:
# print(some_reviewer)
# Имя: Some
# Фамилия: Buddy

# У лекторов:
# print(some_lecturer)
# Имя: Some
# Фамилия: Buddy
# Средняя оценка за лекции: 9.9

# А у студентов так:
# print(some_student)
# Имя: Ruoy
# Фамилия: Eman
# Средняя оценка за домашние задания: 9.9
# Курсы в процессе изучения: Python, Git
# Завершенные курсы: Введение в программирование

# Реализуйте возможность сравнивать (через операторы сравнения) между собой лекторов по средней оценке за лекции и студентов по средней оценке за домашние задания.

# Задание № 4. Полевые испытания
# Создайте по 2 экземпляра каждого класса, вызовите все созданные методы, а также реализуйте две функции:
# для подсчета средней оценки за домашние задания по всем студентам в рамках конкретного курса (в качестве аргументов принимаем список студентов и название курса);
# для подсчета средней оценки за лекции всех лекторов в рамках курса (в качестве аргумента принимаем список лекторов и название курса).