import contas
import pessoas


class Banco:
    def __init__(
            self,
            agencias: list[int] | None = None,
            clientes: list[pessoas.Pessoa] | None = None,
            contas: list[contas.Conta] | None = None,
    ):
        self.agencias = agencias or []
        self.clientes = clientes or []
        self.contas = contas or []

    def _checa_agencia(self, conta):
        if conta.agencia in self.agencias:
            print('_checa_agencia', True)
            return True
        print('_checa_agencia', False)
        return False

    def _checa_cliente(self, cliente):
        if cliente in self.clientes:
            print('_checa_cliente', True)
            return True
        print('_checa_cliente', False)
        return False

    def _checa_conta(self, conta):
        if conta in self.contas:
            print('_checa_conta', True)
            return True
        print('_checa_conta', False)
        return False

    def _checa_se_conta_e_do_cliente(self, cliente, conta):
        if conta is cliente.conta:
            # print(conta, cliente.conta)
            print('_checa_se_conta_e_do_cliente', True)
            return True
        # print(conta, cliente.conta)
        print('_checa_se_conta_e_do_cliente', False)
        return False

    def autenticar(self, cliente: pessoas.Pessoa, conta: contas.Conta):
        return self._checa_agencia(conta) and \
            self._checa_cliente(cliente) and \
            self._checa_conta(conta) and \
            self._checa_se_conta_e_do_cliente(cliente, conta)

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencias!r}, {self.clientes!r}, {self.contas!r})'
        return f'{class_name}, {attrs}'


if __name__ == '__main__':

    c1 = pessoas.Cliente('Jessica', 30)
    cc1 = contas.ContaCorrente(111, 222, 0, 0)
    c1.conta = cc1
    c2 = pessoas.Cliente('Vanessa', 23)
    cc2 = contas.ContaCorrente(222, 434, 120, 200)
    c2.conta = cc2
    c3 = pessoas.Cliente('Pedro', 43)
    cc3 = contas.ContaPoupanca(333, 123, 345)
    c3.conta = cc3
    banco = Banco()
    banco.clientes.extend([c1, c2, c3])
    banco.contas.extend([cc1, cc2, cc3])
    banco.agencias.extend([111, 222, 333])

    if banco.autenticar(c1, cc1):
        cc1.depositar(10)
        print(c1.conta)

    # print(banco)
