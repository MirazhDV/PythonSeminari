#Кортеж - это списко который невозможно изменить

t = () #пустой кортеж, type <tuple>

t = (1, 5, 3,) #в конце обязательно запятая
v = [1, 2, 3, 4]
print(v)
v = tuple(v)
print(v)
a, b, c, d = v #множественное присваивание
print(a, b, c, d) #вывод чисел посимвольно