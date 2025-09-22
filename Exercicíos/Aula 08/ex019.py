import random

aluno1 = str(input('Qual o nome do primeiro aluno que será sorteado?: '))
aluno2 = str(input('segundo aluno: '))
aluno3 = str(input('terceiro aluno: '))
aluno4 = str(input('quarto aluno: '))

opcoes = (aluno1, aluno2, aluno3, aluno4)
sorteio = random.choice(opcoes)
print(f'O aluno que apagará o quadro será: {sorteio}')
