user_text = input('Введите текст: ')
text_list = user_text.split()
check_latin_list = list('qwertyuiopasdfghjklzxcvbnm')
result_string = list()


def int_func(word):
    word_chars = list(word)
    for text_tail in word_chars:
        if text_tail not in check_latin_list:
            print('Just small Latin simbols! This word: \'', word, '\' is not spelled in small Latin')
            return ''
    return word.capitalize()


for word_from_text in text_list:
    result_word = int_func(word_from_text)
    if result_word != '':
        result_string.append(result_word)

print(' '.join(result_string))