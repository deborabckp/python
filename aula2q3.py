#3. Faça um programa que solicite o salário de três servidoras e mostre a média de salário deles.

salario1 = float(input("Digite o seu salário:")) 
salario2 = float(input("Digite o seu salário:")) 
salario3 = float(input("Digite o seu salário:")) 
media = (salario1 + salario2 + salario3)/3

print(f"A média do salário é: {media:,.2f}")