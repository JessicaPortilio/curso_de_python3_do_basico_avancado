# Manipulando chaves e valores em dicionários

pessoa = {
    'nome' : 'Jessica',
    'sobrenome' : 'Portilio',
    'idade' : '25',
    'altura' : 1.6,
    'endereços' : [
        {'rua' : 'tal tal', 'numero' : 123},
        {'rua' : 'outra rua', 'numero' : 321},
    ],
}

animal = {}
chave = 'nome2'
animal['nome'] = 'Abelha'
animal[chave] = 'Burro'
del animal['nome2']
print(animal)
print(animal['nome'])

animal['sobrenome'] = 'Rainha'

# print(pessoa.get('sobrenome'))
if animal.get('sobrenome') is None:
    print('NÃO EXISTE')
else:
    print(animal['sobrenome'])