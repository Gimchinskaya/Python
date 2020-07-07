import random


class LotoCard:
    def __init__(self, name):
        self.card = []
        self.name = name
        self.string_numbers = 3

    def __str__(self):
        if self.name == 'User':
            in_string = '-------- Пользователь -------\n'
        else:
            in_string = '--------- Компьютер ---------\n'
        for string_card in self.card:
            in_string += '  '.join(str(element) for element in string_card) + '\n'
        in_string += '-----------------------------\n'
        return in_string

    def set_string_to_card(self):
        while len(self.card) < self.string_numbers:
            numbers = []
            while len(numbers) < 5:
                repeat_flag = True
                elems = random.randint(1, 90)
                if len(self.card) > 0:
                    for cards_elem_index in range(0, len(self.card)):
                        if elems in self.card[cards_elem_index]:
                            repeat_flag = False
                if elems not in numbers and repeat_flag is True:
                    numbers.append(elems)
            numbers = list(numbers) + list(' ' * 4)
            random.shuffle(numbers)

            for pos in range(0, len(numbers)):
                n = 1
                if numbers[pos] == ' ':
                    continue
                else:
                    while n + pos <= len(numbers) - 1:
                        if numbers[pos + n] != ' ' and (numbers[pos] > numbers[pos + n]):
                            numbers[pos], numbers[pos + n] = numbers[pos + n], numbers[pos]
                        n += 1
            self.card.append(numbers)


class LotoGame:
    def __init__(self, card_user, card_comp):
        self.start = input('\nНачнем Игру Супер Лото? (y/n):')
        self.card_user = card_user
        self.card_comp = card_comp

    def load_game(self):
        steps = 90
        loto_numbers = []
        while steps > 0:
            loto_number = random.randint(1, 90)
            if loto_number not in loto_numbers:
                loto_numbers.append(loto_number)
                steps -= 1
                print('Новый бочонок: ', loto_number, '(осталось', steps, ')')
                print(self.card_user)
                print(self.card_comp)
                self.comp_logic(loto_number)
                change_user = input('Зачеркнуть цифру? (y/n): ')
                win_user_status = self.user_logic(loto_number, change_user)

                if not win_user_status:
                    print('Вы проиграли!')
                    print('ИИ: Выкуси, костяной мешок!')
                    return
                else:
                    final_flag = self.checkout()
                    if final_flag:
                        return

    def user_logic(self, loto_number, change_user):
        win_flag = False
        have_elem_flag = False
        for element_index in range(0, len(self.card_user.card)):
            if loto_number in self.card_user.card[element_index]:
                have_elem_flag = True
                index_of_number = self.card_user.card[element_index].index(loto_number)
                if change_user == 'y':
                    self.card_user.card[element_index][index_of_number] = '-'
                    print('Отлично!')
                    win_flag = True
        if not have_elem_flag and change_user == 'n':
            win_flag = True
        return win_flag

    def comp_logic(self, loto_number):
        have_elem_flag = False
        for element_index in range(0, len(self.card_comp.card)):
            if loto_number in self.card_comp.card[element_index]:
                have_elem_flag = True
                index_of_number = self.card_comp.card[element_index].index(loto_number)
                self.card_comp.card[element_index][index_of_number] = '-'
                print('ИИ: Восстание машин! Компьютер зачеркивает!')
        if not have_elem_flag:
            print('ИИ: Я не должен проиграть!')

    def checkout(self):
        user_win_status = False
        user_sum_count = 0

        comp_win_status = False
        comp_sum_count = 0

        final_flag = True

        for user_elem_index in range(0, len(self.card_user.card)):
            if self.card_user.card[user_elem_index].count('-') == 5:
                user_sum_count += 5
        if user_sum_count == 15:
            user_win_status = True

        for comp_elem_index in range(0, len(self.card_comp.card)):
            if self.card_comp.card[comp_elem_index].count('-') == 5:
                comp_sum_count += 5
        if comp_sum_count == 15:
            comp_win_status = True

        if user_win_status and comp_win_status:
            print('\nНичья, ИИ и Игрок победили!')
        elif user_win_status and not comp_win_status:
            print('\nИгрок ПОБЕДИЛ!!!')
        elif not user_win_status and comp_win_status:
            print('\nИИ ПОБЕДИЛ!!!')
        elif not user_win_status and not comp_win_status:
            print('\nПродолжаем супер-игру!')
            final_flag = False
        return final_flag


loto_card_user = LotoCard('User')
loto_card_user.set_string_to_card()
print(loto_card_user)

loto_card_comp = LotoCard('Comp')
loto_card_comp.set_string_to_card()
print(loto_card_comp)

loto_game = LotoGame(loto_card_user, loto_card_comp)
if loto_game.start == 'y':
    loto_game.load_game()
else:
    print('До свидания!')
