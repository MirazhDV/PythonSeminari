# Дано натуральное число *N* 
# и последовательность из *N* элементов. 
# Требуется вывести эту последовательность 
# в обратном порядке.

def chislo(n):
    if n == 0:
        return 'a'
    k = int(input())
    return chislo(n - 1) + f' {k}'
numb = int(input())
print(chislo(numb))