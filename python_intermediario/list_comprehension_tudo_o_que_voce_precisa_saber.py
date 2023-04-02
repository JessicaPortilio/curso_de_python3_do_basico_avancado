numeros = [1,2,3,4,5]
novos_numeros = numeros  # novos_numeros estão apontando para mesma lista de numeros, estou fazendo uma referência

print(numeros)
print(novos_numeros)
print()
print()

novos_numeros[0] = 20
print('Mudou em um lugar mudou nos dois, porque ambos estão apontando para o mesmo lugar!')
print(numeros)
print(novos_numeros)
print()
print()

numeros2 = [1,2,3,4,5]
novos_numeros2 = numeros2.copy() # agora sim novos_numeros2 recebe uma cópia da lista de numeros2 então se eu mudar em um não vai mudar nos dois.

novos_numeros2[0] = 20

print("Agora que fiz a cópia, ele não está apontando por mesmo lugar, por isso só mudou em um lugar!")
print(numeros2)
print(novos_numeros2)
print()
print()

#-------------------------------------------------------
# List Comprehension

numeros3 = [1,2,3,4,5]
novos_numeros3 = [numero for numero in numeros3]

# novos_numeros3 = []
# for numero in numeros3:
#     novos_numeros3.append(numero)

novos_numeros3[0] = 20

print('Fiz uma list comprehension então coloquei dentro da lista novos_numeros3 os valores percorrido pelo for na lista numeros3 que foram colocado na variável numero')
print(numeros3)
print(novos_numeros3)
print()
print()


#-------------------------------------------------------
# Mapeamento

def divisoes(x, y):
    return x / y

def substracoes(x, y):
    return x - y

def multiplicacoes(x, y):
    return x * y

def potenciacoes(x, y):
    return x ** y


numeros4 = [1,2,3,4,5]
divisao = [divisoes(numero, 2) for numero in numeros4]
multiplicacao = [multiplicacoes(numero, 2) for numero in numeros4]
Substracao = [substracoes(numero, 2) for numero in numeros4]
quadrado= [potenciacoes(numero, 2) for numero in numeros4]

print('Mapeando uma lista para outra lista')
print(numeros4)
print(divisao)
print(multiplicacao)
print(Substracao)
print(quadrado)
print()
print()

#-------------------------------------------------------
# Filter
# No final do for o if é para filtrar o valor 
# If no começo do for é operador ternario se for isso faça isso se não faça isso

numeros5 = [1,2,3,4,5,6,7,8,9,10]
novos_numeros5 = [numero for numero in numeros5 if numero > 5]
impares = [numero for numero in numeros5 if numero % 2 != 0]
pares = [numero for numero in numeros5 if numero % 2 == 0]
outro_if = [
            numero 
            if numero != 6 else 600  
            for numero in numeros5 
            if numero % 2 == 0
            ]
pode_ser_assim_tambem = [
            numero 
            if numero != 6 else 600  
            for numero in pares
            ]

print('Filter')
print(numeros5)
print(novos_numeros5)
print(impares)
print(pares)
print(outro_if)
print(pode_ser_assim_tambem)
print()
print()

#----------------------------------------------
# Linhas e Colunas

# for x in range(1, 11): # 10 linhas
#     for y in range(1, 6): # 5 colunas
#         print(x, y)

linhas_e_colunas = [
    (x, y)
    if y != 2 else (x , y * 1000)
    for x in range(1, 11)
    for y in range(1,6)
    #filtrar
    if x != 2
]

print(linhas_e_colunas)
print()
print()

#----------------------------------------------
# string

string = 'Jessica Portilio'
numero_de_letras = 2
# nova_string = ''.join([letra for letra in string])
nova_string = '.'.join([
    string[indice:indice + numero_de_letras ] 
    for indice in range(0, len(string), numero_de_letras )])

print(string)
print(nova_string)
print()
print()

#----------------------------------------------
# listas

nomes = ['jessica', 'maria', 'joana', 'felipe', 'carlos']
# novos_nomes = [nome.lower() for nome in nomes]
# novos_nomes = [nome.title() for nome in nomes]
# novos_nomes = [nome.upper() for nome in nomes]
novos_nomes = [f'{nome[:-1].lower()}{nome[-1].upper()}' 
               for nome in nomes
               ]
print(novos_nomes)
print()
print()

#----------------------------------------------
# flat

numeros6 = [[numero, numero ** 2] for numero in range(10)]
flat = [y for x in numeros6 for y in x]
print(numeros6)
print('------------------------------------------------')
print(flat)
print()
print()
