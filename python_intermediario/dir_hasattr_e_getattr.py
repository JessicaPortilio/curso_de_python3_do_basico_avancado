# dir, hasattr e getattr
# console de depuração 
# dir(string)

string = 'Jessica'
metodo = 'upper'
# if hasattr(string, metodo): # a minha string tem o método upper?
#     print(f'Existe {metodo}')
#     print(string.upper())


if getattr(string, metodo):
    print(f'Existe {metodo}')
    print(getattr(string, metodo)())
else:
    print(f'Não existe {metodo}')