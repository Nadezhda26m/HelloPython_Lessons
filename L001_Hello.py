# a = 123
# b = 1.23
# print(type(a)) # class 'int'
# print(type(b)) # class 'float'

# print(type(a+b)) # class 'float'

# print()
# value = None # объявление пустой переменной
# print(type(value)) # class 'NoneType'

# value = None
# value = 12345
# print(type(value)) # class 'int'

# s = 'hello world' # инициализация строки
# print(s)
# print(type(s)) # class 'str'

# s = "hello 'world" # указать ' в строке
# s = 'hello "world' # указать " в строке
# s = 'hello \'world' # указать ' в строке
# s = 'hello \nworld' # переход на новую строку
# print(s) # вывод строки

# print(a,'-',b,'-', s) # вывод нескольких переменных
# print('{} - {} - {}'.format(a, b, s)) # шаблон
# print('{1} - {2} - {0}'.format(a, b, s)) # можно менять порядок
# print(f'{a} - {b} - {s}') # интерполяция строк
# print(f'{a} - {s} - {b}') # можно менять порядок

# f = True # логические переменные
# print(f)
# print(type(f)) # class 'bool'

# list = [] # объявление списка (аналог массива)
# list = ['1', '2', '3', 'hello'] # список строк
# list = ['1', '2', '3', 'hello', 1,2,4.5, True] # микс типов
#  col = ['1', '2', '3', 'hello'] # аккуратнее с пробелами
# print(list)
# print(col)
# print(type(list)) # class 'list'

# print('Введите а')
# a = input() # ввод данных
# print('Введите b')
# b = input()
# print(a, b)
# print('{} {}'.format(a, b))
# print(f'{a} {b}')

# print('Введите а')
# a = input() # 10
# print('Введите b')
# b = input() # 20
# print(a, ' + ', b, ' = ', a+b) # 10  +  20  =  1020

# print('Введите а')
# a = int(input()) # 12
# print('Введите b')
# b = int(input()) # 23
# print(a, ' + ', b, ' = ', a+b) # 12  +  23  =  35

# print('Введите а')
# a = float(input()) # 1.2
# print('Введите b')
# b = float(input()) # 3.4
# print(a, ' + ', b, ' = ', a+b) # 1.2  +  3.4  =  4.6

# a = int(input('Введите \nа: '))
# b = int(input('Введите \nb: '))
# c = a + b
# print('{} + {} = {}'.format(a, b, c)) # 11 + 22 = 33

# Арифметические операции
# a = +123
# # b = 321
# b = -321
# c = a + b
# print(c)

# a = 2
# b = 8
# # c = a - b
# # c = a * b
# c = a / b # вещественное число
# print(c)

# a = 12
# b = 8
# # c = a - b
# # c = a * b
# # c = a // b # деление в целых числах (1)
# c = a % b # остаток от деления (4)
# print(c)

# a = 2
# b = 8
# c = a ** b # возведение в степень (256)
# print(c)

# a = 1.3
# b = 3
# # c = a * b # 3.9000000000000004
# c = round(a * b) # 4 округление по математическим правилам
# print(c)

# a = 1.312312
# b = 3
# c = round(a * b, 5) # правила округления
# print(c)  # 3.93694

# # операции присваивания
# iter = 2 
# iter += 3 # iter = iter + 3 
# iter -= 4 # iter = iter - 4 
# iter *= 5 # iter = iter * 5
# iter /= 5 # iter = iter / 5 
# iter //= 5 # iter = iter // 5 
# iter %= 5 # iter = iter % 5 
# iter **= 5 # iter = iter ** 5

# a, b, c = 1, 2, 3
# # a: 1 b: 2 c: 3
# print('a: {} b: {} c: {}'.format(a, b, c))

# Логические операции
# >, >=, <=, ==, != 
# not, and, or – не путать с &, |, ^ 
# is, is not, in, not in
# gen

# a = 1 < 4 and 5 > 2
# a = 1 != 2
# print(a)

# a = 'qwe'
# b = 'qwe'
# print(a == b)

# a = [1,2]
# b = [1, 2]
# print(a == b)

# a = 1 < 3 < 5
# print(a)

# func = 1
# T = 4
# x = 123
# print(func<T>x)

# f = 1 > 2 or 4 < 6
# print(f)

# f = [1,2,3,4]
# print(2 in f)
# print(not 2 in f)
# # is_odd = f[0] % 2 == 0
# is_odd = not f[0] % 2 # остаток либо есть [1], либо нет [0]
# print(is_odd)

# Управляющие конструкции: if, if-else
# username = input('Введите имя: ')
# if username == 'Маша':
#     print('Ура, это же МАША!')
# else:
#     print('Привет, ', username)

