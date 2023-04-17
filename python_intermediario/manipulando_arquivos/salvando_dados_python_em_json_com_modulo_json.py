import json

pessoa = {
    'nome': 'Luiz Otávio 2',
    'sobrenome': 'Miranda',
    'enderecos': [
        {'rua': 'R1', 'numero': 32},
        {'rua': 'R2', 'numero': 55},
    ],
    'altura': 1.8,
    'numeros_preferidos': (2, 4, 6, 8, 10),
    'dev': True,
    'nada': None,
}
# #ensure_ascii=False tira "Luiz Ot\u00e1vio 2" e deixa assim "Luiz Ot�vio 2"
caminho_arquivo = 'F:/curso_de_python3_do_basico_avancado/python_intermediario/manipulando_arquivos/aula117.txt'
with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
    json.dump(pessoa, 
              arquivo,
              ensure_ascii=False,
              indent=2,
              )

with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
    pessoa = json.load(arquivo)
    # print(pessoa)
    print(pessoa['nome'])