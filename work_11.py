from pprint import pprint
student = {
    'Іван Петров': {
        'Пошта': 'Ivan@gmail.com',
        'Вік': 14,
        'Номер телефону': '+380987771221',
        'Середній бал': 95.8
    },
    'Женя Курич': {
        'Пошта': 'Geka@gmail.com',
        'Вік': 16,
        'Номер телефону': None,
        'Середній бал': 64.5
    },
    'Маша Кера': {
        'Пошта': 'Masha@gmail.com',
        'Вік': 18,
        'Номер телефону': '+380986671221',
        'Середній бал': 80
    },

}
add_student = {
    'Грицай Влад': {
        'Пошта': 'vlad.gad@gmail.com',
        'Вік': 25,
        'Номер телефону': '+38062716547',
        'Середній бал': 91
    }
    }
all_student = {**student, **add_student}
average_score = 0
number_of_students = len(all_student)
for value in all_student:
    if all_student[value]['Номер телефону'] == None:
        all_student[value]['Номер телефону'] = '102'
    if all_student[value]['Середній бал'] > 90:
        pprint(f" {value} Середній бал {all_student[value]['Середній бал']} ")
    average_score += all_student[value]['Середній бал'] / number_of_students
pprint(average_score)
