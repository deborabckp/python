# 3. Elaborar um programa que apresente o valor da conversão em real (R$) de um valor lido
# em dólar (US$). O programa deve solicitar o valor da cotação do dólar e também a
# quantidade de dólares disponíveis com o usuário.

cotacaoDolar = float(input("\nDigite a cotação do dólar atual: "))
quantDolares = float(input("\nDigite a quantidade de dólares disponíveis: "))
conversao = quantDolares * cotacaoDolar

print(f"O valor em real é: R${conversao:,.2f}")
