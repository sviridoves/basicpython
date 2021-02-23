my_type = str(type(15 * 3))
print('Тип результата выражения 15 * 3:', my_type[(my_type.find("'")+1): -2])

my_type = str(type(15 / 3))
print('Тип результата выражения 15 / 3:', my_type[(my_type.find("'")+1): -2])

my_type = str(type(15 // 3))
print('Тип результата выражения 15 // 3:', my_type[(my_type.find("'")+1): -2])

my_type = str(type(15 ** 3))
print('Тип результата выражения 15 ** 3:', my_type[(my_type.find("'")+1): -2])
