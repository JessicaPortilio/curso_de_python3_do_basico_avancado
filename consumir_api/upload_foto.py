# GET (Listar)
# POST (CADASTRAR)
# PUT (atualizar ou substituir)
# DELETE (deletar)
# HEAD (é semelhante ao GET, mas retorna apenas os cabeçalhos da resposta, sem o corpo da resposta)
import requests
from pprint import pprint
from get_token import token
from mimetypes import MimeTypes
from requests_toolbelt import MultipartEncoder

_print = print
# print = pprint

mimetypes = MimeTypes()

nome_arquivo = 'foto.jpg'
mimetypes_arquivo = mimetypes.guess_type(nome_arquivo)[0]
# print(mimetypes_arquivo)

multipart = MultipartEncoder(fields={
    'aluno_id': '3',
    'foto': (nome_arquivo, open(nome_arquivo, 'rb'), mimetypes_arquivo)
    
})



url = 'http://127.0.0.1:3001/fotos'

headers = {
    'Authorization': token,
    'Content-Type': multipart.content_type
}

response = requests.post(url=url,  headers=headers, data=multipart)

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