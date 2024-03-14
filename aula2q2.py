#2. Fazer um programa para ler dois números inteiros, calcular e imprimir:
#a) A soma dos dois números
#b) A subtração do primeiro pelo segundo
#c) A multiplicação dos dois números
#d) A divisão do primeiro número pelo segundo
#e) O resto da divisão do primeiro pelo segundo
#f) O primeiro número elevado ao quadrado

numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite outro número: "))
soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2
restodivisao = numero1 % numero2
elevado = numero1 ** 4

print(f"\nSOMA: {soma}\nSUBTRAÇÃO: {subtracao}\nMULTIPLICAÇÃO: {multiplicacao}\n")
print(f"DIVISÃO: {divisao}\nRESTO DA DIVISÃO: {restodivisao}\nPOTENCIAÇÃO: {elevado}")
