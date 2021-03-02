def thesaurus(*args):
    dict_tmp = {}
    args = sorted(args)
    for el in args:
        el = el.capitalize()
        if el[0] in dict_tmp:
            dict_tmp[el[0]].append(el)
        else:
            dict_tmp[el[0]] = [el]
    return dict_tmp


print(thesaurus("Маша", "Иван", "Мария", "Петр", "Илья"))
