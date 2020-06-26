with open("for_task_2.txt", "r") as f:
    lines = f.readlines()
    print('Колличество строк в файле: ', len(lines))

    for line in lines:
        words = line.split()
        print(f'Колличество слов в строке {lines.index(line)+1}: {len(words)}')
