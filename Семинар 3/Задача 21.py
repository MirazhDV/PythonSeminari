# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

# dict_1 = [{"V": "S001"},{"V": "S002"},{"VI": "S001"},{"VI": "S005"},{"VII": " S005 "},{" V ":" S009 "},{" VIII ":" S007 "}]
# dict_2 = set()
# for i in dict_1:
#     for j in i:
#         dict_1.add(i[j]) #добавляет уникальное значение в словарь
# print(dict_2)

my_dict = {"V":"S001", "V":"S002", "VI":"S001", "VI":"S005", "VII":" S005 ", " V ":" S009 ", " VIII ":" S007 "}
unique_values = set()

for value in my_dict.values(): #values(значения словаря) можно заменить на case(ключи словаря)
    unique_values.add(value)

print(unique_values)