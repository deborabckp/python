# 3. Um deputado propôs um projeto para alterar as regras para a aposentadoria. Por este
# projeto, para requerer a aposentadoria, os trabalhadores têm que combinar dois requisitos:
# tempo de contribuição ao INSS e idade mínima. Os trabalhadores do sexo masculino poderão
# aposentar-se com no mínimo 50 anos de idade e no mínimo 30 anos de contribuição. Além
# disso, é necessário que a soma entre o tempo de contribuição e a idade seja de no mínimo 90
# anos para eles.
# Faça um programa que leia a idade e o tempo de contribuição de um trabalhador do sexo
# masculino e informe se o mesmo pode se aposentar. Não é necessário validar a idade e o
# tempo de contribuição.

idade = int(input("\nDigite a sua idade:\n"))
anosdecontribuicao = int(input("\nDigite os anos de contribuição:\n"))

soma = idade + anosdecontribuicao

if(idade >= 50 and anosdecontribuicao >= 30):
    print("\nVocê pode se aposentar devido a idade ou tempo de contribuição, ou os dois\n")

else:
    print("\nVocê ainda não pode se aposentar")

if  (soma < 90):
    print("\nPessoa não apta a se aposentar porque a soma entre o tempo de contribuição e idade não é igual ou maior que 90\n")
