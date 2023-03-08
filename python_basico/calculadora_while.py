""" Calculadora com while """
while True:
    numero = input('Informe o primeiro número: ')
    numero2 = input('Informe o segundo número: ')
    operador = input('Informe a operação: (+, -, *, /)')

    numero_valido = None
    try:
        numero= float(numero)
        numero2= float(numero2)
        numero_valido = True
    except:
        numero_valido = None
    
    if numero_valido is None:
        print('Um ou ambos os números digitados são inválidos!')
        continue
    
    operadors_validos = '+-*/'

    if operador not in operadors_validos:
        print('Operação inválida!')
        continue

    if len(operador) > 1:
        print('Escolha somente uma operação!')

    match operador:
        case '+':
            soma = numero + numero2
            print(f'{numero} {operador} {numero2} = {soma}')
        case '-':
            soma = numero - numero2
            print(f'{numero} {operador} {numero2} = {soma}')
        case '*':
            soma = numero * numero2
            print(f'{numero} {operador} {numero2} = {soma}')
        case '/':
            soma = numero / numero2
            print(f'{numero} {operador} {numero2} = {soma}')

    #######################################
    sair = input('Deseja sair? [s]air ou [n]ao: ').lower().startswith('s') # endswith() verifica se encontra no final
    
    if sair is True:
        break