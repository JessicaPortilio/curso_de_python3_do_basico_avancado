"""
    Exercicio
    Exiba os indices da lista
"""

lista = ['Maria', 'Helena', 'Luiz']
lista.append('Jessica')

indice = range(len(lista))
for indice in indice:
    print('Nome:', lista[indice], '-', 'Indice:', indice)
       