print(('-=-'*20),'\033[32mÍndice de Massa Corporal\033[m',('-=-'*20))

print(('-=-'*5),'\033[1mPara calcular o IMC, informe.',('-=-'*5))

print('\033[m')

altura = float(input('\033[1mSua altura (m):\033[m \033[4;33m'))
peso = int(input('\033[m\033[1mSeu peso (Kg):\033[m \033[4;33m'))

print('\033[m')

imc = peso / (altura ** 2)

if imc < 18.5:
    print(('-=-'*5),'\033[1;34mAbaixo do peso!\033[m',('-=-'*5))
elif imc >= 18.5 and imc < 25:
    print(('-=-'*5),'\033[1;32mPeso ideal!\033[m',('-=-'*5))
elif imc >= 25 and imc < 30:
    print(('-=-'*5),'\033[1;33mSobrepeso!\033[m',('-=-'*5))
elif imc >= 30 and imc < 40:
    print(('-=-'*5),'\033[1;31mObesidade!\033[m',('-=-'*5))
else:
    print(('-=-'*5),'\033[7;37;40mObesidade mórbida!\033[m',('-=-'*5))