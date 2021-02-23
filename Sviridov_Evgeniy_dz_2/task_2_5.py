def print_costs(costs_list):
    for cost in costs_list:
        cost = str(float(cost))
        tmp_cost = cost.split('.')
        print(f'{tmp_cost[0]} руб {int(tmp_cost[1]):02d} коп')


cost_list = [57.8, 46.51, 97, 278, 154.57, 20.54, 54, 294.99, 39.65, 43, 19.43]

print('{:*^20s}'.format('Задание 1'))
print_costs(cost_list)

print('\n{:*^20s}'.format('Задание 2'))
print('ID cost_list before sort: ', id(cost_list))
cost_list.sort()
print('ID cost_list after sort: ', id(cost_list))
print_costs(cost_list)

print('\n{:*^20s}'.format('Задание 3'))
new_cost_list = sorted(cost_list, reverse=True)
print_costs(new_cost_list)

print('\n{:*^20s}'.format('Задание 4'))
print_costs(sorted(new_cost_list[0:5]))
