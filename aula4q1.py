#1. Faça um programa que peça 2 números inteiros e um número real. Calcule e mostre:
#a) o produto do dobro do primeiro com metade do segundo;
#b) a soma do triplo do primeiro com o terceiro;
#c) o terceiro elevado ao cubo.

numero1 =  int(input("\nDigite um número inteiro: "))
numero2 =  int(input("\nDigite outro número inteiro: "))
numero3 =  float(input("\nDigite um número real: "))
produto = (numero1 * 2) * (numero2 / 2)
soma =  (numero1 * 3) + numero3
potencia = numero3 ** 3

print(f"\nProduto: {produto:,.2f}\nSoma: {soma:,.2f}\nPotenciação: {potencia:,.2f}")
