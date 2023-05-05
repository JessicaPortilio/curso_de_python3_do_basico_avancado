# os.listdir para navegar em caminhos
# /Users/luizotavio/Desktop/EXEMPLO
# C:\Users\luizotavio\Desktop\EXEMPLO
# caminho = r'F:\\EXEMPLO'
import os

# caminho = r'F:\\EXEMPLO'
# print(caminho)

caminho = os.path.join('F:\EXEMPLO')

for item in os.listdir(caminho):
    print(item)
