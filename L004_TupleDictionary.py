# Лекция 2

# Кортежи
t = ()
print(type(t))  # tuple
t = (1,)
print(type(t))  # tuple
t = (1)
print(type(t))  # int
t = (28, 9, 1990)
print(type(t))  # tuple
colors = ['red', 'green', 'blue']
print(colors)  # ['red', 'green', 'blue']
t = tuple(colors)
print(t)  # ('red', 'green', 'blue')

t = tuple(['red', 'green', 'blue'])
print(t[0])  # red
print(t[2])  # blue
# print(t[10]) # IndexError: tuple index out of range
print(t[-2])  # green
# print(t[-200]) # IndexError: tuple index out of range
for e in t:
    print(e)  # red green blue
# t[0] = 'black'  # TypeError: 'tuple' object does not support
# item assignment

t = tuple(['red', 'green', 'blue'])
red2, green2, blue3 = t
print('r:{} g:{} b:{}'.format(red2, green2, blue3))
# r:red g:green b:blue

# Словари

dictionary = {}
dictionary = \
    {
        'up': '↑',
        'left': '←',
        'down': '↓',
        'right': '→'
    }

print(dictionary)  # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
print(dictionary['left'])  # ←
print(dictionary['up'])  # ↑
# типы ключей могут отличаться

dictionary['left'] = '⇐'
print(dictionary['left'])  # ⇐
# print(dictionary['type']) # KeyError: 'type'

for k in dictionary.keys():
    print(k)  # up left down right

for v in dictionary.values():
    print(v)  # ↑ ⇐ ↓ →

for (k, v) in dictionary.items():
    print('{}: {}'.format(k, v))  # up: ↑ left: ⇐ down: ↓ right: →

del dictionary['down']  # удаление элемента

for item in dictionary:
    print('{}: {}'.format(item, dictionary[item])) # up: ↑ left: ⇐ right: →

