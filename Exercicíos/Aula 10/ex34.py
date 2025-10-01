salario = float(input('Informe o salário do funcionário: '))

aumento_15 = salario + (salario * (15/100))
aumento_10 = salario + (salario * (10/100))

if salario <= 1250:
    print('O aumento de salário desse funcionário será de 15%')
    print(f'O valor total de salário será: R${aumento_15:.2f}')
else:
    print('O aumento de salário desse funcionário será de 10%')
    print(f'O valor total de salário será: R${aumento_10:.2f}')