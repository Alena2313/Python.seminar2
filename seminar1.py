# Задача 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и выводит название этого дня недели.
# 1 –> Понедельник
# 10 –> Нет такого дня
# 7 –> Воскресение5
n = int(input('Введите день: '))
res = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"]
print(res[n-1])


# Задача 2. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# A (3,6); B (2,1) -> 5,1
# A (7,-5); B (1,-1) -> 7,21
from math import hypot
 
def distance(p1, p2):
    return hypot(p1[0] - p2[0], p1[1] - p2[1])
 
print(distance((0, 1), (2, 3)))

# Задача 3. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
#1 -> x > 0, y > 0
def quarter(xcoord, ycoord):
    if xcoord > 0 and ycoord > 0:
       print('I четверть')
    if xcoord > 0 and ycoord < 0:
        print('IV четверть')
    if xcoord < 0 and ycoord > 0:
        print('II четверть')
    if xcoord < 0 and ycoord < 0:
        print('III четверть')
 
quarter(-5, 5)

#Задача 4. Напишите программу, которая на вход принимает число (N), а на выходе показывает все чётные числа от 1 до N.
#5 -> 2, 4
#8 -> 2, 4, 6, 8
lst = [1, 2, 4, 6, 8, 7, 42, 15]

for number in lst:
    if number % 2 == 0:
        print(number, end=' ')
    elif number == 100:
        break

 
    

