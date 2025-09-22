produto = float(input('Qual o preço do produto: '))

desconto = produto * (5/100)

preco_final = produto - desconto
print(f'O valor do produto em liquidação (5%), será de: R${preco_final:.2f}')