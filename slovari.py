#Коллекция объектов с доступом по ключу

d = {}
d = dict() #Создание пустого словаря
d['q'] = 'qwerty' #в словаре по ключу 'q' доступно значение 'qwerty'
print(d)
print(d['q']) #вывод элемента q из словаря d

dictionary = {'up':'vverh', 'down':'↓'}
""" print(dictionary)
print(dictionary['down'])
dictionary['up'] = '<=' #элемент по ключу up заменить на <=
print(dictionary)

del dictionary['down'] #удаление элемента
dictionary[895] = 2394203
print(dictionary) """

for item in dictionary:
    #print(item) - поэлементный вывод словаря
    print('{}: {}'.format(item, dictionary[item])) #вывод ключа, в словаре по [ключу] в формате '{}: {}'

for (k, v) in dictionary.items():
    print(k, v) #при dictionary.items k это ключ, а v это значение ключа