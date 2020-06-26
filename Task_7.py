import json
with open("for_task_7.txt", "r") as f:
    content = f.readlines()
    sum_profit = 0
    firms_numbers = 0
    firms_profit_dict = dict()
    firms_average_dict = dict()
    firms_dicts_list = list()

    for line in content:
        data_firms = line.split()
        firm_name = data_firms[0]
        firm_revenue = data_firms[2]
        firm_costs = data_firms[3]

        profit = float(firm_revenue) - float(firm_costs)

        print(f'Прибыль {firm_name} равна: {profit}')

        firms_profit_dict[firm_name] = profit

        if profit > 0:
            sum_profit += profit
            firms_numbers += 1
    average_profit = sum_profit/firms_numbers
    print('Средняя прибыль равна: ', average_profit)

    firms_average_dict['average_profit'] = average_profit
    firms_dicts_list.append(firms_profit_dict)
    firms_dicts_list.append(firms_average_dict)
    print(firms_dicts_list)

    with open("my_file.json", "w") as write_f:
        json.dump(firms_dicts_list, write_f)

