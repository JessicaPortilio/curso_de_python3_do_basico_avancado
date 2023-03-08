"""
Iterando strings com while
"""
#       0123456
nome = 'Jessica'  # Iteráveis
#       7654321
tamanho_nome = len(nome)
print(nome)
print(tamanho_nome)
nova_string = ''
contador = 0
while(contador < tamanho_nome):
    nova_string += '*' +nome[contador]
    contador += 1
nova_string += '*'
print(nova_string)