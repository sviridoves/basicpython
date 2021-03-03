import xml.etree.ElementTree as Et
from requests import get


def currency_rates(currency):
    content = Et.XML(get('http://www.cbr.ru/scripts/XML_daily.asp').content)
    for el in content.findall('Valute'):
        if el.find('CharCode').text == currency.upper():
            return float(el.find('Value').text.replace(',', '.'))
    return None


print(currency_rates('USD'))
print(currency_rates('eur'))
print(currency_rates('eur2'))
