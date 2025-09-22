salario = float(input('Digite o salário atual do funcionário: '))

aumento = salario * (15/100)

novo_salario = aumento + salario

print(f'O novo salário do funcionário após o aumento de 15% será de: R${novo_salario:.2f}')
