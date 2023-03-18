"""
enumerate - enumera iteráveis (índices)
"""
# [(0, 'Maria'), (1, 'Helena'), (2, 'Luiz'), (3, 'João')]
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

# lista_enumerada = enumerate(lista)
# # print(next(lista_enumerada))
# # print(next(lista_enumerada))
# # print(next(lista_enumerada))
# # print(next(lista_enumerada))

# for item in lista_enumerada:
#     print(item)

# lista_enumerada = list(enumerate(lista))
# print(lista_enumerada)

# for item in enumerate(lista):
#     print(item)

# for item in enumerate(lista):
#     indice, nome = item
#     print(indice, nome)

for indice, nome in enumerate(lista):
    print(indice, nome)