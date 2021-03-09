src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]


# Решение "в лоб":
# result = [el for el in src if src.count(el) == 1]
# print(type(result), *result)

# Оптимизированное решение
def get_unique_numbers(src_numbers, sort=True):
    unique_numbers = set()
    tmp = set()
    for el in src_numbers:
        if el not in tmp:
            unique_numbers.add(el)
        else:
            unique_numbers.discard(el)
        tmp.add(el)
    if sort:
        unique_numbers_ord = [el for el in src_numbers if el in unique_numbers]
        return unique_numbers_ord
    else:
        return list(unique_numbers)


print(get_unique_numbers(src))
