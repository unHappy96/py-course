S = int(input('Введите сумму:  '))
P = int(input('Введите произведение:  '))

for x in range(0, 1000):
    for y in range(0, 1000):
        if (x + y == S and x*y == P):
            print(x,y)