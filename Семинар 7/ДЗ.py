# Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто,
# насколько легко он их придумывает.
# Вам стоит написать программу. Винни-Пух считает, что ритм есть,
# если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
# Фраза может состоять из одного слова, если во фразе несколько слов,
# то они разделяются дефисами. Фразы отделяются друг от друга пробелами.
# Стихотворение Винни-Пух вбивает в программу с клавиатуры.
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке 
# и “Пам парам”, если с ритмом все не в порядке.
# Ввод:                                        Вывод:
# пара-ра-рам рам-пам-папам па-ра-па-дам       Парам пам-пам

poem = input("Введите стихотворение: ")
phrases = poem.split()
vowels_count = None
count_vowels = lambda word: len(list(filter(lambda c: c.lower() in 'аеиоуюя', word)))
for phrase in phrases:
    words = phrase.split("-")
    phrase_vowels_count = sum(map(count_vowels, words))
    if vowels_count is None:
        vowels_count = phrase_vowels_count
    elif phrase_vowels_count != vowels_count:
        print("Пам парам")
        break
    else:
        print("Парам пам-пам")

""" poem = input("Введите стихотворение: ")
phrases = poem.split()
for phrase in phrases:
    words = phrase.split("-")
    vowels_count = 0
    for word in words:
        for letter in word:
            if letter.lower() in "аеиоуюя":
                vowels_count += 1
    print(f"Фраза '{phrase}' содержит {vowels_count} слогов") """

# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию,
# вычисляющую элемент по номеру строки и столбца.
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
# которые должны быть распечатаны.
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
# Примечание: бинарной операцией называется любая операция,
# у которой ровно два аргумента,
# как, например, у операции умножения.
# Ввод:                                       Вывод:
# print_operation_table(lambda x, y: x * y)   1   2   3   4   5   6
#                                             2   4   6   8  10  12
#                                             3   6   9  12  15  18
#                                             4   8  12  16  20  24
#                                             5  10  15  20  25  30
#                                             6  12  18  24  30  36

""" def print_operation_table(operation, num_rows=6, num_columns=6):
    for i in range(1, num_rows + 1):
        for j in range(1, num_columns + 1):
            print(str(operation(i, j)).rjust(4), end= ' ')
        print()
print_operation_table(lambda x, y : x * y) """