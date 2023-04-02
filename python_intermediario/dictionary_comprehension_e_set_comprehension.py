# Dictionary Comprehension e Set Comprehension

# Dictionary Comprehension
produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório',
}

print(produto)
print()
print()

dc = {
    chave : valor.upper()
    #if isinstance(valor, (int, float)) else valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor
    in produto.items()
    if chave == 'categoria' # só vai incluir categoria
}
print(dc)
print()
print()

lista = [
    ('a', 'valor a'),
    ('b', 'valor a'),
    ('b', 'valor a'),
]

# dc = {
#     chave : valor
#     for chave, valor in lista
# }

# print(dc)

print(dict(lista))
print()
print()

# Set Comprehension

s1 = {i for i in range(10)}
print(s1)
print()
print()

print(set(range(10)))

s2 = {2 ** i for i in range(10)}
print(s2)
print()
print()