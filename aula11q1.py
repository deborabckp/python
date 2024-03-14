# 1. Faça um programa que solicite ao usuário uma nota, entre zero e dez. Deve-se verificar se
# essa nota é válida (ou seja, seu valor é menor que zero ou maior que dez). Caso a nota seja
# inválida, o programa deve continuar pedindo uma nota, até que o usuário informe um valor
# válido.

nota = int(input("Digite uma nota entre 0 e 10: "))

if(nota >= 0 and nota <= 10):
    print("Nota válida: ", nota)

while(nota < 0 or nota > 10):
    print("Nota inválida: ", nota)
    nota = int(input("Digite uma nota entre 0 e 10: "))
        
    print("\n", nota)
