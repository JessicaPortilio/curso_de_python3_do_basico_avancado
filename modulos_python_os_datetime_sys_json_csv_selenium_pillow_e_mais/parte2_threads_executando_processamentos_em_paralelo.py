# Threads - Executando processamentos em paralelo
from threading import Thread
from time import sleep


def vai_demorar(texto, tempo):
    sleep(tempo)
    print(texto)


t1 = Thread(target=vai_demorar, args=('Olá mundo!', 8))
t1.start()

t2 = Thread(target=vai_demorar, args=('Hello World!', 2))
t2.start()

t3 = Thread(target=vai_demorar, args=('Oi Terra!', 5))
t3.start()


for i in range(20):
    print(i)
    sleep(.5)
