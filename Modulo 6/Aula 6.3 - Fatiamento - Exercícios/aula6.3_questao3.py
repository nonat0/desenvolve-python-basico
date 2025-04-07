import random

lista = [random.randint(-10, 10) for _ in range(20)]
print("Original:", lista)

max_negativos = 0
inicio_remover = 0
fim_remover = 0

for i in range(len(lista)):
    for j in range(i, len(lista)):
        sublista = lista[i:j+1]  
        negativos = sum(1 for num in sublista if num < 0)  
        
        if negativos > max_negativos:
            max_negativos = negativos
            inicio_remover = i
            fim_remover = j

del lista[inicio_remover:fim_remover+1]

print("Editada:", lista)
