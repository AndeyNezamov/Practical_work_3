educational_grant = int(input('Введите стипендию: '))
expenses = int(input('Введите расходы на проживание: '))
res = expenses - educational_grant
for i in range(1, 11):
    if i == 1:
        print(f'\n{i:>2}. месяц траты {expenses} не хватает {res}')
        
    else:
        expenses += expenses * 0.03
        res += expenses - educational_grant
        print(f'{i:>2}. месяц траты {round(expenses, 1)} не хватает {round(res,2)}')
else:
    print(f'\nПопросить у родителей {round(res,2)} рублей')