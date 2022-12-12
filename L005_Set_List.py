# Лекция 2

# Множества

a = {1, 2, 3, 5, 8}
b = {'2', '5', 8, 13, 21}
print(type(a)) # set
print(type(b)) # set

a = {1, 2, 3, 5, 8}
b = set([2, 5, 8, 13, 21])
c = set((2, 5, 8, 13, 21))
print(type(a)) # set
print(type(b)) # set
print(type(c)) # set
a = {1, 1, 1, 1, 1}
print(a) # {1}

colors = {'red', 'green', 'blue'}
print(colors) # {'red', 'green', 'blue'}
print(type(colors)) # <class 'set'>
colors.add('red')
print(colors) # {'red', 'green', 'blue'}
colors.add('gray')
print(colors) # {'red', 'green', 'blue','gray'}
colors.remove('red')
print(colors) # {'green', 'blue','gray'}
# colors.remove('red') # KeyError: 'red'
colors.discard('red') # ok
print(colors) # {'green', 'blue','gray'}
colors.clear() # { }
print(colors) # set()

a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy() # c = {1, 2, 3, 5, 8} Копия
u = a.union(b) # u = {1, 2, 3, 5, 8, 13, 21} Объединение
i = a.intersection(b) # i = {8, 2, 5} Пересечение
dl = a.difference(b) # dl = {1, 3} Разность
dr = b.difference(a) # dr = {13, 21}
q = a \
    .union(b) \
    .difference(a.intersection(b))
# {1, 21, 3, 13} Симметрическая разность

a = {1, 2, 3, 5, 8}
b = frozenset(a)
print(b) # frozenset({1, 2, 3, 5, 8})

# Списки

# 1/ Копирование списков
list1 = [1, 2, 3, 4, 5]
list2 = list1

for e in list1:
    print(e)  # 1 2 3 4 5

print()

for e in list2:
    print(e)  # 1 2 3 4 5

list1[0] = 123
list2[1] = 333

for e in list1:
    print(e)  # 123 333 3 4 5

print()

for e in list2:
    print(e)  # 123 333 3 4 5

# 2/ Операции с элементами списка

list1 = [1, 2, 3, 4, 5]

print(list1) # [1, 2, 3, 4, 5]
print(list1.pop()) # 5
print(list1) # [1, 2, 3, 4]
print(list1.pop()) # 4
print(list1) # [1, 2, 3]
print(list1.pop()) # 3
print(list1) # [1, 2]

list1 = [1, 2, 3, 4, 5]

print(list1)  # [1, 2, 3, 4, 5]
# print(list1.pop(2)) # 3
# print(list1) # [1, 2, 4, 5]
# print(list1.insert(2, 11))
# print(list1) # [1, 2, 11, 3, 4, 5]
print(list1.append(11))
print(list1)  # [1, 2, 3, 4, 5, 11]


