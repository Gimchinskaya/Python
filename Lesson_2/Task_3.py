# dict

my_dict = {1: 'зима',
           2: 'зима',
           3: 'весна',
           4: 'весна',
           5: 'весна',
           6: 'лето',
           7: 'лето',
           8: 'лето',
           9: 'осень',
           10: 'осень',
           11: 'осень',
           12: 'зима'}

month_number = int(input('Введите номер месяца: '))
if my_dict.get(month_number) is not None:
    print(my_dict.get(month_number))
else:
    print('Такого месяца не существует')

# list

month_list = {'1 зима',
              '2 зима',
              '3 весна',
              '4 весна',
              '5 весна',
              '6 лето',
              '7 лето',
              '8 лето',
              '9 осень',
              '10 осень',
              '11 осень',
              '12 зима'}

season = None
month_number = int(input('Введите номер месяца: '))

for month in month_list:
    element_list = month.split()
    if month_number == int(element_list[0]):
        season = element_list[1]

if season is None:
    print('Такого месяца не существует')
else:
    print(season)




