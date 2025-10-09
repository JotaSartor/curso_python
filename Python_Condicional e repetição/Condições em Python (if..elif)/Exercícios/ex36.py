import time

print(('-=-'*20),'\033[32mAPROVAÇÃO DE EMPRÉSTIMO BANCÁRIO\033[m',('-=-'*20))

valor_casa = float(input('Informe o valor da casa: '))
salario = float(input('Informe o valor do salário: '))
anos = int(input('Informe em quantos anos irá pagar: '))

meses = (anos * 12)
prestacao = valor_casa / meses
limite = 0.3 * salario

print('\033[1;33mSIMULANDO EMPRÉSTIMO...\033[m')
time.sleep (2)

if prestacao > limite:
    print('\033[33mSua solicitação de empréstimo foi \033[1;31mNEGADA!\033[m\033[m')
    print('\033[1;37mO valor da prestação excede 30% do salário.\033[m]')
else:
    print('\033[32mSua solicitação de empréstimo foi \033[1mAPROVADA!\033[m\033[m')
    print(f'\033[33mSua prestação será de: \033[m\033[1;32mR${prestacao:.2f}\033[m', f'\033[33mPor mês durante: \033[m\033[1;32m{meses}\033[m \033[33mmeses!\033[m')