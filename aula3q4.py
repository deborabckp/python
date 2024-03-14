#4. Elaborar um programa que calcule e apresente o valor do volume de uma caixa retangular,
#utilizando a fórmula: VOLUME = COMPRIMENTO * LARGURA * ALTURA

altura = float(input("\nDigite a altura da caixa: "))
comprimento = float(input("\nDigite o comprimento da caixa: "))
largura = float(input("\nDigite a largura da caixa: "))
volumeCaixaRetangular = comprimento * largura * altura

print(f"\n O volume da caixa retangular é: {volumeCaixaRetangular:,.2f}")