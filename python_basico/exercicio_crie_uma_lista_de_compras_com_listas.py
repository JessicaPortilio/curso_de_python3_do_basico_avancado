"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de 
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com erros de indices inexistentes na lista
"""
import os

lista_compras = []
while True:
    opcao = input("""
                   MENU
    1 - Visualizar a lista de compras
    2 - Inserir itens na lista de compras 
    3 - Apagar itens da lista
    4 - Sair
""")

    if opcao == '1':
       os.system('cls')
       if lista_compras == []:
        print('Nada para listar')
       else:
        for i, nome in enumerate(lista_compras):
            print(i, nome)
        
    elif opcao == '2':
        os.system('cls')
        inseri = input('Informe o nome do produto: ')
        lista_compras.append(inseri)
        for i, nome in enumerate(lista_compras):
            print(i, nome)
        
    elif opcao == '3':
        os.system('cls')
        apagar = input('Digite o nome do produto que você deseja retirar da lista: ')
        lista_compras.remove(apagar)
        for i, nome in enumerate(lista_compras):
            print(i, nome)
        
    elif opcao == '4':
        print('Finalizado!')
        break
        
    else:
        print("Opção inválida. Tente novamente.")