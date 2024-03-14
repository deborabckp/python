# 1. Construa um programa para determinar se o indivíduo está com um peso favorável. Essa
# situação é determinada através do IMC (Índice de Massa Corpórea), que é definida como
# sendo a relação entre o peso (PESO) e o quadrado da Altura (ALTURA) do indivíduo
# obedecendo a seguinte fórmula:
#imc = peso / altura²

peso = float(input("\nDigite o seu peso: "))
altura = float(input("\nDigite sua altura: "))
IMC = peso / altura ** 2

if(IMC < 20):
    print("\nAbaixo do peso\n")
    print(f"{IMC:,.2f}")

elif(IMC > 20 and IMC <= 25):
    print("\nPeso normal\n")
    print(f"{IMC:,.2f}")

elif(IMC > 25 and IMC <= 30):
    print("\nSobrepeso\n")
    print(f"{IMC:,.2f}")

elif(IMC > 30 and IMC <= 40):
    print("\nObeso(a)\n")
    print(f"{IMC:,.2f}")

elif(IMC > 40):
    print("\nObeso mórbido\n")
    print(f"{IMC:,.2f}")