print(('-=-'*20),'\033[32mAnalisando Triângulos v2.0\033[m',('-=-'*20))

l1 = float(input('\033[7;30;40mdigite o primeiro lado:\033[m \033[4;97m'))
l2 = float(input('\033[m\033[7;30;40mdigite o segundo lado:\033[m \033[4;97m'))
l3 = float(input('\033[m\033[7;30;40mdigite o terceiro lado:\033[m \033[4;97m'))

if (l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1):
    print(('    '*4),'\033[m\033[32;1mAS MEDIDAS FORMAM UM TRIÂNGULO!\033[m',)

    print(('-=-'*5),'\033[1mO triângulo formado será do tipo:\033[m',('-=-'*5))
    if l1 == l2 and l2 == l3:
        print(('   '*8),'  \033[4;35mEquilátero\033[m')
    elif (l1 == l2 and l2 != l3) or (l1 == l3 and l3 != l2) or (l2 == l3 and l3 != l1):
        print(('   '*8),'  \033[4;34mIsósceles\033[m')
    else:
        print(('   '*8),'  \033[4;33mEscaleno\033[m')
else:
    print('\033[m\033[1;31mAS MEDIDAS NÃO FORMAM UM TRIÂNGULO!\033[m')