# Usando calendar para calendários e datas
# https://docs.python.org/3/library/calendar.html
# calendar é usado para coisas genéricas de calendários e datas.
# Com calendar, você pode saber coisas como:
# - Qual o último dia do mês (ex.: monthrange)
# - Qual o nome e número do dia de determinada data (ex.: weekday)
# - Criar um calendário em si (ex.: monthcalendar)
# - Trabalhar com coisas específicas de calendários (ex.: calendar, month)
# Por padrão dia da semana começa em 0 até 6
# 0 = segunda-feira | 6 = domingo

import calendar
import locale

# Definindo a localização para o Brasil
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

# print(calendar.calendar(2023))
# print(calendar.month(2023, 5))

print(calendar.monthrange(2023, 12))
# Obtendo os nomes dos dias da semana em português
dias_da_semana = calendar.day_name
# Imprimindo os nomes dos dias da semana em português
# Esse primeiro número é o dia que foi o primeiro dia do mes
print(list(dias_da_semana))

numero_primeiro_dia, ultimo_dia = calendar.monthrange(2023, 12)
# primeiro dia de dezembro será na sexta feira
print(calendar.day_name[numero_primeiro_dia])
# ultimo dia de dezembro será nno domingo
print(calendar.day_name[calendar.weekday(2023, 12, ultimo_dia)])

for week in calendar.monthcalendar(2022, 12):
    # print(week)
    for day in week:
        if day == 0:
            continue
        print(day)
