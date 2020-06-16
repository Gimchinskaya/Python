"""structure_goods = [(1, {'название': 'компьютер', 'цена': 20000, 'количество': 5, 'eд': 'шт.'}),
                   (2, {'название': 'принтер', 'цена': 6000, 'количество': 2, 'eд': 'шт.'}),
                   (3, {'название': 'сканер', 'цена': 2000, 'количество': 7, 'eд': 'шт.'})]
"""
positions_number = int(input('Введите колличество позиций: '))
number = 1
structure_goods = list()

while number <= positions_number:
    name = input('Введите название товара: ')
    price = input('Введите цену товара: ')
    goods_number = input('Введите количество товаров: ')

    structure_goods.append((number, {'название': name, 'цена': price, 'количество': goods_number}))
    number += 1

print(structure_goods)

new_dict = dict()

for structure_value in structure_goods:
    structure_value_index = structure_goods.index(structure_value)

    if 'название' in new_dict:
        names = new_dict.get('название')
        new_dict.update({'название': [names, structure_goods[structure_value_index][1]['название']]})
    else:
        new_dict['название'] = structure_goods[structure_value_index][1]['название']

    if 'цена' in new_dict:
        prices = new_dict.get('цена')
        new_dict.update({'цена': [prices, structure_goods[structure_value_index][1]['цена']]})
    else:
        new_dict['цена'] = structure_goods[structure_value_index][1]['цена']

    if 'количество' in new_dict:
        numbers = new_dict.get('количество')
        new_dict.update({'количество': [numbers, structure_goods[structure_value_index][1]['количество']]})
    else:
        new_dict['количество'] = structure_goods[structure_value_index][1]['количество']

print(new_dict)
