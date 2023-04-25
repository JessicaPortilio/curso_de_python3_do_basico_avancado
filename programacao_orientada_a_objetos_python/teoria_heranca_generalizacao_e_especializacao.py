# Herança simples - Relações entre classes
# Associação - usa (um objeto usa outro objeto), Agregação - tem (objeto tem outro objeto)
# Composição - É dono de, Herança - É um
#
# Herança vs Composição
#
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class

class Pessoa():
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def falar_nome_classe(self):
       print(self.nome, self.sobrenome, self.__class__.__name__)

class Cliente(Pessoa):
    ...

class Aluno(Pessoa):
    ...


c1 = Cliente('Jessica', 'Portilio')
c1.falar_nome_classe()
a1 = Aluno('Maria', 'Oliveira')
a1.falar_nome_classe()

help(Cliente)

# class Animal:
#     def __init__(self, nome):
#         self.nome = nome

#     def comer(self):
#         print(self.nome, "está comendo.")

# class Cachorro(Animal):
#     def latir(self):
#         print(self.nome, "está latindo.")

# rex = Cachorro("Rex")
# rex.comer()  # saída: Rex está comendo.
# rex.latir()  # saída: Rex está latindo.
