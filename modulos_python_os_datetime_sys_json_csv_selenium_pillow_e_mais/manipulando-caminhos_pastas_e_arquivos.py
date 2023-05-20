# https://www.youtube.com/watch?v=T17BTNKBeJY&ab_channel=Ot%C3%A1vioMiranda

# unlink() apaga
# rmdir() apaga a pasta
# rmtree(caminho_da_pasta)

from pathlib import Path

caminho_projeto = Path()
# print(caminho_projeto.absolute())
# print()

caminho_arquivo = Path(__file__)
# print(caminho_arquivo)
# print()

# print(caminho_arquivo.parent)
# print()

# print(caminho_arquivo.parent.parent)

ideias = caminho_arquivo.parent / 'ideias'

# print(ideias / 'arquivos.txt')


# print(Path.home() / 'Desktop')

criar = caminho_projeto.parent / 'arquivo.txt'
# criar.touch()
# # print(criar)

# criar.write_text('Olá mundo')
# print(criar.read_text())

# with criar.open('a+') as file:
#     file.write('Uma linha ')
#     file.write('Duas linha \n')

# print(criar.read_text())

criar_pasta = caminho_projeto.parent / 'Teste'

criar_pasta.mkdir(exist_ok=True)

criar_subpasta = criar_pasta / 'subpasta'
criar_subpasta.mkdir(exist_ok=True)

outro_arquivo = criar_subpasta / 'arquivo.txt'
outro_arquivo.touch()
outro_arquivo.write_text('Hey')
