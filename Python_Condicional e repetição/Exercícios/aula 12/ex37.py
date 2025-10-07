print(('-=-'*20),'\033[32mCONVERSOR DE BASES NUMÉRICAS\033[m',('-=-'*20))

numero = int(input("\033[7;30;40mDigite um número inteiro:\033[m "))


print("\033[7;30;40mEscolha uma Base de Conversão:\033[m ")

print("[\033[31m1\033[m] - Binário")
print("[\033[32m2\033[m] - Octal")
print("[\033[33m3\033[m] - Hexadecimal")

opcao = int(input("\033[7;30;40mSua opção:\033[m "))

if opcao == 1:
    binario = bin(numero)
    print(f"O número escolhido em \033[31mBinário\033[m é igual a: {binario[2:]}")
elif opcao == 2:
    octal = oct(numero)
    print(f"O número escolhido em \033[32mOctal\033[m é: {octal[2:]}")
elif opcao == 3:
    hexadecimal = hex(numero)
    print(f"O número escolhido em \033[33mhexadecimal\033[m é: {hexadecimal[2:]}")
else:
    print("\033[1;31mOpção inválida! Escolha uma opção de 1 a 3.\033[m")