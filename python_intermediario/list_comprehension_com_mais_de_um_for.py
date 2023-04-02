lista = []
for x in range(3):
    for y in range(3):
        lista.append((x,y))

print(lista)


lista = [
    (x, y) #lado esquerdo do for é usado para mapeamento
    for x in range(3)
    for y in range(3)
]

print(lista)