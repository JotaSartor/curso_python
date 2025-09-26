km = int(input('Digite a distâcia da viagem (em Km): '))
viagem_curta = km * 0.50
viagem_longa = km * 0.45

if km <= 200:
    print(f'O valor da passagem será: R${viagem_curta:.2f}!')
else:
    print(f'O valor da passagem será: R${viagem_longa:.2f}!')
