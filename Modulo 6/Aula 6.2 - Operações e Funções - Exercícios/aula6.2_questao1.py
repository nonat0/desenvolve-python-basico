import random

lista = [random.randint(-100, 100) for _ in range (20)]

lista_ordenada = sorted(lista)

print("Lista Ordenada: ", lista_ordenada)
print("Lista Original: ", lista)
print("Maior Índice: ", lista_ordenada[-1])
print("Menor Índice: ", lista_ordenada[0])