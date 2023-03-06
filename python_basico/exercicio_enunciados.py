"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numero = input('Informe um número inteiro: ')

if numero.isdigit():
    numero = int(numero)
    if numero % 2 == 0:
        print(f'{numero} é par')
    else:
        print(f'{numero} é impar')
else:
    print('Isso não é um número ou não é um número inteiro!')
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
hora = input('Informe a hora: ')

if hora.isdigit():
    hora = int(hora)
    if hora == 0 or hora <= 11:
        print(f'Bom dia, {hora}hr')
    elif hora > 11 and hora <= 17:
        print(f'Boa tarde, {hora}hr')
    elif hora > 17 and hora <= 23:
        print(f'Boa noite, {hora}hr')
    else:
        print(f'{hora} não corresponde a um horario valido')
else:
    print('Você precisa digitar números!')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

primeiro_nome = input('Informe seu primeiro nome: ')
quantidade_de_letras_do_nome = len(primeiro_nome)

if quantidade_de_letras_do_nome <=4:
    print('Seu nome é curto.')
elif quantidade_de_letras_do_nome >=5 and quantidade_de_letras_do_nome <=6:
    print('Seu nome é normal.')
else:
    print('Seu nome é muito grande.')