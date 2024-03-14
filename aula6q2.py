# 2. Faça um Programa que peça um número inteiro e determine se ele é par ou ímpar. Dica:
# utilize o operador módulo (resto da divisão).

numint = int(input("Digite um número: "))

if((numint % 2) == 0):
    print("Número par")

else:
    print("Número ímpar")