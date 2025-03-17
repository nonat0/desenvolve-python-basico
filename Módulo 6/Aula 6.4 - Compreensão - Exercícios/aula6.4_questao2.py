frase = input("Digite uma frase: ")

lista_vogais = "aeiouAEIOU"
vogais = sorted([l for l in frase if l in lista_vogais])
consoantes = [l for l in frase if l not in lista_vogais and l !=" "]

print("\nVogais ordenadas: ", vogais)
print("Consoantes: ", consoantes)