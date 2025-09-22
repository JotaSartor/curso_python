import random

aluno1 = str(input('Qual o nome do primeiro aluno que será sorteado?: '))
aluno2 = str(input('segundo aluno: '))
aluno3 = str(input('terceiro aluno: '))
aluno4 = str(input('quarto aluno: '))

lista = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(lista)

print(f'A ordem de apresentação será: {lista}')
