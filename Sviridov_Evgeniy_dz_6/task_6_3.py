import json


users_hobby = {}
with open('users.csv') as users, open('hobby.csv') as hobby:
    fio = ' '.join(users.readline().split(',')).strip()
    hobby_tmp = ', '.join(hobby.readline().strip().split(','))
    while fio:
        users_hobby[fio] = None if hobby_tmp == '' else hobby_tmp
        fio = ' '.join(users.readline().split(',')).strip()
        hobby_tmp = ', '.join(hobby.readline().strip().split(','))
    else:
        if hobby_tmp:
            users_hobby = 1
            print(users_hobby)
        else:
            with open('users_hobby.txt', 'w') as f:
                json.dump(users_hobby, f)
