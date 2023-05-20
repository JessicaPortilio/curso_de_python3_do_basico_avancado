# Threads - Executando processamentos em paralelo
from threading import Thread
from time import sleep


def vai_demorar(texto, tempo):
    sleep(tempo)
    print(texto)


t1 = Thread(target=vai_demorar, args=('Olá mundo!', 10))
t1.start()
t1.join()

print('Thread acabou')
