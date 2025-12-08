# This application prints text based on the data in the list

students = ['Ivanov', 'Petrov', 'Sidorov']

subjects = ['math', 'biology', 'geography']

list_students = ', '.join(students)

list_subjects = ', '.join(subjects)

print(f'Students {list_students} study these subjects: {list_subjects}')
