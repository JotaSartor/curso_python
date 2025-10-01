from datetime import date

ano = int(input('Digite o ano para saber se ele é BISSEXTO (Coloque 0 para analisar o ano atual): '))

if ano == 0:
   ano = date.today().year
elif ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
   print('O ano é BISSEXTO!') 
else:
   print('O ano NÃO é BISEXTO!')