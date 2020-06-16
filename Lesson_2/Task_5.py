rating_list = [8, 6, 6, 5, 4, 2]

user_element = int(input('Введите новый элемент рейтинга: '))

if user_element in rating_list:
    for rating_el_index in range(len(rating_list) - 1, -1, -1):
        if rating_list[rating_el_index] == user_element:
            rating_list.insert(rating_el_index, user_element)
            print(rating_list)
            break
else:

    # method_2
    for rating_el_index in range(0, len(rating_list), 1):
        if (rating_list[rating_el_index] > user_element) & (rating_el_index == (len(rating_list) - 1)):
            rating_list.append(user_element)
            print(rating_list)
            break

        if rating_list[rating_el_index] < user_element:
            rating_list.insert(rating_el_index, user_element)
            print(rating_list)

            break
"""
    # method_1
    for value in rating_list:
        print(rating_list.index(value))
        if user_element > value:
            rating_list.insert(rating_list.index(value), user_element)
            print(rating_list)
            break

        if (user_element < value) & (rating_list.index(value) == (len(rating_list)-1)):
            rating_list.append(user_element)
            print(rating_list)
            break
"""
