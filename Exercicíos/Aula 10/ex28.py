import random

numero_aleatorio = random.randint(0, 5)
max_tentativas = 3
tentativas = 0

while tentativas < max_tentativas:
    restantes = max_tentativas - tentativas
    chute = int(input(f'Adivinhe o número escolhido pelo PC, de 0 a 5 (você tem {restantes} tentativa(s): '))
    tentativas += 1
    if chute == numero_aleatorio:
        print('PARABÉNS! Você adivinhou o número.')
        break
    else:
        if tentativas < max_tentativas:
            print('VOCÊ ERROU! tente novamente.')

        else:
            print('VOCÊ ERROU! Suas tentativas acabaram.')
            print(f'O número era {numero_aleatorio}')