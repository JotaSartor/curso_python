# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
#  Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$0,15 por Km rodado.

km = float(input('Digite quantos km foram percorridos: '))
dia = int(input('Digite quantos dias o carro ficou alugado: '))

valor_km = km * 0.15
aluguel = dia * 60

preço_total = valor_km + aluguel

print(f'Km percorridos: {km} = R${valor_km:.2f}')
print(f'Dias alugados: {dia} = R${aluguel}')
print(f'O valor total a pagar é: R${preço_total:.2f}')