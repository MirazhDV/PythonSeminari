# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.
# Ввод:           Вывод:
# 1 2 3 2 3       2

from random import randint as rd
n = int(input())
list_n = [rd(1,9) for i in range(n)]
ecsept_index = []
count_n = 0
print(list_n)
for i in range(n-1):
    for j in range(i+1,n):
        if list_n[i] == list_n[j] and i not in ecsept_index and j not in ecsept_index:
            count_n += 1
            ecsept_index.append(i)
            ecsept_index.append(j)
            print(f'{list_n[i]}(индекс {i}), {list_n[j]}(индекс {j})')

print(count_n)