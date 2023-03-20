"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10
Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0
Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O primeiro dígito do CPF é 7
"""
import sys

cpf = input('Digite o número do cpf [746.824.890-70]: ')

novo_cpf = cpf.replace(".", "").replace("-", "")[:9]
soma = 0
multiplicar = 0

entrada_e_sequencial = novo_cpf == novo_cpf[0] * len(novo_cpf)

if entrada_e_sequencial:
    print('Você enviou dados sequenciais.')
    sys.exit()

# print(novo_cpf)
contador = 10
while(contador >=2):
   for x in novo_cpf:
    soma += int(x) * contador
    contador -=1

# print(soma)

multiplicar = soma * 10
# print(multiplicar)
resto = 0
resto = multiplicar % 11
# print(resto)

if resto > 9:
  novo_cpf += '0'
  # print(novo_cpf)
else:
  novo_cpf += str(resto)

# cpf_formatado = '{}.{}.{}-{}'.format(novo_cpf[:3], novo_cpf[3:6], novo_cpf[6:9], novo_cpf[9:]) 
# print(cpf_formatado)

"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11
Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14
Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O segundo dígito do CPF é 0
"""
soma2 = 0
contador2 = 11
while(contador2 >=2):
   for x in novo_cpf:
    soma2 += int(x) * contador2
    contador2 -=1

# print(soma2)

multiplicar2 = soma2 * 10
# print(multiplicar2)
resto2 = 0
resto2 = multiplicar2 % 11
# print(resto2)

if resto2 > 9:
  novo_cpf += '0'
  # print(novo_cpf)
else:
  novo_cpf += str(resto2)

cpf_formatado = '{}.{}.{}-{}'.format(novo_cpf[:3], novo_cpf[3:6], novo_cpf[6:9], novo_cpf[9:]) 
if cpf_formatado == cpf:
  print(f'{cpf_formatado} é válido')
else:
  print(f'{cpf}, não é válido')