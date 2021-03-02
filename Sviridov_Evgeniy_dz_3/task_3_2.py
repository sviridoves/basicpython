digit_dict = {
    'zero': 'ноль',
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}


def num_translate_adv(digit):
    return digit_dict[digit] if digit in digit_dict else None or \
           digit_dict[digit.lower()].capitalize() if digit.lower() in digit_dict else None


print(num_translate_adv("one"))
print(num_translate_adv("Eight"))
print(num_translate_adv(" "))
