frase = 'O python é uma linguagem de programação multiparadigma. '\
    'Python foi criada por Guido Van Rossun'

frase = frase.lower()

apareceu_mais_vezes = 0
letras_que_apareceu_mais_vezes = ''

i = 0
while i < len(frase):
    letra_atual = frase[i]
    i+= 1
    
    if letra_atual == ' ':
        continue

    qtd_letras = frase.count(letra_atual.lower())

    if apareceu_mais_vezes < qtd_letras:
        apareceu_mais_vezes = qtd_letras
        letras_que_apareceu_mais_vezes = letra_atual

print(f'A letra "{letras_que_apareceu_mais_vezes}" apareceu {apareceu_mais_vezes}x')

    
