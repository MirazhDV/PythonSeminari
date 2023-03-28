# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.
# Ввод:                 Ввод:
# 5                     5
# 1 2 3 4 5             1 5 1 5 1
# Вывод:                Вывод:
# 0                     2

from random import randint
n = int(input())
list_n = [randint(1,9) for i in range(n)]
count_n = 0
for i in range(n-1):
    if list_n[i-1] < list_n[i] > list_n[i+1]:
        count_n += 1
print(list_n)
print(count_n)

""" a = int(input())
list_a = [randint(1,9) for i in range(a)]
print(list_a)
print(len([i for i in range(1,len(list_a) - 1) if list_a[i] > list_a[i-1] and list_a[i] > list_a[i+1]])) """