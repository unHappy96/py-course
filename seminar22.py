# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

# х2 + bх + c = 0
# х1 * х2 = с и  х1 + х2 = – b

# X + Y = S  =>  X = S - Y
# X * Y = P  =>  (S - Y) * Y = P  =>  -Y^2 + Y*S - P = 0  =>  Y^2 - Y*S + P = 0
import math

S = int(input())
P = int(input())

a = 1
b = -S
c = P
x = 0
x1 = 0
x2 = 0

D = b*b - 4*a*c

if D < 0:
    print('Корней нет')

if D == 0:
    x = -b/2*a
    y = S - x
    print(x,y)
    
if D > 0:
    x1 = (-b + math.sqrt(D)) / (2*a)
    x2 = (-b - math.sqrt(D)) / (2*a)
    print(x1, x2)