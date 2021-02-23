task_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй',
             'директор аэлита']
for string in task_list:
    print(f'Привет, {string.split()[-1].lower().capitalize()}!')
