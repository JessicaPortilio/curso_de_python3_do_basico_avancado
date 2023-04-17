# Métodos em instâncias de classes Python
# Hard coded - É algo que foi escrito diretamente no código
# Classe - Molde (geralmente sem dados)
# Instância da class (objeto) - Tem os dados
# Uma classe pode gerar várias instâncias.
# Na classe o self é a própria instância.

class Carro:
    def __init__(self, nome):
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} está acelerando...')

fusca = Carro('Fusca')
print(fusca.nome)
print(fusca.acelerar())

celta = Carro(nome='Celta')
print(celta.nome)
print(celta.acelerar())