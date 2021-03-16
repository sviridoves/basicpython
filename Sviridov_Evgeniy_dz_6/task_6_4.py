def parsed_files(users_file, hobby_file):
    with open(users_file) as users, open(hobby_file) as hobby:
        fio = tuple(users.readline().strip().split(','))
        hobby_tmp = (hobby.readline().strip().split(','))
        while fio[0] != '':
            if hobby_tmp[0] == '':
                hobby_tmp = None
            yield fio, hobby_tmp
            fio = tuple(users.readline().strip().split(','))
            hobby_tmp = (hobby.readline().strip().split(','))


users_hobby = {fio: hobby for fio, hobby in parsed_files('users.csv', 'hobby.csv')}
print(users_hobby)
