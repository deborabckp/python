# 3. Faça um programa que leia o nome de um vendedor, o seu salário fixo e o total de
# vendas efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor ganha 15%
# de comissão sobre suas vendas efetuadas, informar o total a receber no final do mês,
# com duas casas decimais.

nomeVendedor = (input("\nDigite o seu nome: "))
salarioFixo = float(input("\nDigite o seu salário fixo: "))
totalVendas = float(input("\nDigite o total de vendas efetuadas no mês em dinheiro: "))
comissao = salarioFixo + 0.15 * totalVendas

print(f"\nO vendedor {nomeVendedor} irá receber R${comissao:,.2f} ao final do mês")
