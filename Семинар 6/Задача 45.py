# Два различных натуральных числа n и m 
# называются дружественными, 
# если сумма делителей числа n (включая 1, но исключая само n) 
# равна числу m и наоборот. 
# Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных чисел,
# каждое из которых не превосходит k.
# Программа получает на вход одно натуральное число k,
# не превосходящее 105.
# Программа должна вывести все пары дружественных чисел,
# каждое из которых не превосходит k. 
# Пары необходимо выводить по одной в строке, разделяя пробелами.
# Каждая пара должна быть выведена только один раз
# (перестановка чисел новуюпару не дает).
# Ввод:   Вывод:
# 300     220 284

k = int(input())

def srch_sum_del(num):
    summa = 0
    for delitel in range(1, num // 2 + 1):
        if num % delitel == 0:
            summa += delitel
    return summa

for i in range(1,k):
    sum_i = srch_sum_del(i)
    if k > sum_i > i:
        sum_second = srch_sum_del(sum_i)
        if sum_second == i:
            print(i, sum_i)