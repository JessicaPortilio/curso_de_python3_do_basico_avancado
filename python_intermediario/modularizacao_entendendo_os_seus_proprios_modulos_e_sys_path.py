# Modularização - Entendendo os seus próprios módulos Python
# O primeiro módulo executado chama-se __main__
# Você pode importar outro módulo inteiro ou parte do módulo
# O python conhece a pasta onde o __main__ está e as pastas
# abaixo dele.
# Ele não reconhece pastas e módulos acima do __main__ por
# padrão
# O python conhece todos os módulos e pacotes presentes
# nos caminhos de sys.path

import sys
import retorno_de_valores_das_funcoes_return

# try:
#     import sys
#     sys.path.append('Colocar outro caminho do arquivo')
# except ModuleNotFoundError:
#     ...

# import agora eu poderia importar um arquivo de outro lugar

print('Este módulo se chama', __name__)

print(*sys.path, sep='\n')