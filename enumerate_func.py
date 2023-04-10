# Функция enumerate() позволяет пронумеровать набор данных. Т.е. выводит индекс и элемент в этом ячейке.

users = ['user1', 'user2', 'user3']
data = list(enumerate(users))
print(data) # [(0, 'user1'), (1, 'user2'), (2, 'user3))]
