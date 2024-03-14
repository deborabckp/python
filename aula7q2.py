# 2. Faça um programa que peça um número inteiro e determine se ele é par ou ímpar. Dica:
# utilize o operador módulo (resto da divisão).

number = int(input("Digite um número: "))

if(number % 2 == 0):
    print("Número par")

else:
    print("Número ímpar")