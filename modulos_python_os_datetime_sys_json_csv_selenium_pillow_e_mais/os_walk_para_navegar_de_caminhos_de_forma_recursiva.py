# os.walk para navegar de caminhos de forma recursiva
# os.walk é uma função que permite percorrer uma estrutura de diretórios de
# maneira recursiva. Ela gera uma sequência de tuplas, onde cada tupla possui
# três elementos: o diretório atual (root), uma lista de subdiretórios (dirs)
# e uma lista dos arquivos do diretório atual (files).
import os
from itertools import count

caminho = os.path.join('F:\EXEMPLO')
counter = count()

for root, dirs, files in os.walk(caminho):
    the_counter = next(counter)
    print(the_counter, 'Pasta atual', root)
    # Se tiver alguma pasta dentro da pasta EXEMPLO, ele vai mostrar
    for dir_ in dirs:
        print('  ', the_counter, 'Dir:', root)
    # Aqui mostra os arquivos
    for file_ in files:
        print('  ', the_counter, 'File:', file_)
        # caminho_completo_arquivo = os.path.join(root, file_)
        # print()
        # print(caminho_completo_arquivo)
        # NÃO FAÇA ISSO (VAI APAGAR TUDO DA PASTA)
        # os.unlink(caminho_completo_arquivo)
