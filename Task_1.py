with open("for_task_1.txt", "w") as f:

    while True:
        user_string = input('Введите текст:\n')
        if user_string == '':
            break
        f.write(user_string + '\n')