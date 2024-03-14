# 3. Escreva um programa que leia 3 números e imprima o maior e o menor na mesma mensagem.

n1 = int(input("Digite um número inteiro: "))
n2 = int(input("Digite outro número inteiro: "))
n3 = int(input("Digite mais um número inteiro: "))
maior = n1
menor = n1

if(n2 < menor):
    menor = n2

elif(n2 > maior):
    maior = n2

if(n3 < menor):
    menor = n3

elif(n3 > maior):
    maior = n3

print(f"O {maior} é o maior número e o {menor} é o menor número")