num = int(input('Digite um número de 0 a 9999: '))

if num < 0 or num > 9999:
    print('Número inválido! Deve ser entre 0 e 9999.')
else:
    u = num % 10
    d = num // 10 % 10
    c = num // 100 % 10
    m = num // 1000 % 10

print(f'unidade: {u}')
print(f'dezena: {d}')
print(f'centena: {c}')
print(f'milhar: {m}')