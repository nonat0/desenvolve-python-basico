import random
import math
soma = 0
x = int(input("Digite a quantidade de valores aleatórios desejados: "))

for i in range(x):
    rand = random.randint(0,100)
    print(rand)
    soma += rand

raiz = math.sqrt(soma)
print("A Raiz quadrada das somas é: ", raiz)