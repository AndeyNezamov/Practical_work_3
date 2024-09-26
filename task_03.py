reverse_timer = int(input('Напишите на какое время включить микроволновну? '))
for i in range(reverse_timer, 0, -1):
    user_command = int(input('1 - прервать, 0 - продолжить '))
    if user_command == 1:
        print(f'{i} (ая) секунда - Ваша еда готова, можете забрать')
        break
    else:
        print(f'{i} (ая) секунда')
else:
    print('Ваша еда готова, осторожно горячо!')