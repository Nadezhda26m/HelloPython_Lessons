# Лекция 3

# /9
f = open('file2.txt', 'r')  # или
# path = 'C:/Users/.../file2.txt'
# f = open(path, 'r')
data = f.read() + ' '
f.close()
print(data)  # 1 2 15 8 22 5 9 18 83 11

numbers = []
while data != '':
    space_pos = data.index(' ')
    numbers.append(int(data[:space_pos]))
    data = data[space_pos + 1:]
out = []
for e in numbers:
    if not e % 2:
        out.append((e, e ** 2))
print(out)  # [(2, 4), (8, 64), (22, 484), (18, 324)]

# /10
def select(f, col):
    return [f(x) for x in col]

def where(f, col):
    return [x for x in col if f(x)]

data = '1 2 3 5 8 15 23 38'.split()
res = select(int, data)
print(res)  # [1, 2, 3, 5, 8, 15, 23, 38]
res = where(lambda e: not e % 2, res)
print(res)  # [2, 8, 38]
res = select(lambda e: (e, e ** 2), res)
print(res)  # [(2, 4), (8, 64), (38, 1444)]

# /11 map
li = [x for x in range(1, 13)]
print(li)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# li = map(lambda x: x + 10, li)
# print(type(li))  # class 'map'
li = list(map(lambda x: x + 10, li))
print(li)  # [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]

# /12
data = list(map(int, input('Введите числа: ').split()))
# Введите числа: 4 5 6 4 3 45
print(data)  # [4, 5, 6, 4, 3, 45]

data = map(int, input('Введите числа: ').split())
for e in data:
    print(e)  # 1  2  3

data = map(int, '1 2 3'.split())
for e in data:
    print(e)  # 1  2  3
print('--')  # --
for e in data:
    print(e)  # (пусто)

data = list(map(int, '1 2 3'.split()))
for e in data:
    print(e)  # 1  2  3
print('--')  # --
for e in data:
    print(e)  # 1  2  3

# /13
def where(f, col):
    return [x for x in col if f(x)]

data = '1 2 3 5 8 15 23 38'.split()
# ['1', '2', '3', '5', '8', '15', '23', '38']
res = map(int, data)  # map
res = where(lambda e: not e % 2, res)  # [2, 8, 38]
res = list(map(lambda e: (e, e ** 2), res))
print(res)  # [(2, 4), (8, 64), (38, 1444)]

# /14 filter
data = [x for x in range(10)]
# res = filter(lambda x: not x % 2, data)  # filter object
res = list(filter(lambda x: not x % 2, data))
print(res)  # [0, 2, 4, 6, 8]

# /15
data = '1 2 3 5 8 15 23 38'.split()
# ['1', '2', '3', '5', '8', '15', '23', '38']
res = map(int, data)  # map object
res = filter(lambda e: not e % 2, res)  # filter object
res = list(map(lambda e: (e, e ** 2), res))
print(res)  # [(2, 4), (8, 64), (38, 1444)]
