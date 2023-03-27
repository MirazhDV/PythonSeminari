"""
# Задача 1. За день машина проезжает n километров. Сколько дней нужно, чтобы проехать m километров?

# S = V*t; V = S/t; t = S/V;

n = 500
m = 1150

print (int(m/n))
"""

# Задача 3. В школе набрали 3 математических класса и оборудовали новыми партами.
# По 2 учащихся на 1 парту, количество учащихся известно.
# Выведите наименьшее необходимо количество парт.

""" a1 = int(input("Количество учеников в 1м классе:"))
a2 = int(input("Количество учеников в 2м классе:"))
a3 = int(input("Количество учеников в 3м классе:"))

print((((a1+1)+(a2+1)+(a3+1))//2)) """

""" math = '2 + 2 = 4'
print(f"{math}\n{math}\n{math}") """

""" dal = int(input())
sdacha = dal - 2.5 * 38
if sdacha < 0:
    print("mala denyak")
else:
    sdacha = int(sdacha)
    print(sdacha) """

""" name = input()
cena = int(input())
ves = int(input())
dal = int(input())
itogo = cena * ves
sdacha = dal - ves * cena
if sdacha < 0:
    print("mala denyak")
else:
    itogo = int(itogo)
    sdacha = int(sdacha)
    print(f"Чек\n{name} - {ves}кг - {cena}руб/кг\nИтого: {itogo}руб\nВнесено: {dal}руб\nСдача: {sdacha}руб") """

""" n = int(input())
print("Купи слона!\n" * n) """

""" n = int(input())
punishment = input()
print(f'Я больше никогда не буду писать "{punishment}"!\n' * n) """

""" n = int(input("minut "))
m = int(input("detey "))
eda = n * m / 2
eda = int(eda)
print(eda) """

""" name = input()
shkaf = int(input())  #832
gruppa = shkaf / 100 
nomer = shkaf % 10 
krovatka = shkaf / 10 % 10 
gruppa = int(gruppa)
nomer = int(nomer)
krovatka = int(krovatka)
print(f"Группа №{gruppa}.\n{nomer}. {name}.\nШкафчик: {shkaf}.\nКроватка: {krovatka}.") """

""" n = int(input())
print(f"{n // 100 % 10}{n // 1000 % 10}{n % 10}{n // 10 % 10}") """

""" n1 = int(input())
n2 = int(input())
print(f"{(n1 // 100 % 10 + n2 // 100 % 10) % 10}{(n1 // 10 % 10 + n2 //10 % 10) % 10}{(n1 % 10 + n2 % 10) % 10}") """

""" deti = int(input())
vsego = int(input())
kaghdomu = vsego / deti
ostatok = vsego % deti
kaghdomu = int(kaghdomu)
ostatok = int(ostatok)
print(f"{kaghdomu}\n{ostatok}") """

""" kra = int(input())
zel = int(input())
sin = int(input())
maximum = (kra + sin) + 1
maximum = int(maximum)
print(maximum) """

""" n = int(input())  
m = int(input())  
t = int(input())  
hours = t % (60 * 24)# // 60)
minutes = ((t + m) % 60)
print(f"{hours}:{minutes}") """

""" n = int(input())
m = int(input())
t = int(input())
hours = t % (60 * 24) // 60
minutes = t % 60
delivery_hours = n + hours
delivery_minutes = m + minutes
if delivery_minutes >= 60:
    delivery_hours += 1
    delivery_minutes -= 60
if delivery_hours >= 24:
    delivery_hours -= 24
if delivery_hours < 10 and delivery_minutes < 10:
    print(f"0{delivery_hours}:0{delivery_minutes}")
elif delivery_hours > 10 and delivery_minutes < 10:
    print(f"{delivery_hours}:0{delivery_minutes}")
elif delivery_hours < 10 and delivery_minutes > 10:
    print(f"0{delivery_hours}:{delivery_minutes}")
else:
    print(f"{delivery_hours}:{delivery_minutes}") """


""" a = int(input())
b = int(input())
c = int(input())
s = b - a
t = s / c
print(t) """
""" 
d = int(input())
b = str(input())
decimal_num = int(b, 2)
summa = d + decimal_num
print(summa) """

c = str(input())
k = int(input())
decimal_num = int(c, 2)
print(decimal_num)
if k % 100 == 0:
    sdacha = k - decimal_num
sdacha = int(sdacha)
print(sdacha)