# isinstace - para saber se objeto é de determinado tipo
lista = [
    'a', 1, 1.1, True, [0, 1, 2], (1, 2),
    {0, 1}, {'nome': 'Luiz'},
]

for item in lista:
    if isinstance(item, set):
        print('SET')
        item.add(5)
        print(item, isinstance(item, set))

    elif isinstance(item, str):
        print('STR')
        print(item.upper())

    elif isinstance(item, (int, float)):
        print('INT OU FLOAT')
        print(item, item * 2)
    elif isinstance(item, list):
        print('LISTA')
        print(item)
    elif isinstance(item, tuple):
        print('TUPLA')
        print(item)
    else:
        print('OUTRO')
        print(item)