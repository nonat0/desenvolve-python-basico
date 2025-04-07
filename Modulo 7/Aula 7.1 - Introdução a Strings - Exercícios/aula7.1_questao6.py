from collections import Counter

def encontrar_anagramas(frase, palavra):
    palavras = frase.split()
    anagramas = [p for p in palavras if Counter(p) == Counter(palavra)]
    return anagramas

frase = input("Digite uma frase: ")
palavra_objetivo = input("Digite a palavra objetivo: ")

resultado = encontrar_anagramas(frase, palavra_objetivo)
print("Anagramas:", resultado)
