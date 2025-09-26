n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o segundo número: '))

maior = n1
menor = n2

if n2 > maior:
    maior = n2
else:
    menor = n2

if n3 > maior:
    maior = n3
else:
    menor = n3

print(f'O numero maior é {maior} e o número menor é o {menor}')
