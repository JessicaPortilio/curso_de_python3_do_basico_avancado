"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
palavra_secreta = 'python'
letras_acertadas = ''
numero_tentativas = 0

while True:
    letra_digitada = input('Digite uma letra: ')
    numero_tentativas += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            print(letra_secreta, end=' ')
        else:
            print('*', end=' ')
    print()

    if numero_tentativas < 10:
        print(f'Você já tentou {numero_tentativas}x você ainda tem {10 -numero_tentativas}')
    else:
        print('Poxa, você não acertou a palavra secreta!')
        break
    # Essa condição compara os conjuntos das letras da palavra secreta e das letras acertadas.
    # Se eles forem iguais, significa que todas as letras da palavra secreta foram adivinhadas.
    if set(palavra_secreta) == set(letras_acertadas):
        print('Parabéns, você acertou a palavra secreta!')
        break
