"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append, insert, pop, del, clear, extend, +
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
#        0   1   2   3   4   5
print('Lista que criei')
lista = [10, 20, 30, 40]
print(lista)
# numero = lista[2]
# lista[2] = 300
# print(lista)
# print(lista[2])
# print(numero)

# REMOVER
# del lista[2]
# print(lista)
# print(lista[2])

# ADICIONAR NO FINAL DA LISTA
print('Adicionando um valor no final da lista')
lista.append(50)
print(lista)

# REMOVE O ULTIMO LEMENTO DA LISTA, MAS POSSO TAMBÈM COLOCAR O INDICE QUE DESEJO REMOVER
print('Removendo o valor do final da lista')
lista.pop()
print(lista)

ultimo_valor = lista.pop()
print('Removendo o valor do final da lista e mostrando qual foi o valor removido')
print(lista, 'Removido, ', ultimo_valor)
print('Removendo o valor passando o indice que seja remover e mostrando qual foi o valor removido')
ultimo_valor = lista.pop(1)
print(lista, 'Removido, ', ultimo_valor)

# INSERT ADICIONA UM ITEM NO INDICE ESCOLHIDO
print('Inserindo um valor na lista no indice escolhido')
#         indice  valor
lista.insert(0,     1)
print(lista)
print('Pegando o tamanho da lista')
print(len(lista))
print('Inserindo um valor na lista no indice escolhido')
lista.insert(3,     5)
print(lista)

lista_a = [1, 2, 3]
print('Lista A')
print(lista_a)
lista_b = [4, 5, 6]
print('Lista B')
print(lista_b)
lista_c = lista_a + lista_b
print('Concatenando duas listas')
print(lista_c)

# extend - estende a lista
# Valores de retorno de extend()
# O método list extend() não retorna nada, apenas modifica a lista fornecida.
print('Estende a lista b dentro da lista a')
lista_a.extend(lista_b)
print(lista_a)

# CLEAR LIMPAR A LISTA
print('Limpando a lista')
lista.clear()
print(lista)