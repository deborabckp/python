# 2. Escreva um programa que apresente como resultado a potência de uma base elevada ao
# expoente qualquer, ou seja, de B^e, em que B é o valor da base e E é o valor do expoente.
# Considere apenas a entrada de valores inteiros e positivos, ou seja, de valores naturais.

e = int(input("Digite um expoente qualquer: "))
base = int(input("Digite uma base: "))

if(e >= 0):
    result = base ** e
    print(result)

else:
    while(e < 0):
        e = int(input("Digite outro número: "))
        result = base ** e
        print(result)




