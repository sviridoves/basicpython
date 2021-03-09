def gen_numbers(n):
    for i in range(1, n+1, 2):
        yield i


add_to_15 = gen_numbers(15)
print(type(add_to_15))
for num in add_to_15:
    print(num, end=' ')
