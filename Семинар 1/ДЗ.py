"""
# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

i = int(input("Введите трёхзначное число "))
sum = 0
if i>999 or i<100:
    print("введите ТРЁХзначное число, ну алло!")
else:
   while i > 0:
        ostatok = i % 10
        sum += ostatok
        i //= 10
print(sum)
"""
"""
# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. 
# Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, 
# что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# *Пример:*
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

S = int(input("Сколько сделали журавлей "))
p = int
c = int
k = int
if S > 3:
    p:int = S // 3 // 2
    c:int = p
    k:int = (p + c) * 2
    print(f"Петя сделал {p} шт., Серёжа сделал {c} шт., а Катя сделала {k} шт.")
else:
    print(f"Зачем программа? И так видно что их {S}")
"""
"""
# Задача 6: Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.
# *Пример:*
# 385916 -> yes
# 123456 -> no

i = int(input("6 значный номер билета: "))
sum1 = 0
sum2 = 0
if i>999999 or i<100000:
    print("Некорректный номер билета")
else:
    while i > 999:
        ostatok = i % 10
        sum1 += ostatok
        i //= 10
    while i > 0:
        ostatok = i % 10
        sum2 += ostatok
        i //= 10
print(sum1)
print(sum2)
if sum1 == sum2:
    print("yes")
else: 
    print("no")
"""

# Задача 8: Требуется определить,
# можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками
# (то есть разломить шоколадку на два прямоугольника).
# *Пример:*
# 3 2 4 -> yes
# 3 2 1 -> no

n = int(input("Размер шоколадки "))
m = int(input("на "))
k = int(input("И отломить надо "))

if k==n or k % n == 0:
    print("yes")
elif k==m or k % m == 0:
    print("yes")
elif k > n*m:
    print("no")
else:
    print("no")