# Задача 26:  Напишите программу, 
# которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

""" def stepen(a,b):
    if b == 0:
        return 1
    return a * stepen(a,b - 1)
a1 = int(input("Число: "))
b1 = int(input("Степень: "))
print(stepen(a1,b1)) """

# Задача 28: Напишите рекурсивную функцию sum(a, b), 
# возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. 
# Также нельзя использовать циклы.
# *Пример:*
# 2 2
#     4 

def summa(a,b):
    if b == 0:
        return a
    return summa(a+1, b-1)
a1 = int(input("Первое слагаемое: "))
b1 = int(input("Второе слогаемое: "))
print(summa(a1,b1))