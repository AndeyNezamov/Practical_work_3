boys = int(input('Введите количество мальчиков: '))
girls = int(input('Введите количество девочек: '))
res = []
if (boys > girls * 2) | (girls > boys * 2):
    print('Нет решения')
elif boys >= girls:
    for i in range(boys - girls):
        res.append('BGB')
    for i in range(girls - (boys-girls)):
        res.append('BG')
else:
    for i in range(girls-boys):
        res.append('GBG')
    for i in range(boys - (girls-boys)):
        res.append('GB')

print(*res, sep='')