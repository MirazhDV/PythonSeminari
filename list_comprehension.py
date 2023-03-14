#Генерация списков
# 1 способ
list_1 = []
for i in range(1,101):
    list_1.append(i)
print(list_1)

# 2 способ
list_2 = [i for i in range(1,101)]
print (list_2)

# 3 способ (только чётные числа)
list_3 = [i for i in range(1,101) if i%2==0]
print (list_3)

# 4 способ (выводить числа парно)
list_4 = [(i, i) for i in range(1,101) if i%2==0]
print (list_4)

# 5 способ (умножать каждое число на 2)
list_5 = [i*2 for i in range(11) if i%2==0]
print (list_5)