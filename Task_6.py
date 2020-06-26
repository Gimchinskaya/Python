with open("for_task_6.txt", "r") as f:
    content = f.readlines()
    dict_lessons = dict()
    for line in content:
        str_elements = line.split()
        name = ''.join([el for el in list(str_elements[0]) if el != ':'])
        lectures = (''.join([el for el in list(str_elements[1]) if el != '-']))[:-3]
        practice = (''.join([el for el in list(str_elements[2]) if el != '-']))[:-4]
        labs = (''.join([el for el in list(str_elements[3]) if el != '-']))[:-5]

        if lectures == '':
            lectures = '0'
        if practice == '':
            practice = '0'
        if labs == '':
            labs = '0'

        sum_lessons = int(lectures) + int(practice) + int(labs)
        dict_lessons[name] = sum_lessons

    print('Итоговый словарь:\n', dict_lessons)