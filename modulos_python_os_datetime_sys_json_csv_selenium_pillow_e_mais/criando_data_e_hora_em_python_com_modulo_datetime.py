# Criando datas com módulo datetime
# datetime(ano, mês, dia)
# datetime(ano, mês, dia, horas, minutos, segundos)
# datetime.strptime('DATA', 'FORMATO')
# datetime.now()
# https://pt.wikipedia.org/wiki/Era_Unix
# datetime.fromtimestamp(Unix Timestamp)
# https://docs.python.org/3/library/datetime.html
# Para timezones
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# Instalando o pytz
# pip install pytz types-pytz

# from datetime import datetime, timedelta

from datetime import datetime

# from dateutil.relativedelta import relativedelta

# from pytz import timezone


# data_str_data = '2023/05/02 22:41:23'
# data_str_formato = '%Y/%m/%d %H:%M:%S'
# data_str_data = '02/05/2023'
# data_str_formato = '%d/%m/%Y'
# data = datetime(2023, 5, 2, 22, 41, 23)
# data = datetime.strptime(data_str_data, data_str_formato)

# Pegar a data e hora atual
# data = datetime.now(timezone('America/Maceio'))
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones

# data = datetime(2023, 5, 2, 22, 41, 23, tzinfo=timezone('America/Maceio'))
# print(data)

# data = datetime.now()
# print(data.timestamp())  # O numero de segundos de 01-01-1970 até hoje
# print(datetime.fromtimestamp(1683209683))

#######################################################################
# datetime.timedelta e dateutil.relativetimedelta (calculando datas)
# Docs:
# https://dateutil.readthedocs.io/en/stable/relativedelta.html
# https://docs.python.org/3/library/datetime.html#timedelta-objects
# pip install python-dateutil types-python-dateutil

# fmt = '%d/%m/%Y %H:%M:%S'
# data_inicio = datetime.strptime('20/04/1987 09:30:30', fmt)
# data_fim = datetime.strptime('12/12/2022 08:20:20', fmt)

# print(data_fim > data_inicio)
# print(data_fim < data_inicio)
# print(data_fim == data_inicio)

# print(data_fim - data_inicio)
# delta = data_fim - data_inicio
# print(delta.days, delta.seconds, delta.microseconds)
# print(delta.total_seconds())

# delta = timedelta(days=10)
# print(data_fim + delta)

# delta = timedelta(days=10, hours=2)
# print(data_fim + delta)

# print(data_fim + relativedelta(seconds=60, minutes=10))

# delta = relativedelta(data_fim, data_inicio)
# print(delta)
# print(f'A diferença em anos são: {delta.years} anos \
# e a diferença em dias são: {delta.days} dias')

#######################################################################
# Formatando datas do datetime
# datetime.strftime('DATA', 'FORMATO')
# https://docs.python.org/3/library/datetime.html


# data = datetime(2022, 12, 13, 7, 59, 23)
data = datetime.strptime('2022-12-13 07:59:23', '%Y-%m-%d %H:%M:%S')
print(data.strftime('%d/%m/%Y'))
print(data.strftime('%d/%m/%Y %H:%M'))
print(data.strftime('%H:%M:%S'))
print(data.strftime('%Y'), data.year)
print(data.strftime('%d'), data.day)
print(data.strftime('%m'), data.month)
print(data.strftime('%H'), data.hour)
print(data.strftime('%M'), data.minute)
print(data.strftime('%S'), data.second)
