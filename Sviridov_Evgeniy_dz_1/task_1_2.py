MAX_NUMBER = 1000

numbers_array = []
numbers_sum = 0

for i in range(1, MAX_NUMBER, 2):
    numbers_array.append(i ** 3)

for i in range(0, len(numbers_array)):
    temp_sum = 0
    temp_number = numbers_array[i]
    divisor = 1
    while divisor <= (MAX_NUMBER ** 3):
        temp_digit = temp_number % (divisor * 10)
        temp_sum += temp_digit // divisor
        divisor = divisor * 10
    if temp_sum % 7 == 0:
        numbers_sum += temp_number

print(f'Cумма всех чисел из списка, сумма цифр которых делится нацело на 7 = {numbers_sum}')

n = 0
numbers_sum = 0

for number in numbers_array:
    numbers_array[n] = numbers_array[n] + 17
    n += 1

for i in range(0, len(numbers_array)):
    temp_sum = 0
    temp_number = numbers_array[i]
    divisor = 1
    while divisor <= (MAX_NUMBER ** 3):
        temp_digit = temp_number % (divisor * 10)
        temp_sum += temp_digit // divisor
        divisor = divisor * 10
    if temp_sum % 7 == 0:
        numbers_sum += temp_number

print(f'Cумма всех чисел списка после прибавления к каждому 17, сумма цифр которых делится нацело на 7 = {numbers_sum}')
