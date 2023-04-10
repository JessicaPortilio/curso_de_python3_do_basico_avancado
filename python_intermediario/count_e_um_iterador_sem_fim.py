# count é um iterador sem fim (itertools)

from itertools import count

c1 = count()
r1 = range(10)

print('c1', hasattr(c1, '__iter__')) # count é interavel
print('c1', hasattr(c1, '__next__')) # count é intereto
print('r1', hasattr(r1, '__iter__')) # range é interavel
print('r1', hasattr(r1, '__next__')) # range não é intereto

print('count')
for i in c1:
    if i > 100:
        break
    print(i)

print()
print('range')

for i in r1:
    print(i)