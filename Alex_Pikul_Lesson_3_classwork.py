'''
1. На вход программе подаются две строки текста, содержащие по одному слову из перечня "камень", "ножницы", "бумага", "ящерица" или "Спок". 
На первой строке записан выбор Тимура, на второй – выбор Руслана.

Формат выходных данных
Программа должна вывести результат жеребьёвки: кто победил - Тимур или Руслан, или они сыграли вничью.

Примечание. Правила игры стандартные: ножницы режут бумагу. Бумага заворачивает камень. Камень давит ящерицу, а ящерица травит Спока, в то время как Спок 
ломает ножницы, которые, в свою очередь, отрезают голову ящерице, которая ест бумагу, на которой улики против Спока. Спок испаряет камень, а камень, разумеется, 
затупляет ножницы.

a=input()
b=input()
m = {'камень-камень': 'ничья', 'камень-ножницы': 'Тимур', 'камень-бумага': 'Руслан',
'камень-ящерица': 'Тимур', 'камень-Спок': 'Руслан', 'ножницы-ножницы': 'ничья',
'ножницы-бумага': 'Тимур', 'ножницы-камень': 'Руслан', 'ножницы-ящерица': 'Тимур',
'ножницы-Спок': 'Руслан', 'бумага-бумага': 'ничья', 'бумага-камень': 'Тимур',
'бумага-ножницы': 'Руслан', 'бумага-ящерица': 'Руслан', 'бумага-Спок': 'Руслан',
'ящерица-ящерица': 'ничья', 'ящерица-Спок': 'Тимур', 'ящерица-ножницы': 'Руслан',
'ящерица-бумага': 'Тимур', 'ящерица-камень': 'Руслан', 'Спок-Спок': 'ничья',
'Спок-ножницы': 'Тимур', 'Спок-бамага': 'Руслан', 'Спок-камень': 'Тимур',
'Спок-ящерица': 'Руслан'}
'''
# def show_result(a=input('Тимур выросил: '), b=input('Руслан выбросил: ')):

#     player_1 = 'Тимур'
#     player_2 = 'Руслан'
#     game_words = ['камень', 'ножницы', 'бумага', 'ящерица', 'Спок']
    
#     dist = (game_words.index(input()) - game_words.index(input())) % len(game_words)

#     return (('ничья', 'Тимур', 'Руслан')[dist and dist % 2 + 1])


# if __name__ == '__main__':
#     print(show_result())

'''
2. Орел и решка

Дана строка текста, состоящая из букв русского алфавита "О" и "Р". Буква "О" – соответствует выпадению Орла, а буква "Р" – соответствует выпадению Решки. 
Напишите программу, которая подсчитывает наибольшее количество подряд выпавших Решек.

Формат входных данных
На вход программе подается строка текста, состоящая из букв русского алфавита "О" и "Р".

Формат выходных данных
Программа должна вывести наибольшее количество подряд выпавших Решек.

Примечание. Если выпавших Решек нет, то необходимо вывести число
0
0.

Тестовые данные
Sample Input 1:
ОРРОРОРООРРРО
Sample Output 1:
3
Sample Input 2:
ООООООРРРОРОРРРРРРР
Sample Output 2:
7
Sample Input 3:
ООООРРРРОРОРРРРРРРРООРОРОРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРР
Sample Output 3:
31
'''
# def how_much(text):
    
#     n = 0
#     word = 'Р'

#     while text.count(word) != 0:
#         n += 1
#         word += 'Р'

#     return n


# if __name__ == '__main__':
#     print(how_much('ОРРОРОРООРРРО'))
#     print(how_much('ООООООРРРОРОРРРРРРР'))
#     print(how_much('ООООРРРРОРОРРРРРРРРООРОРОРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРР'))

'''
3. Искусственный интеллект Антон, созданный Гилфойлом, взломал сеть умных холодильников. Теперь он использует их в качестве серверов "Пегого дудочника". 
Помогите владельцу фирмы отыскать все зараженные холодильники.

Для каждого холодильника существует строка с данными, состоящая из строчных букв и цифр, и если в ней присутствует слово "anton" (необязательно рядом стоящие буквы,
 главное наличие последовательности букв), то холодильник заражен и нужно вывести номер холодильника, нумерация начинается с единицы

Формат входных данных
В первой строке подаётся число
n
n – количество холодильников. В последующих
n
n строках вводятся строки, содержащие латинские строчные буквы и цифры, в каждой строке от
5
5 до
100
100 символов.

Формат выходных данных
Программа должна вывести номера зараженных холодильников через пробел. Если таких холодильников нет, ничего выводить не нужно.

Формат входных данных
В первой строке подаётся число
n
n – количество холодильников. В последующих
n
n строках вводятся строки, содержащие латинские строчные буквы и цифры, в каждой строке от
5
5 до
100
100 символов.

Формат выходных данных
Программа должна вывести номера зараженных холодильников через пробел. Если таких холодильников нет, ничего выводить не нужно.

Sample Input 1:
6
222anton456
a1n1t1o1n1
0000a0000n00t00000o000000n
gylfole
richard
ant0n
Sample Output 1:
1 2 3
Sample Input 2:
9
osfjwoiergwoignaewpjofwoeijfnwfonewfoignewtowenffnoeiwowjfninoiwfen
anton
aoooooooooontooooo
elelelelelelelelelel
ntoneeee
tonee
253235235a5323352n25235352t253523523235oo235523523523n
antoooooooooooooooooooooooooooooooooooooooooooooooooooon
unton
Sample Output 2:
1 2 7 8
'''
# def find_virus(name):

    
#     list = ['222anton456', 'a1n1t1o1n1', '0000a0000n00t00000o000000n', 'gylfole', 'richard', 'ant0n']
#     n = len(list)
#     find = []

#     for i in range(n):
#         count = 0
#         for j in range(len(list[i])):
#             if name[count] == list[i][j]:
#                 count += 1
#             if count == 5:
#                 find.append(i+1)
#                 break
    
#     print(find)


# if __name__ == '__main__':
#     find_virus('anton')

'''
4. Создать текстовый файл, записать в него построчно данные, которые вводит пользователь. Окончанием ввода пусть служит пустая строка.
'''

# data = open('file.txt', 'w')

# while True:
#     str1 = input()
#     data.writelines(str1)
#     if str == '':
#         break





