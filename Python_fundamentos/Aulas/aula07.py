# OPERADORES ARITMÉTICOS

n1 = int(input('um valor: '))
n2 = int(input('um valor: '))
s = n1 + n2 # Adição
m = n1 * n2 # Subtração
d = n1 / n2 # Divisão
di = n1 // n2 # Divisão inteira
r = n1 % n2 # Resto da Divisão
p = n1 ** n2 # potência
print('A soma é {}, o produto é {} e a divisão é {}'.format(s, m, d), end=' ')
print('Divisão inteira {}, o resto da divisão {} e potência {}'.format(di, r, p))

# {:.3f} limita em 3 casas decimais quando o número for flutuante
# end=' ' faz com que os prints continuem na mesma linha
# Ordem de Procedência
# 1°- ()
# 2°- **
# 3°- * / // %
# 4°- + -  

