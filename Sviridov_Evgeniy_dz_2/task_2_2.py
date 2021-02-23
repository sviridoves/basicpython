task_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
new_task_list = []

for el in task_list:
    if el.isdigit():
        new_task_list.append('"')
        if len(el) == 1:
            new_task_list.append('0'+el)
        else:
            new_task_list.append(el)
        new_task_list.append('"')
    else:
        digit_count = 0
        digit_index = -1
        if not el.isalnum():
            for ch in el:
                if ch.isdigit():
                    digit_count += 1
                digit_index += 1
        if digit_count == 0:
            new_task_list.append(el)
        elif digit_count > 1:
            new_task_list.append('"')
            new_task_list.append(el)
            new_task_list.append('"')
        else:
            new_task_list.append('"')
            new_task_list.append(el[:digit_index]+'0'+el[digit_index:])
            new_task_list.append('"')

print(("".join((' ' + el + ' ') if el.isalpha() else el for el in new_task_list)).strip().replace('  ', ' '))
