cid = str(input('Em que cidade você nasceu? ')).strip()
print(cid[:5].upper() == 'SANTO')

# .strip e .upper é muito importante para previnir erros de digitaççao do usuário, o ".strip" server para eliminar os espaços antes e depois da string,
# e o .upper transforma o que o usuário escreveu para maiúsculo para evitar erros como o sAnTo