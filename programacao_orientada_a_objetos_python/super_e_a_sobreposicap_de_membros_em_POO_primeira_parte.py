# super() e a sobreposição de membros - Python Orientado a Objetos
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class
# class MinhaString(str):
#     def upper(self):
#         print('CHAMOU UPPER')
#         retorno = super(MinhaString, self).upper()
#         print('DEPOIS DO UPPER')
#         return retorno

# class MinhaString(str):
#     def upper(self):
#         print('CHAMOU UPPER')
#         retorno = super().upper()
#         print('DEPOIS DO UPPER')
#         return retorno

# string = MinhaString('Jessica')

# print(string.upper())


class A:
    atributo_a = 'valor_a'

    def __init__(self, atributo):
        self.atributo = atributo

    def metodo(self):
        print('A')
    

# B tem tudo que tinha no A
# então tem atributo_a e atributo_b
# e só tem o metodo B porque ele sobrescreveu o de cima, já que tem o mesmo nome o metodo
class B(A):
    atributo_b = 'valor_b'

    def __init__(self, atributo, outra_coisa):
        super().__init__(atributo)
        self.outra_coisa = outra_coisa

    def metodo(self):
        print('B')

# C tem tudo que tinha no B
# então tem atributo_a, atributo_b e atributo_c
# e só tem o metodo C porque ele sobrescreveu o de cima, já que tem o mesmo nome o metodo
class C(B):
    atributo_c = 'valor_c'

    def __init__(self, *args, **kwargs):
        # print('EI, burlei o sistema.')
        super().__init__(*args, **kwargs)

    def metodo(self):
        # Agora eu dei um super, então ele sabe que eu sou o C e ele vai procurar o metodo do B
        # tipo assim super(C, self) o self é o B
        super().metodo() #B
        super(B, self).metodo() #A
        print('C') #C

# print(C.mro())
# print(B.mro())
# print(A.mro())
c = C('Atributo', 'Qualquer')
# print(c.atributo)
# print(c.outra_coisa)
c.metodo()
# print(c.atributo_a)
# print(c.atributo_b)
# print(c.atributo_c)
# c.metodo()