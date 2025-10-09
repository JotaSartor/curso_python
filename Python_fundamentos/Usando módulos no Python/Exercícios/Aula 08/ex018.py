import math

angulo_graus = float(input('Digite o ângulo: '))


parte_inteira = int(angulo_graus)
parte_decimal = angulo_graus - parte_inteira

if parte_decimal >= 0.5:
    angulo_int = math.ceil(angulo_graus)
else:
    angulo_int = math.floor(angulo_graus)

angulo_rad = math.radians(angulo_int)

print(f'Ângulo aproximado para: {angulo_int}°')
print(f"Seno({angulo_int}°) = {math.sin(angulo_rad):.2f}")
print(f"Cosseno({angulo_int}°) = {math.cos(angulo_rad):.2f}")
print(f"Tangente({angulo_int}°) = {math.tan(angulo_rad):.2f}")
