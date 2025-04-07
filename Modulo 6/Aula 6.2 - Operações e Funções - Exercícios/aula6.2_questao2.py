import random
soma = 0

num_elementos = random.randint(5, 20)
elementos = [random.randint(1,10)for _ in range (num_elementos)]

for i in range(num_elementos):
    soma=soma + elementos[i]

media = soma/num_elementos

print("Lista: ",elementos)
print("Quantidade de elementos na lista: ",num_elementos)
print("Soma dos elementos: ",soma)
print("Média dos elementos: ",media)