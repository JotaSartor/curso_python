print(('-=-'*20),'\033[32mCÁLCULO DE MÉDIA\033[m',('-=-'*20))

nota1 = float(input('\033[7;30;40mInforme a primeira nota:\033[m\033[1m '))
nota2 = float(input('\033[m\033[7;30;40mInforme a segunda nota:\033[m\033[1m '))

media = (nota1 + nota2) / 2

print(f'\033[m\033[7;30;40mTirando\033[m \033[1m{nota1}\033[m \033[7;30;40me\033[m \033[1m{nota2}\033[m\033[7;30;40m, a média do aluno é\033[m \033[1m{media}\033[m')

if media >= 7:
    print('\033[7;30;40mO aluno está\033[m \033[1;32mAPROVADO\033[m\033[7;30;40m!\033[m')
elif 7 > media >= 5:
    print('\033[7;30;40mO aluno está de\033[m \033[1;33mRECUPERAÇÃO\033[m\033[7;30;40m!\033[m')
else:
    print('\033[7;30;40mO aluno está\033[m \033[1;31REPROVADO\033[m\033[7;30;40m!\033[m')