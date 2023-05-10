surname_students = input('Your surname: ').title()
students_list = []
for result in surname_students:
    students_list = surname_students.split()
    students_list.sort()
print('Surnames of students:', students_list)
