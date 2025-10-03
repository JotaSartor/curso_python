#MANIPULANDO TEXTO

#frase.split() = Separa uma string em numerações. A separação é feita pelo carácter de "split", também conhecido por espaço. De forma mais técnica 
#o split gera uma lista com cada palavra de uma cadeia de carácteres.

#'-'.join(frase) = Utilizado para juntar elementos

frase = 'Curso em Video Python'
print('fatiador de frase: ', frase[3:10:2])
print('frase.count: ', frase.count('o'))
print('frase.replace: ', frase.replace('Python', 'Android'))
print('in frase: ', 'Curso' in frase)
print('frase.find: ', frase.find('video'))
print('frase.rfind: ', frase.rfind('video'))
print('frase.lower.find: ', frase.lower().find('video'))
print('print: ', frase)
