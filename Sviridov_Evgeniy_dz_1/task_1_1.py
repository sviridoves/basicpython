duration = int(input('Введите промежуток времени в секундах: '))
seconds = duration % 60
duration = (duration - seconds) // 60
minutes = duration % 60
duration = (duration - minutes) // 60
hours = duration % 24
duration = (duration - hours) // 24
days = duration % 365
duration = (duration - days) // 365

if duration > 0:
    print(f'{duration} год (лет) {days} сут {hours} час {minutes} мин {seconds} сек')
elif days > 0:
    print(f'{days} сут {hours} час {minutes} мин {seconds} сек')
elif hours > 0:
    print(f'{hours} час {minutes} мин {seconds} сек')
elif minutes > 0:
    print(f'{minutes} мин {seconds} сек')
else:
    print(f'{seconds} сек')
