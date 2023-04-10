""" def calc1(a, b):
    return a + b

def calc2(a, b):
    return a * b

def math(op, x, y):
    print(op (x, y))

calc3 = lambda a, b: a + b

math(calc1, 3, 4)
math(calc2, 3, 4)
math(calc3, 3, 4) """

# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = list()

# for i in data:
#     if i % 2 == 0:
#         res.append((i, i**2))
# print(res)

def select(f, col):
    return [f(x) for x in col]

def where(f, col):
    return [x for x in col if f(x)]

data = [1, 2, 3, 5, 8, 15, 23, 38]
res = select(int, data)
print(res)
res = where(lambda x: x % 2 == 0, res)
print(res)
res = list(select(lambda x: (x, x**2), res))
print(res)