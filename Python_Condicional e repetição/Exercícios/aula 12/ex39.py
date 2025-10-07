from datetime import date

print(('-=-'*20),'\033[32mALISTAMENTO MILITAR\033[m',('-=-'*20))

ano = int(input('\033[37mPara verificar seu alistamento\033[m \033[1;37minforme o ano de seu nascimento:\033[m '))

ano_atual = date.today().year
ano_alistamento = (ano + 18)
idade = (ano_atual - ano)

print(f'\033[1mQuem nasceu em\033[m \033[33m{ano}\033[m \033[1mtem\033[m \033[33m{idade}\033[m \033[1manos em\033[m \033[33m{ano_atual}\033[m\033[1m!\033[m')

if idade < 18:
    faltam = ano_alistamento - ano_atual
    print(f'\033[37mAinda faltam\033[m \033[1;32m{faltam}\033[m \033[37mano(os) para o alistamento.\033[m')
    print(f'\033[37mSeu alistamento será em:\033[m \033[1;32m{ano_alistamento}\033[m')
elif idade > 18:
    passou = ano_atual - ano_alistamento
    print(f'\033[37mJá se passaram\033[m \033[1;31m{passou}\033[m \033[37mano(os) do alistamento.\033[m')
    print(f'\033[37mSeu alistamento foi em:\033[m \033[1;31m{ano_alistamento}\033[m')
else:
    print('\033[37mVocê deve se alistar\033[m \033[1;33mIMEDIATAMENTE!')
