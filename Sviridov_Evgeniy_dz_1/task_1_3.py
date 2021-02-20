COUNT = 20

numbers = []

for i in range(COUNT + 1):
    numbers.append(i)

for i in numbers:
    if i % 10 == 1 and (i < 10 or i > 20):
        print(f'{i} процент')
    elif (i % 10 == 2 or i % 10 == 3 or i % 10 == 4) and (i < 10 or i > 20):
        print(f'{i} процента')
    else:
        print(f'{i} процентов')
