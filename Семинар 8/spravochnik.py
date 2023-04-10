info = 'Команды: \n Показать всё: 1 \n Поиск: 2 \n Добавить: 3 \n Удалить: 4 \n Изменить: 5 \n Выход: 0'

def del_empty():
    df = open('spravochnik.txt')
    lines = df.readlines()
    non_empty_lines = (line for line in lines if not line.isspace())
    df_2 = open('spravochnik.txt', 'w')
    df_2.writelines(non_empty_lines)
    df.close()
    df_2.close()

def show():
    df = open('spravochnik.txt', 'r')
    for line in df.readlines():
        print(line)
    df.close()
    command()

def find():
    df = open('spravochnik.txt')
    str = input('Найти: ')
    count = 0
    lines = df.readlines()
    for line in lines:
        if str in line:
            print(line, end='')
            count += 1
    if count == 0:
        print('Нет такого')
    df.close()
    command()

def new():
    df = open('spravochnik.txt', 'a')
    print('Введите новую инфу: ')
    df.write(f'\n {input()}')
    df.close()
    del_empty()
    command()

def delete():
    df = open('spravochnik.txt')
    str = input('Удалить: ')
    count = 0
    lines = df.readlines()
    str_for_delete = ''
    for line in lines:
        if str in line:
            print('Удалится ')
            print(line, end='')
            str_for_delete = line
            line = ''
            count += 1
    if count == 0:
        print('Нет такого')
        df.close()
        command()
    else:
        acces = input('\n Подтвердите удаление (да\нет): ')
        if acces.lower() == 'да':
            df.close()
            df = open('spravochnik.txt', 'r').read()
            df = df.replace(str_for_delete, '')
            df_2 = open('spravochnik.txt', 'w')
            df_2.write(df)
            df_2.close()
            command()
        else:
            df.close()
            command()

def change():
    df = open('spravochnik.txt', 'r')
    str_for_change = input('Заменить: ')
    str = input('на ')
    spravochnik = df.read()
    spravochnik = spravochnik.replace(str_for_change, str)
    df.close()
    df = open('spravochnik.txt', 'w')
    df.write(spravochnik)
    df.close()
    command()

def command():
    comand = int(input('Номер команды: '))
    if comand == 1:
        show()
    elif comand == 2:
        find()
    elif comand == 3:
        new()
    elif comand == 4:
        delete()
    elif comand == 5:
        change()
    elif comand == 0:
        exit()
    else:
        exit()

start = input('Открыть справочник? (да\нет)')
if start.lower() == 'да':
    try:
        data = open('spravochnik.txt', 'r+')
    except:
        data = open('spravochnik.txt', 'a')
    data.close()
    print(info)
    command()