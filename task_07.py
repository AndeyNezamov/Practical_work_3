res = sum([((-1) ** i) * (1 / 2 ** i) for i in range(int(input('Введите N: ')))])
# for i in range(int(input('Введите число N: '))):
#     elem = ((-1) ** i) * (1 / 2 ** i)
#     res += elem
print(f'Ответ: {res}')