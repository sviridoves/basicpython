numbersarray = []
numberssum = 0
maxnumber = 1000

for i in range(1, maxnumber, 2):
    numbersarray.append(i ** 3)

for i in range(0, len(numbersarray)):
    tempsum = 0
    tempnumber = numbersarray[i]
    divisor = 1
    while divisor <= (maxnumber ** 3):
        tempdigit = tempnumber % (divisor * 10)
        tempsum += tempdigit // divisor
        divisor = divisor * 10
    if tempsum % 7 == 0:
        numberssum += tempnumber

print(f'Cумма всех чисел из списка, сумма цифр которых делится нацело на 7 = {numberssum}')

n = 0
numberssum = 0

for number in numbersarray:
    numbersarray[n] = numbersarray[n] + 17
    n += 1

for i in range(0, len(numbersarray)):
    tempsum = 0
    tempnumber = numbersarray[i]
    divisor = 1
    while divisor <= (maxnumber ** 3):
        tempdigit = tempnumber % (divisor * 10)
        tempsum += tempdigit // divisor
        divisor = divisor * 10
    if tempsum % 7 == 0:
        numberssum += tempnumber

print(f'Cумма всех чисел списка после прибавления к каждому 17, сумма цифр которых делится нацело на 7 = {numberssum}')
