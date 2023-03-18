"""
Introdução ao empacotamento e desempacotamento
"""

nomes = ['Maria', 'Helena', 'Luiz']
# nome1, nome2, nome3 = nomes
nome1, nome2, nome3 = ['Maria', 'Helena', 'Luiz']
print('Nome1: ',nome1)
print('Nome2: ',nome2)
print('Nome3: ',nome3)
pegando_primeiro_somente, *resto = ['Maria', 'Helena', 'Luiz']
print(pegando_primeiro_somente)
print('---------------------------------------')
pegando_primeiro_somente2, *_ = ['Maria', 'Helena', 'Luiz']
print(pegando_primeiro_somente2)
print('---------------------------------------')
_, pegando_segundo_somente2, *_ = ['Maria', 'Helena', 'Luiz']
print(pegando_segundo_somente2)
print('---------------------------------------')
_, _, pegando_terceiro_somente2, *_ = ['Maria', 'Helena', 'Luiz']
print(pegando_terceiro_somente2)
print('---------------------------------------')
_, _, nome, *resto = ['Maria', 'Helena', 'Luiz']
print(nome)