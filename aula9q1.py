# 1. A prefeitura de Ouro Preto contratou você para fazer um programa que calcule os
# valores do IPTU de imóveis da cidade, conforme o tipo do loteamento e a área dos
# mesmos. Deverão ser considerados apenas dois tipos de loteamento: 1 e 2. Para cada
# tipo de loteamento, se a área do imóvel for menor que 200 m2, efetua-se um cálculo de
# IPTU; se for maior ou igual a 200 m2, efetua-se outro cálculo de IPTU. A tabela abaixo
# mostra como o cálculo deve ser efetuado para cada caso.

# Faça um programa que leia o tipo de um loteamento e a área do mesmo e apresente o
# valor do IPTU de um determinado imóvel de Ouro Preto, calculado conforme a tabela
# acima.

loteamento = int(input("\nDigite o tipo loteamento: "))
area = int(input("\nDigite a área do loteamento: "))
IPTU = 0

if(loteamento == 1 and area < 200):
    IPTU = area * 1.0

elif(loteamento == 1 and area >= 200):
    IPTU = area * 1.2

elif(loteamento == 2 and area < 200):
    IPTU = area * 1.1

elif(loteamento == 2 and area >= 200):
    IPTU = area * 1.3

print(f"\nO valor do IPTU do lote é: {IPTU:,.2f}")