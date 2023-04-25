# Encapsulamento (modificadores de acesso: public, protected, private)
# Python NÃO TEM modificadores de acesso
# Mas podemos seguir as seguintes convenções
#   (sem underline) = public
#       pode ser usado em qualquer lugar
# _ (um underline) = protected
#       só DEVE ser usado na sua classe
#       ou suas subclasses.
# __ (dois underlines) = private
#       "name mangling" (desfiguração de nomes) em Python
#       _NomeClasse__nome_attr_ou_method
#       só DEVE ser usado na classe em que foi
#       declarado.

class Foo:
    def __init__(self):
        self.public = 'isso é público'
        self._protected = 'isso é protegido'
        self.__private = 'isso é privado'

    def metodo_publico(self):
        self._metodo_protected()
        print(self._protected)
        print(self.__private)
        self.__metodo_private()
        return 'Metodo público'
    
    def _metodo_protected(self):
        print('Metodo protegido')
        return 'Metodo protegido'
    
    def __metodo_private(self):
        print('Metodo privado')
        return 'Metodo privado'
    
f = Foo()
print(f.public)
print(f.metodo_publico())
# Não devo fazer isso
# print(f._protected) # funciona, funciona, mas não devo utilizar
# print(f._metodo_protected()) # funciona, funciona, mas não devo utilizar