import xml.etree.ElementTree as Et
from datetime import datetime
from requests import get


def currency_rates(currency):
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    content = Et.XML(response.content)
    date_response = datetime.strptime(content.get('Date'), "%d.%m.%Y")
    for el in content.findall('Valute'):
        if el.find('CharCode').text == currency.upper():
            return float(el.find('Value').text.replace(',', '.')), date_response.date(), currency.upper()
    return None


def currency_rates_cmd(currency):
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    content = Et.XML(response.content)
    date_response = datetime.strptime(content.get('Date'), "%d.%m.%Y")
    for el in content.findall('Valute'):
        if el.find('CharCode').text == currency.upper():
            return float(el.find('Value').text.replace(',', '.')), date_response.date(), currency.upper()
    return None


if __name__ == '__main__':
    pass
