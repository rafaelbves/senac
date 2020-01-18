
"""
#EXE 01

x=2
while x <=5:
    print(x)
    x=x+1
"""
"""
#EXE O2

fim = int(input("Digite o último numero: "))
x=1
while x<= fim:
    print (x)
    x=x+1
"""
"""
#EXE 03

fim = int(input("digite o ultimo numero: "))
x = 0
while x <= fim:
    if x % 2 != 0:
        print (x)
    x = x+1
"""
"""
#EXE 04

fim = 0
x = 0
while fim<=10:
    x = fim*3
    print (x)
    x = x + 1
    fim = fim + 1
"""
"""
#EXE 05

n = 1
soma = 0
while n <= 10:
    x = int(input("Digite o %d número: " %n))
    soma += x
    n = n + 1
print("soma: %d" %soma)
"""
"""
#EXE 06

soma = 0
n = 0
while True:
    x = int(input("Digite o numero (0 sai): "))
    if x == 0:
        break
    else:
        n += 1
    soma += x
print("Média: %5.2f" %(soma/n))
"""