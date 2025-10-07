print(('-=-'*20),'\033[32mCOMPARADOR NUMÉRICO\033[m',('-=-'*20))

print("\033[7;30;40mInforme dois números para saber o maior valor:\033[m ")

n1 = int(input('\033[1mDigite o primeiro valor:\033[m\033[32m '))
n2 = int(input('\033[m\033[1mDigite o segundo valor:\033[m\033[32m '))

maior = n1

if n2 < maior:
    print('\033[1;33mO primeiro valor é maior!\033[m')
elif n2 > maior:
    print('\033[1;33mO segundo valor é o maior!\033[m')
else:
    print('\033[1;33mOs dois números tem o mesmo valor!\033[m')