""" #Содержат в себе неупорядоченные уникальные элементы
colors = {'red','green','blue'}
print(colors)
colors.add('gray') #добавление элемента
print(colors)
colors.remove('red') #удаление элемента
print(colors)
colors.discard('red') #отключение отображения элемента
print(colors)
colors.clear() #очистка множества
print(colors)
q = set() #создание пустого множества """

a = {1,2,3,4,5}
b = {2,4,7,21,12}
c = a.copy() #копирование
u = a.union(b) #объединение уникальныъ элементов
i = a.intersection(b) #добавление в i только повторяющихся элементов
d1 = a.difference(b) #элементы что есть в a, но нет в b
d2 = b.difference(a) #элементы что есть в b, но нет в a
q = a.union(b).difference(a.intersection(b)) #действия делаются по порядку
f = frozenset(a) #заморозка множества