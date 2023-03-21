"""
Exercícios com funções

Crie uma função que multiplica todos os argumentos
não nomeados receidos
Retorne o total para uma variável e mostre o valor
da variavel


Crie uma função que fale se um número é par ou ímpar.
Retorne se o número é par ou ímpar

"""

def multiplicar(*args):
    total = 1
    for i in args:
        total *= i
    return total

mult = multiplicar(1,2,3,4,5)
print(mult)

def par_impar(num):
    if num % 2 ==0:
        return f'{num} é par'
    return f'{num} é ímpar'

print(par_impar(3))
