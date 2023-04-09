from dados import produtos
import copy
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere nos produtos por deep copy (cópia profunda)

novo_produtos = [
        {**p, 'preco': round(p['preco'] * 1.1, 2 )}
        for p in copy.deepcopy(produtos)
    ]
print('---------------------------------------------------------')
print(*produtos, sep='\n')
print()
print('Aumente os preços dos produtos a seguir em 10%')
print()
print(*novo_produtos, sep='\n')
print()
print()
# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos ordenados por nome por deep copy (cópia produnda)

produtos_ordenados_por_nome = sorted(
    copy.deepcopy(novo_produtos),
    key=lambda p: p['nome'],
    reverse= True
)
print('---------------------------------------------------------')
print(*produtos, sep='\n')
print()
print('Ordene os produtos por nome decrescente')
print()
print(*produtos_ordenados_por_nome, sep='\n')
print()
print()
# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos ordenados por preco por deep copy (cópia produnda)


produtos_ordenados_por_preco = sorted(
       copy.deepcopy(produtos_ordenados_por_nome),
        key=lambda p: p['preco']
)
print('---------------------------------------------------------')
print(*produtos, sep='\n')
print()
print('Ordene os produtos por preco crescente')
print()
print(*produtos_ordenados_por_preco, sep='\n')
print()
print()