# Дана последовательность из N целых чисел и число K.
# Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K – положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

# from random import randint
# list = [randint(1,10) for i in range(1,10)]
# print (list)
# k = int(input())
# print(list[-k:len(list)] + list[:-k])

# a = [1, 2, 3, 4, 5]
# k = 2
# print(a[k+1:] + a[:k+1])

lst = [1, 2, 3, 4, 5]
k = 2
for i in range(k):
    lst.insert(0, lst.pop(-1))
print(lst)