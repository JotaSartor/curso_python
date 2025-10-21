print(('-=-'*20),'\033[32mGerenciador de Pagamentos\033[m',('-=-'*20))

print(('-=-'*5),'\033[1mPara calcular quanto o cliente irá pagar, informe.',('-=-'*5))

print('\033[m')

preco = float(input('\033[1mValor do produto:\033[m \033[4;33mR$'))

print('\033[m')

print(('-=-'*5),'\033[1mEscolha uma condição de pagamento abaixo:\033[m',('-=-'*5))

print('\033[1m1 -\033[m \033[4;32mdinheiro/cheque\033[m \033[1m(10% desc)\033[m')
print('\033[1m2 -\033[m \033[4;34mcartão à vista\033[m \033[1m(5% desc)\033[m')
print('\033[1m3 -\033[m \033[4;36m2x cartão\033[m')
print('\033[1m4 -\033[m \033[4;35m3x cartão\033[m \033[1m(20% juros)')

print('\033[m')

opcao = int(input('\033[97mSua opção:\033[m \033[4;33m'))

print(('\033[m-=-'*16))

print(f'\033[1mValor do produto:\033[m \033[4;33mR${preco}\033[m')

if opcao == 1:
    print('\033[1mForma de pagamento selecionada:\033[m \033[1;32mDinheiro/cheque')
    print('\033[m')
    dinheiro = preco - (preco * (10/100))
    print(f'\033[1mO total a ser pago será de\033[m \033[4;33mR${dinheiro:.2f}\033[m')

elif opcao == 2:
    print('\033[1mForma de pagamento selecionada:\033[m \033[1;34mcartão à vista')
    print('\033[m')
    cartao = preco - (preco * (5/100))
    print(f'\033[1mO total a ser pago será de\033[m \033[4;33mR${cartao:.2f}\033[m')

elif opcao == 3:
    print('\033[1mForma de pagamento selecionada:\033[m \033[1;36m2x cartão')
    print('\033[m')
    print(f'\033[1mO total a ser pago será de\033[m \033[4;33mR${preco:.2f}\033[m')
    
elif opcao == 4:
    print('\033[1mForma de pagamento selecionada:\033[m \033[1;35m3x cartão')
    print('\033[m')
    cartao3 = preco + (preco * (20/100))
    print(f'\033[1mO total a ser pago será de\033[m \033[4;33mR${cartao3:.2f}\033[m')

else:
    print('\033[1;31mSelecione uma opção válida. (1 à 4)\033[m')