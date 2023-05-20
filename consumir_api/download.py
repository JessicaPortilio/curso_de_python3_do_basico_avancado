import requests

url = 'http://localhost:3001/images/1684354125962_11903.jpg'

nome_arquivo = url.split('/')[-1]
# print(nome_arquivo)

response = requests.get(url)

if response.status_code >= 200 and response.status_code <= 299:
    # Sucesso
    print(response.status_code)
    print(response.reason)
    # print(response.text)

    with open(nome_arquivo, 'wb') as file:
        file.write(response.content)


else:
    # Error
    print(response.status_code)
    print(response.reason)
    print(response.text)
    # print('Bytes', response.content)