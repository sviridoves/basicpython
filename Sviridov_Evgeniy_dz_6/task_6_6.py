# Пример запуска:
# python3 task_6_6.py add 3829,44 3293 959,3
# python3 task_6_6.py show
# python3 task_6_6.py show 2
# python3 task_6_6.py show 2 3


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
    else:
        print('Bad command: add or show only.')


if __name__ == '__main__':
    import argparse
    import os.path

    parser = argparse.ArgumentParser(description='Enter command')
    parser.add_argument('command', nargs='*', help='add or show and arguments (less 5)')
    args = parser.parse_args().command[:6]
    if os.path.exists('bakery.csv'):
        exit(main(args))
    else:
        with open('bakery.csv', 'w') as f:
            pass
        exit(main(args))
