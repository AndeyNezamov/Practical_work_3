start = int(input('Введите начало отрезка: '))
finish = int(input('Введите конец отрезка: '))
if finish > start:
    start, finish = finish, start
size = int(input('Введите шаг: '))
if size > 0:
    size *= -1
for x in range(start, finish, size):
    y = (x ** 3) + 2 * (x ** 2) - (4 * x) + 1
    print(f'В точке {x} функция равна {y}')