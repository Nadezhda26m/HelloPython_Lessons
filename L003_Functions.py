# Лекция 2

# 1/
import L001_Hello

print(L001_Hello.p(1))

# 2/
import L001_Hello as lec1

print(lec1.p(1))

# 3/
def new_string(symbol, count):
    return symbol * count

print(new_string('!', 5))  # !!!!!
# print(new_string('!'))  # TypeError missing 1 required ...

# 4/
def new_string(symbol, count=3):
    return symbol * count

print(new_string('!', 5))  # !!!!!
print(new_string('!'))  # !!!
print(new_string(4))  # 12

# 5/
def concatenatio(*params):
    res: str = ""
    for item in params:
        res += item
    return res

print(concatenatio('a', 's', 'd', 'w'))  # asdw
print(concatenatio('a', '1', 'd', '2'))  # a1d2
# print(concatenatio(1, 2, 3, 4)) # TypeError: ...

# 6/ Рекурсия
def fib(n):
    if n in [1, 2]:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

list = []
for e in range(1, 10):
    list.append(fib(e))
print(list)  # 1 1 2 3 5 8 13 21 34
