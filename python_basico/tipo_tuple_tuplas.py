"""
Tipo tupla - Uma lista imutável 
tupla você não consegue mudar ela
Se você quer mudar crie uma lista, pois lista é mutável
"""
# LISTA
nome = ['Maria', 'Helena', 'Luiz']
tupla = tuple(nome)
print('Tupla: ', tupla)
# TUPLA
nomes = ('Maria', 'Helena', 'Luiz')
lista = list(nomes)
print('Lista: ', lista)
# nomes = list(nomes)
print('Tupla: ', nomes)
print('Pegando o ultimo valor de uma tupla: ' ,nomes[-1])
