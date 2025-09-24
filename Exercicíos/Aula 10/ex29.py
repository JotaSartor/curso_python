limite_velocidade = 50
velocidade_carro = int(input('Digite a velocidade que o carro passou no radar: '))
multa = (velocidade_carro - 50) * 7

if velocidade_carro < limite_velocidade:
    print('Tudo certo! Você está dentro do limite de velocidade')
else:
    print('Atenção! Você foi multado por excesso de velocidade')
    print(f'A multa a ser paga será de: {multa}')
    