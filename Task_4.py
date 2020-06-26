with open("for_task_4.txt", "r") as f:

    lines = f.readlines()
    new_lines = list()

    for line in lines:
        text_line = line.split()
        eng_numeral = text_line[0]

        if eng_numeral == 'One':
            line = line.replace("One", "Один")
        if eng_numeral == 'Two':
            line = line.replace("Two", "Два")
        if eng_numeral == 'Three':
            line = line.replace("Three", "Три")
        if eng_numeral == 'Four':
            line = line.replace("Four", "Четыре")
        new_lines.append(line)
    with open("new_task_4.txt", "w") as new_f:
        new_f.writelines(new_lines)