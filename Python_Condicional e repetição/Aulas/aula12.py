#CONDIÇÕES ANINHADAS

nome = str(input('Qual é seu nome? '))

if nome == 'João':
    print('Que nome bonito!')
elif nome =='Pedro' or nome =='Maria' or nome == 'Enzo':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino')
else:
    print('Seu nome é tão normal.')
print(f'Tenha um bom dia, {nome}! ')
