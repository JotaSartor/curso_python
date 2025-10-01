#      Style       |      Text       |    Background
# _________________|_________________|___________________
#    0       None  |  30    Black    |   Preto     40
#    1       Bold  |  31    Red      |   Vermelho  41
#    4  Underline  |  32    Green    |   Verde     42
#    7   Negative  |  33    Yellow   |   Amarelo   43
#                  |  34    Blue     |   Azul      44
#                  |  35    Magenta  |   Magenta   45
#                  |  36    Cyan     |   Ciano     46
#                  |  37    Grey     |   Cinza     47
#                  |  97    White    |   Branco    107



a = 3
b = 5
print(f'Os valores são \033[32m{a}\033[m e \033[31m{b}\033[m')