# Написать функцию,
# которая принимает список строк
# и возвращает список строк,
# содержащих только одно слово,
# с использованием лямбда-функции

lst = ['aasdasd', 'asd asd', 'as', 'a s d f', 'asdasddqwe']
lst_2 = list(filter(lambda x: len(x.split()) == 1, lst))
print(lst_2)