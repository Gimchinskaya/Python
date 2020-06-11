time = int(input('Введите время в секундах: '))
hours = int(time//3600)
minutes = int(time//60) % 60
seconds = int(time % 60)
if hours < 10:
    hours = '0' + str(hours)
else:
    hours = str(hours)
if minutes < 10:
    minutes = '0' + str(minutes)
else:
    minutes = str(minutes)
if seconds < 10:
    seconds = '0' + str(seconds)
else:
    seconds = str(seconds)
print(f'{hours}:{minutes}:{seconds}')


