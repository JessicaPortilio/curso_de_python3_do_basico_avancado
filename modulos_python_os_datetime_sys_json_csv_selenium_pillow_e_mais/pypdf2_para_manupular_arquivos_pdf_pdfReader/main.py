# # PyPDF2 para manipular arquivos PDF (Instalação)
# PyPDF2 é uma biblioteca de manipulação de arquivos PDF feita em Python puro,
# gratuita e de código aberto. Ela é capaz de ler, manipular, escrever e unir
# dados de arquivos PDF, assim como adicionar anotações, transformar páginas,
# extrair texto e imagens, manipular metadados, e mais.
# A documentação contém todas as informações necessárias para usar PyPDF2.
# Link: https://pypdf2.readthedocs.io/en/3.0.0/
# Ative seu ambiente virtual
# pip install pypdf2
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

from pathlib import Path

from PyPDF2 import PdfMerger, PdfReader, PdfWriter

PASTA_RAIZ = Path(__file__).parent
PASTA_ORIGINAIS = PASTA_RAIZ / 'pdfs_originais'
PASTA_NOVA = PASTA_RAIZ / 'arquivos_novos'

RELATORIO_BACEN = PASTA_ORIGINAIS / 'R20230512.pdf'
PASTA_NOVA.mkdir(exist_ok=True)


reader = PdfReader(RELATORIO_BACEN)

# print(len(reader.pages))

# for page in reader.pages:
#     print(page)
#     print()


page0 = reader.pages[0]
imagem0 = page0.images[0]


# print(page0.extract_text())
# Aqui estamos salvando uma imagem
# with open(PASTA_NOVA / imagem0.name, 'wb') as fp:
#     fp.write(imagem0.data)


write = PdfWriter()
# aqui salvando uma pagina do pdf
# write.add_page(page0)

# aqui salvando todas as páginas do pdf em um pdf
# with open(PASTA_NOVA / 'Novo_PDF.pdf', 'wb') as arquivo:
#     for page in reader.pages:
#         write.add_page(page)

#     write.write(arquivo)

# Colocar em dois pdf separados
# for i, page in enumerate(reader.pages):
#     write = PdfWriter()
#     with open(PASTA_NOVA / f'page{i}.pdf', 'wb') as arquivo:
#         write.add_page(page)
#         write.write(arquivo)


files = [
    PASTA_NOVA / 'page0.pdf',
    PASTA_NOVA / 'page1.pdf'
]

merger = PdfMerger()
for file in files:
    merger.append(file)

with open(PASTA_NOVA / 'merged.pdf', 'wb') as fp:
    merger.write(fp)
