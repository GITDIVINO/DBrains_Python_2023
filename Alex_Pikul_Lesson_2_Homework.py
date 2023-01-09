'''Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

Пример:

- 6782 -> 23
- 0.56 -> 11
'''

# def sum(num = float(input('Введите число: '))):

#     number = str(num)
#     result = 0

#     for i in range(len(number)):
#         if number[i].isdigit():
#             result += int(number[i])
    
#     return result


# if __name__ == '__main__':
#     print(sum())

'''Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

Пример:

- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
'''
# def some_func(num = int(input('Введите число: '))):

#     opt = [i+1 for i in range(num)]
#     result = []

#     for i in range(num):
#         if opt[i] == 1:
#             result.append(opt[i])
#         else:
#             result.append(result[i-1]*opt[i])

#     return result


# if __name__ == '__main__':
#     print(some_func())

'''
Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.
'''

# def get_funcsum(n = int(input('Введите число: '))):

#     some_list = [round((1 + 1/i)**i, 2) for i in range(1, n+1)]
#     return sum(some_list)


# if __name__ == '__main__':
#     print(get_funcsum())

'''
Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в отдельном 
списке( пример n=4, lst1=[4,-2,1,3] - списко на основе n, а позиции элементов lst2=[3,1].
'''
# import random

# def show_result(n = int(input('Введите число: '))):
    
#     numbers = [i for i in range(-n, n + 1)]
#     lst1 = [random.choice(numbers) for i in range(n)]
#     lst2 = [int(input('Введите 1е число: ')), int(input('Введите 2е число: '))]

#     return lst1[lst2[0] - 1] * lst1[lst2[1] - 1]
    
# if __name__ == '__main__':
#     print(show_result())

'''
Реализуйте алгоритм перемешивания списка. (рандомно поменять местами элементы списка между собой)
'''

# import random

# def shake_list(n = int(input('Введите число: '))):

#     lst1 = [i for i in range(n)]
#     random.shuffle(lst1)

#     return lst1

# if __name__ == '__main__':
#     print(shake_list())







