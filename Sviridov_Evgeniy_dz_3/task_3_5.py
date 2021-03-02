import random


def get_jokes(n, repeat=0):
    """
    Возвращает n шуток, сформированных из трех случайных слов, взятых из трех списков:
    nouns, adverbs, adjectives
    """
    res = []
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    if len(nouns) < n and repeat != 0:
        return f'n должно быть меньше или равно {len(nouns)}'
    if repeat == 0:
        for i in range(n):
            res.append(f'{random.choice(nouns)} {random.choice(adverbs)} {random.choice(adjectives)}')
    else:
        for i in range(n):
            res.append(f'{random.choice(nouns)} {random.choice(adverbs)} {random.choice(adjectives)}')
            noun, adverb, adjective = res[i].split()
            nouns.remove(noun)
            adverbs.remove(adverb)
            adjectives.remove(adjective)
    return res


print(get_jokes(n=2, repeat=0))
