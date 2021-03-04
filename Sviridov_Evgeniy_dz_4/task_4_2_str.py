from requests import get


def currency_rates(currency='USD'):
    content = (get('http://www.cbr.ru/scripts/XML_daily.asp')).content
    content = str(content)
    char_code = content.find(currency.upper())
    if char_code == -1:
        return None
    else:
        start_value = content.find('<Value>', char_code) + 7
        end_value = content.find('</Value>', char_code)
        value = content[start_value:end_value]
        return value


print(currency_rates('USD'))
print(currency_rates('eur'))
print(currency_rates('eur2'))
