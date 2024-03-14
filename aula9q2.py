# 2. Escreva um programa que leia a nota final de um aluno referente à disciplina de
# Introdução à Programação. Caso a nota seja maior ou igual a 6.0, o programa imprime
# uma mensagem dizendo que o aluno foi aprovado.
# No caso da nota ser menor que 6.0, o programa imprime uma mensagem informando
# que o aluno está em exame especial, e faz uma nova leitura de nota desse aluno,
# referente à nota do exame especial. Caso a nota do exame especial seja maior ou igual a
# 6,0, o programa imprime a mensagem que o aluno foi aprovado; caso contrário,
# imprime que o aluno foi reprovado.

notafinal = float(input("\nDigite a nota final do aluno: "))

if(notafinal >= 6):
    print("\nALUNO APROVADO\n")

else:
    print("\nALUNO EM EXAME ESPECIAL\n")
    novoexame = float(input("\nDigite a nota do exame especial: "))

if(novoexame >= 6):
    print("\nALUNO APROVADO NO EXAME ESPECIAL\n")

else:
    print("\nALUNO REPROVADO\n")

