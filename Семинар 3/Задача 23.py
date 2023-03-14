# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)

massiv = [0, -1, 5, 2, 3]
count = 0
elem = ""
for i in range(len(massiv)-1):
    if massiv[i+1] > massiv[i]:
        count += 1
        elem = elem + ', ' + str(massiv[i]) + ' < ' + str(massiv[i+1])
print(count, elem)