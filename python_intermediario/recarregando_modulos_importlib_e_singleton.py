import importlib
import exercicio_com_funcoes

print(exercicio_com_funcoes.multiplicar)

for i in range(10):
    importlib.reload(exercicio_com_funcoes)
    print(i)

print('Fim')