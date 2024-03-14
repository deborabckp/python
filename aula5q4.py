# 4. Faça um programa que receba o valor do salário de um funcionário e o valor do
# salário mínimo, calcule e imprima quantos salários mínimos o funcionário recebe.

salarioFuncionario = float(input("\nDigite o valor do seu salário: "))
salarioMinimo = float(input("\nDigite o valor do salário mínimo: "))

print(f"\nO funcionário recebe {salarioFuncionario / salarioMinimo:,.1f} salário(s) mínimo(s)\n")