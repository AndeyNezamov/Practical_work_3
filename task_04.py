a = int(input('Введите точку А: '))
b = int(input('Введите точку B: '))
c = int(input('Введите число С: '))

res = [i for i in range(a,b+1) if i % c == 0]
print(res)
print(f'Среднее арифметическое отрезка А:В {sum(res)/len(res)}')