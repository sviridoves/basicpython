# Пример запуска:
# python3 task_6_7.py change 2 3024,32

import os


def read_from_file(*args):
    if len(args) == 0:
        with open('bakery.csv') as f:
            line = f.readline().strip()
            while line:
                print(line)
                line = f.readline().strip()
    else:
        if len(args[0]) == 1:
            with open('bakery.csv') as f:
                for i, line in enumerate(f):
                    if i >= int(args[0][0]) - 1:
                        print(line.strip())
        elif len(args[0]) == 2:
            with open('bakery.csv') as f:
                for i, line in enumerate(f):
                    if int(args[0][0]) - 1 <= i < int(args[0][1]):
                        print(line.strip())
                    elif i == int(args[0][1]):
                        break


def add_to_file(cost):
    with open('bakery.csv', 'a') as f:
        f.write(f'{cost}\n')


def change_line(line_number, cost):
    with open('bakery.csv') as f:
        i_find = False
        i = 0
        line = f.readline()
        f_tmp = open('tmp_bakery.csv', 'w')
        while line:
            if i == int(line_number) - 1:
                f_tmp.write(f'{cost}\n')
                i_find = True
            else:
                f_tmp.write(line)
            i += 1
            line = f.readline()
        f_tmp.close()
        if i_find:
            os.remove('bakery.csv')
            os.rename('tmp_bakery.csv', 'bakery.csv')
        else:
            os.remove('tmp_bakery.csv')
            print(f'Line number {line_number} not found.')


def main(args):
    if args[0] == 'add':
        print('To file bakery.csv add lines:')
        for cost in args[1:]:
            add_to_file(cost)
            print(cost)
    elif args[0] == 'show':
        if len(args) == 1:
            read_from_file()
        else:
            read_from_file(args[1:])
    elif args[0] == 'change':
        change_line(args[1], args[2])
    else:
        print('Bad command: add or show only.')


if __name__ == '__main__':
    import argparse
    import os.path

    parser = argparse.ArgumentParser(description='Enter command')
    parser.add_argument('command', nargs='*', help='add, change or show and arguments (less 5)')
    args = parser.parse_args().command[:6]
    if os.path.exists('bakery.csv'):
        exit(main(args))
    else:
        with open('bakery.csv', 'w') as f:
            pass
        exit(main(args))
