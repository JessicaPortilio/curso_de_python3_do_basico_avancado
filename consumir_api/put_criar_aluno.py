# GET (Listar)
# POST (CADASTRAR)
# PUT (atualizar ou substituir)
# DELETE (deletar)
# HEAD (é semelhante ao GET, mas retorna apenas os cabeçalhos da resposta, sem o corpo da resposta)
import requests
from pprint import pprint
from get_token import token

_print = print
# print = pprint

url = 'http://127.0.0.1:3001/alunos/2'

headers = {
    'Authorization': token
}


aluno_data = {
    "nome": "Maria",
    "sobrenome": "Santos",
    # "email": "paula@email.com",
    # "idade": "35",
    # "peso": "60.04",
    # "altura": "1.70"
}

response = requests.put(url=url, json=aluno_data, headers=headers)

if response.status_code >= 200 and response.status_code <= 299:
    # Sucesso
    print(response.status_code)
    print(response.reason)
    # print(response.text)
    
    response_data = response.json()
    print(response_data)
    # aqui eu crio o token e coloco no token.txt
    # token = response_data['token']

    # with open('token.txt', 'w') as file:
    #     file.write(token)

    # print('Bytes', response.content)
else:
    # Error
    print(response.status_code)
    print(response.reason)
    print(response.text)
    # print('Bytes', response.content)