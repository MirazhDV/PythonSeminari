""" number1 = 1123
number2 = 2234

if number1>number2: #True
  print(number1)
else: #False
  print(number2)
"""
""" 
number1 = 210
number2 = 2000
max = number1

if max<number2:
  max=number2
  
print(max) 
"""
""" 
n1 = 11111
n2 = 2221
n3 = 3333
n4 = 4444

min = n1

if min > n2:
  min = n2
if min > n3:
  min = n3
if min > n4:
  min = n4

print(min)
"""
""" 
number = 15
sum = 0

while number > 0:
  if (number%2) == 0:
    print(number)
    sum = sum + number
  number = number - 1

print('Сумма четных чисел', sum)
"""
""" 
distance = 1111
men1 = 1
men2 = 2
dog = 5
direction = 1
count = 0

while distance>5:
    if direction == 1:
        time = distance/(dog+men1)
        count = count + 1
        direction = 2
    else: # direction == 2
        time = distance/(dog+men2)
        count = count + 1
        direction = 1
    distance = distance - time*(men1 + men2)

print(count)
"""