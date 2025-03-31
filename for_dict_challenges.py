# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]
name_count={}
for student in students:
    name=student['first_name']
    name_count[name]=name_count.get(name,0)+1
for name, count in name_count.items():
    print(f'{name}: {count}')



# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]

name_count={}
for student in students:
    name=student['first_name']
    name_count[name]=name_count.get(name,0)+1
    name = next((name for name, count in name_count.items() if count == max(name_count.values())))
print(f'Самое распростаненное имя в классе: {name}')


# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]
for k, clas in enumerate(school_students, start=1):
    name_count={}
    for student in clas:
        name = student['first_name']
        name_count[name]=name_count.get(name,0)+1
        name = max(name_count, key=name_count.get)
    print(f'Самое распространенное имя в классе {k}: {name}')


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2в', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}
for clas in school:
    clas_name=clas['class']
    girls=0
    boys=0
    for student in clas['students']:
        name = student['first_name']
        if is_male[name]:
            boys+=1
        else:
            girls+=1
    print(f'Класс {clas_name}: девочек {girls}, мальчиков {boys}')


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}
class_count={}
for clas in school:
    class_name=clas['class']
    students=clas['students']
    class_count[class_name]={'boys': 0, 'girls':0}
    for student in students:
        name=student['first_name']
        if is_male[name]:
            class_count[class_name]['boys']+=1
        else:
            class_count[class_name]['girls']+=1
    max_boys=max(class_count, key=lambda x: class_count[x]['boys'])
    max_girls=max(class_count, key=lambda x: class_count[x]['girls'])
print(f'Больше всего мальчиков в классе {max_boys}')   
print(f'Больше всего мальчиков в классе {max_girls}') 