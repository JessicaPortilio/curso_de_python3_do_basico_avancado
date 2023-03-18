"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
"""
#        +01234
#        -54321
string = 'ABCDE'  # 5 caracteres (len)
#---------0----1--------2-------3---------
lista = [123, True, 'Jessica', 1.2]
#------ -4--- -3------ -2------ -1---------
print(lista)
# print(string[2])
# print(lista, type(lista))
# print(bool(lista))
lista[-2] = 'Vitória'
print(lista[-2], type(lista[-2]))
print(lista)
