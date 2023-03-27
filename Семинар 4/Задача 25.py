# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию .split()

""" fst = 'a a a b c a a d c d d'
scnd = fst.split()
thrd = []
for i in range(len(scnd)):
    if scnd[:i+1].count(scnd[i]) == 1:
        thrd.append(scnd[i])
    else:
        thrd.append(scnd[i] + '_' + str(scnd[:i].count(scnd[i])))
print(*thrd) """

""" fst = 'a a a b c a a d c d d'
scnd = fst.split()
for i in range(len(scnd)):
    if scnd[:-i - 1].count(scnd[-i - 1]) >= 1:
        scnd[-i - 1] = scnd[-i - 1] + '_' + str(scnd[:-i - 1].count(scnd[-i - 1]))
print(*scnd) """

string = str.upper('a a a b c a a d c d d')
print(string)
new_string = (string.split())
result = {}
for i in new_string:
    if i in result:
        print(f'{i}_{result[i]}', end=' ')
    else:
        print(i,end=' ')
    result[i] = result.get(i, 0) + 1