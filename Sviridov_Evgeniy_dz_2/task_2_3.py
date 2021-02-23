task_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
number_index = []
count = 0

for el in task_list:
    if el.isdigit():
        number_index.append(count)
        if len(el) == 1:
            task_list[count] = f'{int(el):02d}'
    else:
        if not el.isalnum():
            digit_count = 0
            digit_index = -1
            for ch in el:
                if ch.isdigit():
                    digit_count += 1
                digit_index += 1
            if digit_count > 0:
                number_index.append(count)
            if digit_count == 1:
                task_list[count] = f'{el[:digit_index]}{int(el[digit_index:]):02d}'
    count += 1

for i in number_index[::-1]:
    task_list.insert(i+1, '"')
    task_list.insert(i, '"')

print(("".join((' ' + el + ' ') if el.isalpha() else el for el in task_list)).strip().replace('  ', ' '))
