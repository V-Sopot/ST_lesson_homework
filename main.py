import random
number = random.randrange(0, 50)
z = -1
while z !=number:
    z = int(input('Введи число от 0 до 50'))
    if z > number:
        print('Загаданное число меньше')
    elif z < number:
        print('Загаданное число больше')
    elif z ==number:
        print('Ты угадал число!')
