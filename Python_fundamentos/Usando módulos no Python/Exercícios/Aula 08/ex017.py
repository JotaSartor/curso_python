import math

cateto1 = int(input('Digite o comprimento do primeiro cateto: '))

cateto2 = int(input('Digite o comprimento do segundo cateto: '))


hipotenusa = math.hypot(cateto1, cateto2)

print(f' Os catetos de comprimentos {cateto1}, {cateto2} resultam no comprimento da hipotenusa de: {hipotenusa:.3f}')

