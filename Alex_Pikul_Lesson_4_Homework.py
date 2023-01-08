'''
1. Вычислить число c заданной точностью d

Пример:

- при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
'''

# def show_exc(d = int(input('Введите количество знаков после запятой: '))):

#     num = round(10 / 3, d)

#     return num


# if __name__ == '__main__':
#     print(show_exc())

'''
Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
'''
# def show_mult(n = int(input('Задайте натуральное число: '))):

#     m = 1
#     lst1 = []

#     while m <= n:
#         if n % m == 0:
#             lst1.append(m)
#             m += 1
#         else:
#             m += 1

#     return lst1


# if __name__ == '__main__':
#     print(show_mult())

'''
Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
'''
# from random import randint

# def check_rep(m):

#     lst1 = [randint(1, 15) for i in range(m)]
#     lst_result = []

#     for i in lst1:
#         if lst1.count(i) == 1:
#             lst_result.append(i)

#     return f'{lst_result} - неповторяющихся элементы исходной последовательности {lst1}'


# if __name__ == '__main__':
#     print(check_rep(int(input('Введите количеество элементов последовательности: '))))

'''
Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

Пример:

- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
'''
# from random import randint
# from sympy import symbols
# from math import prod


# def make_expr(k):

#     koeff=[randint(0, 100) for i in range(k)]+[randint(1, 100)]
#     x = symbols('x')

#     pilunomial = (sum(map(prod, zip(koeff, [x**i for i in range(k + 1)]))), '= 0')

#     with open("pilunomial.txt", "w") as file:
#         file.write(str(pilunomial))


# if __name__ == '__main__':
#     make_expr(int(input('Задайте коэффициент k: ')))

