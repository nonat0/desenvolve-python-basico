import random
from collections import Counter

lista1 = [random.randint(0, 50) for _ in range(20)]
lista2 = [random.randint(0, 50) for _ in range(20)]

interseccao = list(set(lista1) & set(lista2))

interseccao.sort()

contagem_lista1 = Counter(lista1)
contagem_lista2 = Counter(lista2)

print("lista1", lista1)
print("lista2", lista2) 
print("interseccao", interseccao)    
print([('Número:', valor, 'Lista1:',(contagem_lista1[valor]), 'Lista 2:',(contagem_lista2[valor])) for valor in interseccao])