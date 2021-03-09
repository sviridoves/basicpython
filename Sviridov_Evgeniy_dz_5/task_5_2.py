n = int(input('Введите число n: '))
add_to_15 = (i for i in range(1, n+1, 2))
print(type(add_to_15))
for num in add_to_15:
    print(num, end=' ')
