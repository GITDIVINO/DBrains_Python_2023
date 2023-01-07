'''1. Напишите программу, которая принимает на вход два числа и проверяет является ли одно число квадратом другого'''

# def is_pow(number_1, number_2):
#     if number_1 ** 2 == number_2 or number_2 ** 2 == number_1:
#         return 'Yes'
#     else:
#         return 'No'


# if __name__ == '__main__':
#     print(
#         is_pow(2,4), 
#         is_pow(3,8),
#         is_pow(13, 169)
#         )

'''2. Программа принимает 5 цифр и вывод наибольшее из них'''

# def what_bigger():
    
#     numbers = []

#     for i in range(5):
#         a = int(input(f'Введите {int(i)+1} число: '))
#         numbers.append(a)

#     return max(numbers)


# if __name__ == '__main__':
#     print(what_bigger())

'''3. На вход принимает число N и выводит диапозон от -N до N'''

# def make_range(number = int(input('Введите число: '))):

#     numbers = [0]

#     for i in range(number):
#         numbers.append(i+1)
#         numbers.append(-i-1)
    
#     return sorted(numbers)


# if __name__ == '__main__':
#     print(make_range())

'''4. Принимает дробь и возвращает первую цифру дробной части чсисла'''

# def show_decimal(d_number = float(input('Введите дробное число: '))):
#         if d_number % 1 == 0:
#             return 'NO'
#         else:
#             return int((d_number % 1) * 10)


# if __name__ == '__main__':
#     print(show_decimal())

'''5. Проверить кратно ли число 5, 10 или 15, но не 30'''

# def check(number = int(input('Введите число: '))):
#     if (number % 5 == 0 and number % 10 == 0 or number % 15 == 0) and number != 30:
#         return 'YES'
#     else:
#         return 'NO'

# if __name__ == '__main__':
#     print(check())

