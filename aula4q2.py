# 2. Efetuar o cálculo da quantidade de litros de combustível gasta em uma viagem, utilizando
# um automóvel que faz 12 quilômetros por litro. Para o cálculo, o usuário deve fornecer o
# tempo gasto e a velocidade média durante a viagem. Desta forma, será possível obter a
# distância percorrida com a fórmula:

# DISTANCIA ← VELOCIDADE × TEMPO.

# A partir do valor da distância, basta calcular a quantidade em litros de combustível utilizada
# na viagem com a fórmula:

# LITROS_USADOS ← DISTANCIA / 12.

# O programa deve apresentar os valores da velocidade média, tempo gasto na viagem, a
# distância percorrida e a quantidade de litros utilizados na viagem.

tempoGasto =  float(input("\nDigite o tempo gasto na viagem: "))
velocidadeMedia =  float(input("\nDigite a velocidade média durante a viagem: "))
distancia = velocidadeMedia * tempoGasto
litrosGasto = distancia / 12

print(f"\nA velocidade média durante a viagem foi de: {velocidadeMedia:,.0f}Km/h")
print(f"O tempo gasto durante a viagem foi de: {tempoGasto:,.0f} horas")
print(f"Foram usados {litrosGasto:,.2f}L durante a viagem\n")