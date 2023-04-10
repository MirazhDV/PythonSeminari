colors = ['red', 'green', 'blue']
data = open('file.txt', 'a') # открываемый файл, режим обращения
data.writelines(colors) # разделителей не будет
data.close() #используется для закрытия файла, чтобы разорвать подключение файловой переменной с файлом на диске.

path = 'file.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()

colors = ['red', 'green', 'blue']
data = open('file.txt', 'w') # открываемый файл, режим обращения
data.writelines(colors) # разделителей не будет
data.close()
