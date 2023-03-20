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

cpf = '746.824.890-70'
novo_cpf = cpf.replace(".", "").replace("-", "")[:9]
soma = 0
multiplicar = 0

# print(novo_cpf)
contador = 10
while(contador >=2):
   for x in novo_cpf:
    soma += int(x) * contador
    contador -=1

print(soma)

multiplicar = soma * 10
print(multiplicar)
resto = 0
resto = multiplicar % 11
print(resto)

if resto > 9:
  novo_cpf += '0'
  print(novo_cpf)
else:
  novo_cpf += str(resto)

cpf_formatado = '{}.{}.{}-{}'.format(novo_cpf[:3], novo_cpf[3:6], novo_cpf[6:9], novo_cpf[9:]) 
print(cpf_formatado)