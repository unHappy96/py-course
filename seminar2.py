# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

n = int(input('How much coins on the table?  '))  # вводим число монет n, лежащих на столе

heads = 0                                         # создали переменные для орла и решки
tails = 0 

for i in range(n):                                                      # цикл для ввода данных
    value = int(input('Heads or tails? Heads - 1, Tails - 0:  ')) 
    if value != 0 and value != 1:                                           # если введенное значение не равно 1 и 0 прерывает код и выводит сообщение
        print('error, invalid value')   
        break
    if value == 1: 
        heads += 1 
    else: 
        tails += 1

check = heads+tails

if check == n:                                                              # проверяем, правильно ли ввел значения пользователь
    if heads < tails:
        print(f'minimum value: {heads}')
    if heads > tails:
        print(f'minimum value: {tails}')
    if heads == tails:
        print(f'minimum value: {tails}')