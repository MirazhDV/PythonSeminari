# Python map() — это встроенная функция, 
# которая позволяет обрабатывать и преобразовывать
# все элементы в итерируемом объекте
# без использования явного цикла for,
# методом, широко известным как сопоставление (mapping).
# map() полезен, когда вам нужно применить
# функцию преобразования к каждому элементу
# в коллекции или в массиве
# и преобразовать их в новый массив.

""" list_1 = [x for x in range (1, 20)]
print(list_1)

list_1 = list(map(lambda x: x + 10, list_1))
print(list_1) """

data = '12 23 4 546 6 234 32'
data = list(map(int, data.split())) #split преобразует строку в список через ",", но в скобках можно изменить разделитель