salario = int(input('Informe o salário do funcionário: '))

aumento_10 = salario * (10/100)
aumento_15 = salario * (15/100)

salario_10 = salario + aumento_10
salario_15 = salario + aumento_15

if salario > 1251:
    print('O aumento de salário desse funcionário será de 10%')
    print(f'O valor total de salário será: R${salario_10:.2f}')
else:
    print('O aumento de salário desse funcionário será de 15%')
    print(f'O valor total de salário será: R${salario_15:.2f}')