# 3. Escreva um programa que leia 3 números e imprima o maior e o menor na mesma
# mensagem.

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
n3 = int(input("Digite outro número: "))
maior = n1
menor = n1

if(n2 < menor):
    menor = n2

if(n2 > maior):
    maior = n2

if(n3 < menor):
    menor = n3

if(n3 > maior):
    maior = n3

print(f"O {maior} é o maior número e o {menor} é o menor número")

