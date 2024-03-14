# 3. Faça um programa que recebe o salário de um colaborador e o reajuste segundo o
# seguinte critério, baseado no salário atual:
# 1) salários até R$ 280,00 (incluindo) : aumento de 20%
# 2) salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# 3) salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# 4) salários de R$ 1500,00 em diante : aumento de 5%

# Após o aumento ser realizado, informe na tela:

# a) o salário antes do reajuste;
# b) o percentual de aumento aplicado;
# c) o valor do aumento;
# d) o novo salário, após o aumento.

salario = float(input("\nDigite o seu salário: "))
percentual = 0

if(salario <= 280):
    percentual = '20%'
    aumento = salario * 0.20

elif(salario > 280 and salario <= 700):
    percentual = '15%'
    aumento = salario * 0.15

elif(salario > 700 and salario <= 1500):
    percentual = '10%'
    aumento = salario * 0.10

elif(salario > 1500):
    percentual = '5%'
    aumento = salario * 0.05

print("-----------------------------------------------------")

print(f"\nSalário antes do reajuste: R${salario:,.0f},00")

print("\nO percentual aplicado foi: ", percentual)

print("\nValor do aumento: ", aumento)

print(f"\nSalário depois do aumento R${salario + aumento:,.0f},00")




