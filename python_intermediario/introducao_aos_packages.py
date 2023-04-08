from sys import path
import introducao_packages.modulo
from introducao_packages import modulo
from introducao_packages import *
from introducao_packages.modulo import soma_do_modulo
# print(__name__)
# print(*path, sep='\n')
print(soma_do_modulo(1,2))
print(introducao_packages.modulo.soma_do_modulo(1,2))
print(modulo.soma_do_modulo(1,2))