'''
1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

Пример:

- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
'''
# from random import randint

# def show_sum(lst = [randint(-5, 5) for i in range(randint(5, 10))]):
    
#     result = 0
    
#     for i in range(len(lst)):
#         if i % 2 != 0:
#             result += lst[i]

#     return result


# if __name__ == '__main__':
#     print(show_sum())

'''
2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

Пример:

- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]
'''

# from random import randint

# def show_comp(lst):

#     result = []

#     if len(lst) % 2 == 0:
#         l = len(lst) // 2 
#         for i in range(l):
#             result.append(lst[i] * lst[len(lst) - i - 1])
#     else:
#         l = len(lst) // 2 + 1
#         for i in range(l):
#             result.append(lst[i] * lst[len(lst) - i - 1])

#     return result

# if __name__ == '__main__':
#     print(show_comp([2, 3, 4, 5, 6]))
#     print(show_comp([2, 3, 5, 6]))
#     print(show_comp([randint(1, 5) for i in range(randint(4, 6))]))

'''
3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
(если получаются длинные числа после запятой, это нормально и особенность данного языка программирования. ваш ответ может не совпадать с примером(может получитя 0,20))

Пример:

- [1.1, 1.2, 3.1, 5, 10.01] => 0.19
'''
# from random import random, randint

# def show_diff(lst):

#     new_lst = []

#     for i in lst:
#         new_lst.append(i - i // 1)
    
#     return max(new_lst) - min(new_lst)


# if __name__ == '__main__':
#     print(show_diff([1.1, 1.2, 3.1, 5, 10.01]))
#     print(show_diff([round(random(), 3) for i in range(randint(4, 6))]))

'''
4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.

Пример:

- 45 -> 101101
- 3 -> 11
- 2 -> 10
'''
# def magic(decimal):
    
#     return bin(decimal)

# if __name__ == '__main__':
#     print(magic(45))
#     print(magic(3))
#     print(magic(2))

'''
5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

Пример:

- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи](https://ru.wikipedia.org/wiki/%D0%9D%D0%B5%D0%B3
%D0%B0%D1%84%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8#:~:text=%D0%92%20%D0%BC%D0%B0%D1%82%D0%B5%D0%BC%D0%B0%D1%82%D0%B8%D0%BA%D0%B5%2C%20%D1%87%D0%B8%D1%81%D
0%BB%D0%B0%20%D0%BD%D0%B5%D0%B3%D0%B0%D1%84%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8%20%E2%80%94%20%D0%BE%D1%82%D1%80%D0%B8%D1%86%D0%B0%D1%82%D0%B5%D0%BB%D1%
8C%D0%BD%D0%BE%20%D0%B8%D0%BD%D0%B4%D0%B5%D0%BA%D1%81%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%BD%D1%8B%D0%B5%20%D1%8D%D0%BB%D0%B5%D0%BC%D0%B5%D0%BD%D1%82%D1%8B%20%D0
%BF%D0%BE%D1%81%D0%BB%D0%B5%D0%B4%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D0%B8%20%D1%87%D0%B8%D1%81%D0%B5%D0%BB%20%D0%A4%D0%B8%D0%B1%D0%B
E%D0%BD%D0%B0%D1%87%D1%87%D0%B8.)
'''

# def make_fibo(n):

#     fib1 = 1
#     fib2 = 1
#     i = 1

#     while (i < n):
#         fib1, fib2, i = fib1 + fib2, fib1, i + 1
#     return fib1

# def show_fibo(n = int(input('Введите число: '))):

#     lst = [0]

#     for i in range(n):
#         lst.append(make_fibo(i))
#         lst.insert(0, - make_fibo(i))

#     return lst

# if __name__ == '__main__':
#     print(show_fibo())
