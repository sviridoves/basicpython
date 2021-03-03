"""
Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (например, USD, EUR, GBP, ...)
и возвращающую курс этой валюты по отношению к рублю. Использовать библиотеку requests. В качестве API можно
использовать http://www.cbr.ru/scripts/XML_daily.asp. Рекомендация: выполнить предварительно запрос к API в обычном
браузере, посмотреть содержимое ответа. Можно ли, используя только методы класса str, решить поставленную задачу?
Функция должна возвращать результат числового типа, например float. Подумайте: есть ли смысл для работы с денежными
величинами использовать вместо float тип Decimal? Сильно ли усложняется код функции при этом? Если в качестве
аргумента передали код валюты, которого нет в ответе, вернуть None. Можно ли сделать работу функции не зависящей
от того, в каком регистре был передан аргумент? В качестве примера выведите курсы доллара и евро.
"""
import xml.etree.ElementTree as ET
from requests import get, utils

def currency_rates(rate):
    respons = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(respons.headers)
    content = respons.content.decode(encoding=encodings)
    tree = ET.XML(content)

    for el in tree.findall('Valute'):
        if el.find('CharCode').text == rate.upper():
             return float(el.find('Value').text.replace(',', '.'))


# currency_rates('USD')
print(currency_rates('USD'))
print(currency_rates('eur'))
print(currency_rates('eur2'))