from datetime import date

print(('-=-'*20),'\033[32mCLASSIFICAÇÃO DE ATLETAS\033[m',('-=-'*20))

ano = int(input('\033[7;30;40mDigite o ano de nascimento do atleta: \033[m\033[4;97m'))

ano_atual = date.today().year
idade = ano_atual - ano

mirim = (idade <= 9)
infantil = (idade > 9 and idade <= 14)
junior = (idade > 14 and idade <= 19)
senior = (idade > 19 and idade <= 25)
master = (idade > 25)

print(f'\033[m\033[7;30;40mQuem nasceu em\033[m \033[4;33m{ano}\033[m \033[7;30;40mtem\033[m \033[4;33m{idade}\033[m \033[7;30;40manos em\033[m \033[4;33m{ano_atual}\033[m\033[7;30;40m!\033[m')

if mirim is True: #Até poderia simplificar pra "if mirim:" — é a mesma coisa, porque o if já entende True como condição verdadeira.
    print(f'\033[7;30;40mEsse atleta se encaixará na categoria:\033[m \033[4;37mMIRIM\033[m')
elif infantil is True:
    print(f'\033[7;30;40mEsse atleta se encaixará na categoria:\033[m \033[4;32mINFANTIL\033[m')
elif junior is True:
    print(f'\033[7;30;40mEsse atleta se encaixará na categoria:\033[m \033[4;33mJUNIOR\033[m')
elif senior is True:
    print(f'\033[7;30;40mEsse atleta se encaixará na categoria:\033[m \033[4;34mSÊNIOR\033[m')
elif master is True:
    print(f'\033[7;30;40mEsse atleta se encaixará na categoria:\033[m \033[4;31mMASTER\033[m')
    