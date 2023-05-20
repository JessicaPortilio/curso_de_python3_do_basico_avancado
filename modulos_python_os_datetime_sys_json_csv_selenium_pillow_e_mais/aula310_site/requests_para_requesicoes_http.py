# requests para requisições HTTP
# python -m http.server 3333
# Tutorial -> https://youtu.be/Qd8JT0bnJGs

import requests

# http:// -> 80
# httos: // -> 443
url = 'http://localhost:3333/'
response = requests.get(url)

print(response.status_code)
# print(response.headers)
# print(response.content)
# print(response.json)
print(response.text)
