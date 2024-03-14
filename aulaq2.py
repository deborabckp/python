# 2. Faça um programa que receba a quantidade de pessoas vacinadas no primeiro dia do
# mês e calcule a estimativa de vacinação mensal (OBS: considere o mês com 22 dias
# úteis).

pessoasVacinadas = int(input("\nDigite a quantidade de pessoas que foram vacinadas no dia primeiro do mês: "))
estimativa = pessoasVacinadas * 22

print(f"A estimativa de vacinação mensal é: {estimativa}\n")

