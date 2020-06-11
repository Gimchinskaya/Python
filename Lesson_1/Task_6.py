first_res = float(input('Введите результат пробежки в первый день в км: '))
final_res = float(input('Введите желаемый результат пробежки в км: '))

res = first_res
days = 0

if first_res > final_res:
    print('Ты итак все пробежал')
else:
    days += 1
    print(days,'-й день:', "%.2f" % res)

while res < final_res:
    res = res + res*0.1
    days += 1
    print(days,'-й день:', "%.2f" % res)

print('на', days,'-й день спортсмен достиг результата — не менее', final_res, 'км')

