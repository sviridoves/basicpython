def thesaurus_adv(*args):
    dict_tmp = {}
    args_tmp = []
    for el in args:
        args_tmp.append(el.split())
    args_tmp.sort(key=lambda el1: el1[1])
    for el in args_tmp:
        if el[1][0] in dict_tmp:
            if el[0][0] in dict_tmp[el[1][0]]:
                dict_tmp[el[1][0]][el[0][0]].append(f'{el[0]} {el[1]}')
            else:
                dict_tmp[el[1][0]][el[0][0]] = [f'{el[0]} {el[1]}']
        else:
            dict_tmp[el[1][0]] = {}
            if el[0][0] in dict_tmp[el[1][0]]:
                dict_tmp[el[1][0]][el[0][0]].append(f'{el[0]} {el[1]}')
            else:
                dict_tmp[el[1][0]][el[0][0]] = [f'{el[0]} {el[1]}']
    return dict_tmp


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))
