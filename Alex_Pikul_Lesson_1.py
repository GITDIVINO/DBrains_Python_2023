'''1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
Пример:
- 6 -> да
- 7 -> да
- 1 -> нет'''

# def whatday(number):
 
#     week = {
#         1: 'Monday',
#         2: 'Tuesday',
#         3: 'Wensday',
#         4: 'Thursday',
#         5: 'Friday',
#         6: 'Suturday',
#         7: 'Sunday'
#     }

#     while number in range(7):    
#         if number == 6 or number == 7:
#             return f'Today is {week[number]} - weekend'
#         else:
#             return f'Today is {week[number]} - workweek'
#     else:
#         return 'Try again....'
 

# if __name__ == "__main__":
#     print(whatday(int(input('Введите число: '))))


'''2. Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z (расшифровка этого выражения not (x[0] or x[1] or x[2] = not x[0] 
and not x[1] and not x[2]) для всех значений предикат.'''

# def check():

#     x = []

#     for i in range(3):
#         x.append(int(input(f'Введите {i+1} число: ')))

#     if not (x[0] or x[1] or x[2]) == (not x[0] and not x[1] and not x[2]):
#         return 'Выражение "not (x[0] or x[1] or x[2] = not x[0] and not x[1] and not x[2])" истинно'
#     return 'Выражение "not (x[0] or x[1] or x[2] = not x[0] and not x[1] and not x[2])" неистинно'


# if __name__ == "__main__":
#     print(check())

'''3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка.
Пример:
- x=34; y=-30 -> 4
- x=2; y=4-> 1
- x=-34; y=-30 -> 3'''

# def what_quarter(x = int(input('Введите координату x: ')), y = int(input('Введите координату y: '))):
    
#     if x > 0 and y > 0:
#         return '1 четверть'
#     elif x > 0 and y < 0:
#         return '2 четверть'
#     elif x < 0 and y < 0:
#         return '3 четверть'
#     return '4 четверть'


# if __name__ == "__main__":
#     print(what_quarter())

'''4. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).'''

# def check_quarter(quater_number = int(input('Введите номер четверти: '))):

#     if quater_number == 1:
#         return 'x > 0 и y > 0'
#     elif quater_number == 2:
#         return 'x > 0 и y < 0'
#     elif quater_number == 3:
#         return 'x < 0 и y < 0'
#     elif quater_number == 4:
#         return 'x < 0 и y > 0'
#     return 'Введите корректную четверть'


# if __name__ == "__main__":
#     print(check_quarter())


'''5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
Пример:
- A (3,6); B (2,1) -> 5,09
- A (7,-5); B (1,-1) -> 7,21'''

# def show_dist(f1 = [0, 0], f2 = [0, 0]):

#     f1[0] = int(input('Введите x1: '))
#     f1[1] = int(input('Введите y1: '))
#     f2[0] = int(input('Введите x2: '))
#     f2[1] = int(input('Введите y2: '))

#     return ((f1[0] - f2[0]) ** 2 + (f1[1] - f2[1]) ** 2) ** 0.5

# if __name__ == "__main__":
#     print(show_dist())