# username = input('Введите имя: ')
# if username == 'Маша':
#     print('Ура, это же МАША!')
# elif username == 'Марина':
#     print('Я так ждала Вас, Марина!')
# elif username == 'Ильнар':
#     print('Ильнар - топ)')
# else: 
#     print('Привет, ', username)

# Управляющие конструкции: while
# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# # print(inverted) # 32
# else: # выполняется после завершения while
#     print('Пожалуй')
#     print('хватит )')
# print(inverted)

# Управляющие конструкции: for
# for i in 1, -2, 3, 4, 5:
#     print(i**2)

# list = [1,2,3,4,10,5]
# for i in list:
#     print(i)

# Оператор range
# r = range(5)
# for i in r:
#     print(i) # 0 … 4

# for i in range(1, 5):
#     print(i)  # 1 … 4

# for i in range(1, 10, 2):
#     print(i) # 1, 3, 5, 7, 9

# c = -20
# for i in range(100, 0, c):
#     print(i) # 100, 80, 60, 40, 20

# r = range(100, 0, -20)
# for i in r:
#     print(i) # 100, 80, 60, 40, 20

# for i in 'qwerty':
#     print(i)

# вложенные циклы
# line = ""
# for i in range(3):
#     line = ""
#     for j in range(5):
#         line += "*"
#     print(line)

# Действия со строками
# text = 'съешь ещё этих мягких французских булок' 
# print(len(text)) # 39 длина строки
# print('ещё' in text) # True наличие подстроки в строке
# print(text.isdigit()) # False все символы строки числа?
# print(text.islower()) # True все символы в нижнем регистре?
# print(text.replace('ещё','ЕЩЁ')) # замена элементов

# help(text.istitle) # подсказки (или ctrl + пробел)
# help(str)

# text = 'съешь ещё этих мягких французских булок'
# print(text[0]) # c
# print(text[1]) # ъ
# # print(text[len(text)]) # IndexError
# print(text[len(text)-1]) # к
# print(text[-5]) # б символы с конца
# print(text[:]) # print(text) сокращение от начала - до конца
# print(text[0:len(text)]) # print(text)
# print(text[:2]) # съ крайние значения можно не писать
# print(text[len(text)-2:]) # ок
# print(text[2:9]) # ешь ещё
# print(text[6:-18]) # ещё этих мягких
# print(text[0:len(text):6]) # сеикакл
# print(text[::6]) # сеикакл
# text = text[2:9] + text[-5] + text[:2] # ешь ещёбсъ
# print(text)

# # Списки: введение
# numbers = [1, 2, 3, 4, 5]
# print(numbers) # [1, 2, 3, 4, 5]

# numbers[0] = 10
# print(f'{len(numbers)} length') # 5 length
# print(numbers) # [10, 2, 3, 4, 5]
# for i in numbers:
#     i *= 2
#     print(i) # [20, 4, 6, 8, 10] построчный вывод
# print(numbers) # [10, 2, 3, 4, 5]

# ran = range(1, 6)
# print(type(ran)) # class 'range'
# numbers = list(ran)
# print(type(numbers)) # class 'list'
# print(numbers) # [1, 2, 3, 4, 5]
# numbers = list(range(1, 6)) # приведение типа range к типу list
# print(numbers) # [1, 2, 3, 4, 5]

# добавление и удаление элементов
# colors = ['red', 'green', 'blue']
# for e in colors:
#     print(e) # red green blue
# for e in colors:
#     print(e*2) # redred greengreen blueblue
# colors.append('gray') # добавить в конец
# print(colors == ['red', 'green', 'blue', 'gray']) # True
# colors.remove('red') # удалить элемент
# print(colors) # ['green', 'blue', 'gray']
# del colors[1] # удалить элемент
# print(colors) # ['green', 'gray']

# Функции
# def f(x):
#     return x ** 2
#
# def p(x):
#     if x == 1:
#         return 'Целое'
#     elif x == 2.3:
#         return 23
#     else:
#         return
#
# print(f(6))  # 25
#
# print(p(1))  # Целое
# print(p(2.3))  # 23
# print(p(28))  # None
# print(type(p(1)))  # str
# print(type(p(2.3)))  # int
# print(type(p(28)))  # NoneType

# Работа с выводом, инициализация нескольких переменных
# num1, num2 = '7', '15'
# print(num1, num2, sep=', ', end='; ')
# print(num1, num2, sep='~', end='---')
# print('два числа', num1, num2, sep=' * ')


# text = 'qwe1'
# res = text * 4
# print(res)
# res2 = text + text + text + text
# print(res2)

# Обмен значений переменных
# num1 = '7'
# num2 = '15'
# print(num1, num2)
# num1, num2 = num2, num1
# print(num1, num2)