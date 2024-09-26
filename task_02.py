summ = 0
for i in range(0,int(input('Введите количество должников: '))+1, 5):
    credit = int(input(f'Должник с номером {i}\nСколько должны? '))
    summ += credit

print(f'Общая сумма долга: {summ}')