# Maria pegou um empréstimo de 1.000.000
# para realizar o pagemento em 5 anos
# A data em que ela pegou o empréstimo foi
# 20/12/2020 e o vencimento de cada parcela
# é no dia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valor de cada parcela
import locale
from datetime import datetime

from dateutil.relativedelta import relativedelta

# Definindo a localização para o Brasil
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

valor_total = 1_000_000
data_emprestimo = datetime(2020, 12, 20)
delta_anos = relativedelta(years=5)
data_final = data_emprestimo + delta_anos

data_parcelas = []
data_parcela = data_emprestimo

while data_parcela < data_final:
    data_parcelas.append(data_parcela)
    data_parcela += relativedelta(months=+1)
contador = 1

numero_parcelas = len(data_parcelas)
print(f'Quantidades de parcelas: {numero_parcelas}')

valor_parcela = valor_total / numero_parcelas

# Formatando o número
valor_parcela_formato_BR = locale.currency(
    # A função locale.currency() formata um valor monetário de acordo com a
    # localização definida, neste caso 'pt_BR.utf8',
    # e utiliza o valor de valor_parcela como entrada.
    # O argumento grouping=True habilita a separação de milhares com pontos,
    # e o argumento symbol=False desabilita a inclusão do símbolo monetário.
    valor_parcela, grouping=True, symbol=False)

for data in data_parcelas:
    print(data.strftime('%d/%m/%Y'), 'R$', valor_parcela_formato_BR)

print()

valor_total_BR = locale.currency(
    valor_total, grouping=True, symbol=False)

print(
    f'Você pegou R${valor_total_BR} para pagar'
    f'em {delta_anos.years} anos '
    f'({numero_parcelas} meses) em parcelas de '
    f'R${valor_parcela_formato_BR}'
)
