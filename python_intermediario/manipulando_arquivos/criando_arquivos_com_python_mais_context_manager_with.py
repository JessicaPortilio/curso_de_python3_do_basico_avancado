# https://www.otaviomiranda.com.br/2020/normalizacao-unicode-em-python/
# Criando arquivos com Python + Context Manager with
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load
caminho_arquivo = 'F:/curso_de_python3_do_basico_avancado/python_intermediario/manipulando_arquivos/aula116.txt'
# caminho_arquivo = 'aula116.txt'

# arquivo = open(caminho_arquivo, 'w')
# 
# arquivo.close()

# abrindo o arquivo, escrevendo e fechando (with abre e fecha o arquivo)
# with open(caminho_arquivo, 'w') as arquivo:
#     arquivo.write('Escrevendo no arquivo\n') # write esreve no arquivo
#     arquivo.write('Continuando\n')


# abrindo o arquivo, escrevendo, lendo e fechando (with abre e fecha o arquivo)
with open(caminho_arquivo, 'w+', encoding='utf8') as arquivo: # w+ (w) ele apaga o que tem no arquivo
    # e escreve tudo e salva
    # já o a+ (a) não apaga o que tem no arquivo, 
    # ele deixa o que existe no arquivo e começa a escrever depois
    arquivo.write('Escrevendo no arquivo\n') # write esreve no arquivo
    arquivo.write('Continuando\n')
    arquivo.writelines(
        ('Escrevendo várias linhas\n', 'Tudo no writelines\n', 'Preste Atenção\n')
    )
    print('Primeira leitura')
    arquivo.seek(0, 0)
    print(arquivo.read()) # read() ler o que tem dentro do arquivo
    print()
    print()
    print('Lendo um de cada vez')
    arquivo.seek(0, 0)
    print(arquivo.readline(), end='')
    print(arquivo.readline().strip())
    print(arquivo.readline().strip())
    print()
    print()
    print('Readlines')
    arquivo.seek(0, 0)
    for linha in arquivo.readlines():
        print(linha.strip())
print('#' * 20)


# abrindo o arquivo, lendo e fechando (with abre e fecha o arquivo)
# with open(caminho_arquivo, 'r') as arquivo:
#    print(arquivo.read()) # read() ler o que tem dentro do arquivo