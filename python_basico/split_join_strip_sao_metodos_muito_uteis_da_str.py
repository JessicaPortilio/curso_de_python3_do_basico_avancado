"""
split e join com list e str
split - divide uma string (list)
join - une uma string
"""
frase = 'Olha só que, coisa interessante'
lista_frases = frase.split() # quebra nos espaços
print(lista_frases)
lista_frases2 = frase.split(',') # quebra na virgulas
print(lista_frases2)
lista_frases3 = frase.split(', ') # quebra na virgulas mais espaço
print(lista_frases3)

frase2 = '    Olha só que         , coisa interessante'
lista_frases4 = frase2.split(',') # quebra na virgulas

for i, frase2 in enumerate(lista_frases4):
    lista_frases4[i] = lista_frases4[i].strip() # strip corta os espaços em branco 
                                               # rstrip corta espaço em branco da direita 
                                               # lstrip corta espaço em branco da esquerda
print(lista_frases4)


frase3 = '    Olha só que         , coisa interessante'
lista_frases_cruas = frase3.split(',') # quebra na virgulas

lista_frases5 = []
for i, frase3 in enumerate(lista_frases_cruas):
    lista_frases5.append(lista_frases_cruas[i].strip()) # strip corta os espaços em branco 
                                               # rstrip corta espaço em branco da direita 
                                               # lstrip corta espaço em branco da esquerda
print(lista_frases_cruas)
print(lista_frases5)

frases_unidas = '-'.join('abc')
print(frases_unidas)

frases_unidas2 = ', '.join(lista_frases5)
print(frases_unidas2)