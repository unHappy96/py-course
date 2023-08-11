# Требуется вывести все целые степени двойки (т.е. числа вида 2^k), не превосходящие числа N.

N = int(input())
value = 0
k=0

while value < N:
    value = 2**k
    if value > N:
        break
    else:
        print(value)
    k += 1