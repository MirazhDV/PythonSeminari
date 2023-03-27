# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример: - [2, 3, 4, 5, 6] => [12, 15, 16];
#         - [2, 3, 5, 6] => [12, 15]

""" from random import randint
n = int(input("Количество элементов: "))
a = [randint(1,10) for i in range(1,n+1)]
print (a)
k = int(input())
m = abs(k - a[0]) # модуль числа
number = a[0]
for i in range(1, len(a)):
    if m > abs(a[i] - k):
        m = abs(a[i] - k)
number = a[i]
print(number) """

# points_en = {1: 'AEIOULNSTR', 2: 'DG', 3: 'BCMP', 4: 'FHVWY', 5: 'K', 8: 'JZ', 10: 'QZ'}
# points_ru = {1: 'АВЕИНОРСТ', 2: 'ДКЛМПУ', 3: 'БГЁЬЯ', 4: 'ЙЫ', 5: 'ЖЗХЦЧ', 8: 'ШЭЮ', 10: 'ФЩЪ'}
# word = input().upper() # переводим все буквы в верхний регистр
# count = 0
# for i in word:
#     if i in 'QWERTYUIOPASDFGHJKLZXCVBNM':
#         for j in points_en:
#             if i in points_en[j]:
#                 count = count + j
#             else:
#                 for j in points_en:
#                     if i in points_ru[j]:
#                         count = count + j
# print(count)