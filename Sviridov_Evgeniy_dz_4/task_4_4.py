import utils

print('{2}/RUB = {0} in date {1}'.format(*utils.currency_rates('USD')))
print('{2}/RUB = {0} in date {1}'.format(*utils.currency_rates('eur')))
