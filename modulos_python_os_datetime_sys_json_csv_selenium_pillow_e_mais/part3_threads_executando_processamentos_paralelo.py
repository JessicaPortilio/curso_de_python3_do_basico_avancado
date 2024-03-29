# Threads - Executando processamentos em paralelo
from threading import Thread
from time import sleep


def vai_demorar(texto, tempo):
    sleep(tempo)
    print(texto)


t1 = Thread(target=vai_demorar, args=('Olá mundo!', 10))
t1.start()


while t1.is_alive():
    print('Esperando a thread')
    sleep(2)


print('Thread acabou')
