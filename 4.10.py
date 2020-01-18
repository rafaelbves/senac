# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 17:06:06 2019

@author: Aluno
"""
'''


Residencial = "R"
Comercial = "C"
Industrial = "I"


'''


tipo = input("qual o tipo de instalação? ")
consumo = float(input("qual o consumo? "))

if tipo == "R":
    if consumo <= 500:
        conta = consumo*0.40
    else:
        conta = consumo*0.65
elif tipo == "C":
    if consumo <= 1000:
        conta = consumo*0.55
    else:
        conta = consumo*0.60
else:
    if consumo <= 5000:
        conta = consumo*0.55
    else:
        conta = consumo*0.60
print("o valor da sua conta é ",conta)
        