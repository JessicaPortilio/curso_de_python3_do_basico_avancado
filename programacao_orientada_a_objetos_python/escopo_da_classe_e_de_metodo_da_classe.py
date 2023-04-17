# Escopo da classe e de métodos da classe
class Animal:
    def __init__(self, nome):
        self.nome = nome

        # só é acessado aqui
        # variavel = 'valor'
        # print(variavel)
    
    def comendo(self, alimento):
        return f'{self.nome} está comendo {alimento}'
    
    def executar(self, *args, **kwargs):
       return self.comendo(*args, **kwargs)

        


leao = Animal('Leão')
print(leao.nome)
print(leao.executar('morango'))