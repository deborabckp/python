#3. Faça um programa que pergunte quanto você ganha por hora e o número de horas
#trabalhadas por semana. Calcule e mostre seu salário por semana.

valorDaHora = float(input("\nDigite quando você ganha por hora: "))
numHoras = int(input("\nDigite o número de horas que você trabalha: "))
salarioSemanal = numHoras * valorDaHora

print(f"O seu salário semanal é: R${salarioSemanal:,.2f}")
