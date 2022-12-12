# Лекция 3

# /1
def sum(x):
    return x + 10

def mult(x):
    return x ** 2

print(sum(mult(2)))

print(type(sum))  # function
sum2 = sum  # присваивание ссылки на функцию
print(type(sum2))  # function
print(sum(5))  # 15
print(sum2(5))  # 15

def math(op, x):
    print(op(x))

math(mult, 4)  # 16
math(sum2, 11)  # 21

# /2
def sum1(x, y):
    return x + y

def mult1(x, y):
    return x * y

def calc(op, a, b):
    print(op(a, b))
    # return op(a, b)

calc(mult1, 4, 6)  # 24
calc(sum1, 4, 8)  # 12

f = sum1
calc(f, 4, 8)  # 12

# /3
sum1 = lambda x, y: x + y
calc(sum1, 5, 8)  # 13
sum1 = lambda x, y: x + y + 1
calc(sum1, 5, 8)  # 14

# /4
calc(lambda p, m: p + m, 7, 11)  # 18
