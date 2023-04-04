# Generator expression, Irables e Iterators
import sys
iterable = ['Eu', 'Tenho', '__iter__']
iterator = iterable.__iter__() # tem __iter__e__next__
#print(next(iterator)) # não consigo pegar a posição de um iterator tipo iterator[0] porque ele não reconhece nem o tamanho len(iterator) somente o próximo next(iterator)

# for i in iterator:
#     print(i)

# Generator são funções que sabem pausar
# Iterator é uma classe que quando for criada tem que ter o método iter e next e geralmente iterator trabalha com iterável
# Todo generator é um iterator
# Mas um iterator não é um generator
lista = [n for n in range(10000000)]
generator = (n for n in range(10000000)) #isso é um generator e não uma tupla com comprehension até porque comprehension não tem em tupla risos
print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

for i in generator:
    print(i)