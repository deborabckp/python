# 1. Faça um programa que leia um número e, caso ele seja maior ou igual a zero, calcule e
# mostre o número digitado ao quadrado. Caso ele seja menor que zero, mostre o dobro deste
# número.

numero = int(input("Digite um número inteiro: "))

if(numero >= 0):
    print(numero ** 2)

else:
    print(numero * 2)
