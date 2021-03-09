tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
classes = ['9А', '7В', '9Б', '9В', '8Б', '10А']


def get_tuple(tutors_def, classes_def):
    for i in range(len(tutors_def)):
        yield tutors_def[i], (None if i >= len(classes_def) else classes_def[i])


classes_tutors = get_tuple(tutors, classes)
print(type(classes_tutors))
for el in classes_tutors:
    print(el)
