n = int(input("Quantidade de números: "))
maior = 0

while n > 0:
    x = int(input("Número: "))
    if x > maior:
        maior = x
    n -= 1

print("Maior número:", maior)