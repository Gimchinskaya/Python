from sys import argv

script_name, production_in_hours, rate_per_hour, premium = argv
production_in_hours = float(production_in_hours)
rate_per_hour = float(rate_per_hour)
premium = float(premium)

print('Выработка в часах: ', production_in_hours)
print('Ставка в час: ', rate_per_hour)
print('Премия: ', premium)


def payroll_func(prod, rate, pr):
    payroll = prod * rate + pr
    return payroll


print('Зарплата: ', payroll_func(production_in_hours, rate_per_hour, premium))



