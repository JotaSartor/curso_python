l1 = int(input('digite o primeiro lado: '))
l2 = int(input('digite o segundo lado: '))
l3 = int(input('digite o terceiro lado: '))

if ((l1 + l2 > l3) and (l1 + l3 > l2) and (l2 + l3 > l1)):
    print('As medidas formam um triângulo')
else:
    print('As medidas NÃO formam um triângulo')