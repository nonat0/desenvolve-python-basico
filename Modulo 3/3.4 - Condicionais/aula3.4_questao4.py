dist = float(input("Distância em km: "))
peso = float(input("Peso do produto empacotado em kg: "))

if peso > 10:
    frete = 10
else:
    frete = 0

if dist >= 0 and dist < 101:
    frete += peso
    print("Valor do frete: ", frete, "R$")

if dist >= 101 and dist <= 300:
    frete += peso * 1.5
    print ("Valor do frete: ", frete, "R$")

if dist > 300:
    frete += peso*2
    print("Valor do frete: ", frete, "R$")