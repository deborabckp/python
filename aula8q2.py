# 2. A servidora Luciene trabalha melhor quando o café está disponível, porém na sua sala
# apenas ela lembra abastecer a garrafa, causando aquele inconveniente diário. Luciene toma 2
# xícaras de café por dia, sabendo que a cafeteira fornece 10 xícaras por dia. Faça um programa
# que receba como entrada a quantidade de xícaras de café que as colegas de Luciene tomaram
# no dia e diga se Luciene ficará chateada ou não.

quantidadeCafe = int(input("Digite a quantidade de café que as colegas bebem: "))

if(quantidadeCafe <= 8):
    print("Luciene não vai ficar chateada")

else:
    print("Luciene ficará chateada")
