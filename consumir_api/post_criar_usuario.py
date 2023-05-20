# GET (Listar)
# POST (CADASTRAR)
# PUT (atualizar ou substituir)
# DELETE (deletar)
# HEAD (é semelhante ao GET, mas retorna apenas os cabeçalhos da resposta, sem o corpo da resposta)
import requests
from pprint import pprint

_print = print
# print = pprint

url = 'http://127.0.0.1:3001/users'

user_data = {
    "nome": "Vanessa",
    "password": "123456",
    "email": "vanessa@email.com"
}

response = requests.post(url, user_data)

if response.status_code >= 200 and response.status_code <= 299:
    # Sucesso
    print(response.status_code)
    print(response.reason)
    # print(response.text)
    print(response.json())
    # print('Bytes', response.content)
else:
    # Error
    print(response.status_code)
    print(response.reason)
    print(response.text)
    # print('Bytes', response.content)