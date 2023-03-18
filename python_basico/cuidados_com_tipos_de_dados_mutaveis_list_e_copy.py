"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
lista_a = ['Luiz', 'Maria', 1, True, 1.2]
print('Lista A: ' , lista_a)
# Eu não estou passando o valor da lista_a para a lista_b, 
# estou simplesmente apontando os dois para o mesmo lugar
lista_b = lista_a

# Quando eu altero em um lugar os dois tera o mesmo valor 
# já que eles apontam para o mesmo lugar
lista_a[0] = 'Jessica'
print('Lista B: ' ,lista_b)

# Agora sim a lista c estará recebendo a lista a
lista_c = lista_a.copy()
lista_a[0] = 'João'
print('Lista C: ', lista_c)
print('Lista A: ' , lista_a)
