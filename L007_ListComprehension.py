# Лекция 3

# /5
# [exp for item in iterable]
array = [item + 2 for item in range(6)]
print(array)  # [2, 3, 4, 5, 6, 7]

list2 = []
for i in range(1, 101):
    if i % 2 == 0:
        list2.append(i)
print(list2)  # [2, 4, 6, ..., 98, 100]

list2 = []
for i in range(1, 21):
    list2.append(i)
print(list2)  # [1, 2, 3, ..., 19, 20]
list2 = [i for i in range(1, 21)]
print(list2)   # [1, 2, 3, ..., 19, 20]

# /6
list2 = [(i, i * 2) for i in range(1, 5)]
print(list2)  # [(1, 2), (2, 4), (3, 6), (4, 8)]

def cube(x):
    return x ** 3

list2 = [cube(i) for i in range(1, 11) if not i % 2]
print(list2)  # [8, 64, 216, 512, 1000]
list2 = [(i, cube(i)) for i in range(1, 11) if not i % 2]
print(list2)  # [(2, 8), (4, 64), (6, 216), (8, 512), (10, 1000)]

# /7
# [exp for item in iterable (if conditional)]
my_list = [1, 3, 7, 12, 8, 9, 16, 5]
array = [i * 3 for i in my_list if i % 2]
print(array)  # [3, 9, 21, 27, 15]

list3 = []
for i in range(1, 51):
    if i % 2 == 0:
        list3.append(i)
print(list3)  # [2, 4, 6, ..., 48, 50]


print(list3)  # [1, 2, 3, ..., 19, 20]
list3 = [i for i in range(1, 21)]
print(list3)   # [1, 2, 3, ..., 19, 20]

# /8
# [exp <if conditional> for item in iterable (if conditional)]
