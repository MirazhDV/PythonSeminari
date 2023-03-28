def fib(n):
    if n in [0,1]:
        return 1
    return fib(n-1) + fib(n-2)

list_1 = []
k = int(input())
for i in range (1,k+1):
    list_1.append(fib(i))
print(list_1)

n = int(input())
print(fib(n))

""" def fib(n):
    if n == 0:
        return 0
    elif n ==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
print(fib(int(input("введите число")))) """