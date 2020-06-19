user_name = input('Введите имя: ')
user_surname = input('Введите фамилию: ')
user_year = int(input('Введите год рождения: '))
user_city = input('Введите город проживания: ')
user_email = input('Введите email: ')
user_phone = input('Введите телефон: ')


def user_data(name, surname, year, city, email, phone):
    print(f'имя: {name}, фамилия: {surname}, год рождения: {year}, город проживания: {city}, email: {email}, телефон: {phone}')


user_data(name=user_name, surname=user_surname, year=user_year, city=user_city, email=user_email, phone=user_phone)