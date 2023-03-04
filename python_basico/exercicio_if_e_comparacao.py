primeiro_numero = input('Digite um valor: ')
segundo_numero = input('Digite outro valor: ')

if primeiro_numero > segundo_numero:
    print(f'{primeiro_numero=} é maior do que o {segundo_numero=}')
elif primeiro_numero == segundo_numero:
    print(f'{primeiro_numero=} é igual o {segundo_numero=}')
else:
    print(f'{segundo_numero=} é maior do que o {primeiro_numero=}')