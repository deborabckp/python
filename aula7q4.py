# 4. Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve
# calcular a média alcançada por aluno e apresentar:
# a) A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# b) A mensagem "Reprovado", se a média for menor do que sete;
# c) A mensagem "Aprovado com Distinção", se a média for igual a dez.

n1 = float(input("Digite a primeira nota parcial do aluno: "))
n2 = float(input("Digite a segunda nota parcial do aluno: "))
media = (n1 + n2) / 2

if(media >= 7 and media < 10):
    print("\nAPROVADE\n")

elif(media == 10):
    print("\nAPROVADE COM DISTINÇÃO\n")

else:
    print("\nREPROVADE\n")

