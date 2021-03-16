# Пример запуска с записью результата в папку на один уровень выше:
# python3 task_6_5.py --users users.csv --hobbys hobby.csv --w ../users_hobby_6_5.txt

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


def main(args):
    users_hobby = {fio: hobby for fio, hobby in parsed_files(args.users, args.hobbys)}
    with open(args.w, 'w') as f:
        f.write(str(users_hobby))
    print(f'Словарь сохранен в файл: {args.w}')

    return 0


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Enter paths for files')
    parser.add_argument('--users', type=str, help='Path to file with users')
    parser.add_argument('--hobbys', type=str, help='Path to file with hobbys')
    parser.add_argument('--w', type=str, help='Path to file to write result')
    args = parser.parse_args()
    exit(main(args))
