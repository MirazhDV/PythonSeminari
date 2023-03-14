# Дан список чисел. 
# Определите, сколько в нем встречается различных чисел.
# Input [1,1,2,0,-1,3,4,4]
# Output [6]

from random import randint
n = int(input())
count = 0
list = []
for i in range(n):
    list.append(randint(-5,5))
print(list)
print(len(set(list))) # set функция подсчитывающая количество повторяющихся символов